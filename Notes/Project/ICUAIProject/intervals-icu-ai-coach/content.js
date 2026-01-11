// Avoid duplicate injection
if (!document.getElementById('intervals-ai-root')) {
  initUI();
}

function initUI() {
  // 1. Create floating widget container
  const container = document.createElement('div');
  container.id = 'intervals-ai-root';
  container.innerHTML = `
    <div class="iai-header" id="iai-toggle">
      <div class="iai-icon">⚡️</div>
      <div class="iai-title">AI Coach</div>
    </div>
    <div class="iai-content">
      <div id="iai-result-area">
        <p style="color:#666; font-size:13px;">Click Analyze to get professional workout insights.</p>
      </div>
      <button id="iai-analyze-btn" class="iai-btn">Analyze</button>
      <div class="iai-settings-link" id="iai-go-settings">⚙️ Settings</div>
    </div>
  `;
  document.body.appendChild(container);

  // 2. 绑定交互事件
  const toggleBtn = document.getElementById('iai-toggle');
  const analyzeBtn = document.getElementById('iai-analyze-btn');
  const settingsBtn = document.getElementById('iai-go-settings');
  const resultArea = document.getElementById('iai-result-area');

  let hasAutoAnalyzed = false;

  // Toggle expand/collapse
  toggleBtn.addEventListener('click', () => {
    container.classList.toggle('expanded');

    // Auto-analyze logic
    if (container.classList.contains('expanded') && !hasAutoAnalyzed) {
      chrome.storage.sync.get(['autoAnalyze'], (items) => {
        if (items.autoAnalyze) {
          if (checkIsActivityPage()) {
             hasAutoAnalyzed = true; // Mark as auto-analyzed to avoid duplicate triggers
             analyzeBtn.click();
          }
        }
      });
    }
  });

  // Open settings page
  settingsBtn.addEventListener('click', () => {
    chrome.runtime.sendMessage({ action: "OPEN_OPTIONS" });
  });

  // Click analyze
  analyzeBtn.addEventListener('click', async () => {
    if (!checkIsActivityPage()) {
        resultArea.innerHTML = "<p style='color:red'>Please navigate to an activity details page first.</p>";
        return;
    }

    analyzeBtn.disabled = true;
    analyzeBtn.textContent = "Analyzing...";

    // Show progress steps
    showProgressSteps(resultArea);

    try {
      // Step 1: Scraping data
      updateProgressStep(1, 'in-progress');
      await sleep(300); // Small delay for visual feedback
      const data = scrapeIntervalsData();
      updateProgressStep(1, 'completed');

      // Step 2: Preparing request
      updateProgressStep(2, 'in-progress');
      await sleep(200);
      updateProgressStep(2, 'completed');

      // Step 3: Calling AI
      updateProgressStep(3, 'in-progress');

      // B. Send to background for processing
      chrome.runtime.sendMessage({
        action: "ANALYZE_ACTIVITY",
        data: data,
        lang: navigator.language || "en-US"
      }, (response) => {
        if (response && response.success) {
          updateProgressStep(3, 'completed');

          // Step 4: Rendering results
          updateProgressStep(4, 'in-progress');
          setTimeout(() => {
            updateProgressStep(4, 'completed');

            // Show final results after a brief moment
            setTimeout(() => {
              resultArea.innerHTML = parseMarkdown(response.result);
              addCopyButtonsToCodeBlocks();
              analyzeBtn.disabled = false;
              analyzeBtn.textContent = "Re-Analyze";
            }, 300);
          }, 200);
        } else {
          updateProgressStep(3, 'error');
          setTimeout(() => {
            resultArea.innerHTML = `<p style="color:red">Analysis failed: ${response.error || 'Unknown error'}</p>`;
            if (response && response.error && response.error.includes("API Key")) {
               resultArea.innerHTML += `<p><a style="cursor:pointer;text-decoration:underline" id="iai-fix-key">Click to configure API Key</a></p>`;
               document.getElementById('iai-fix-key').addEventListener('click', () => chrome.runtime.sendMessage({ action: "OPEN_OPTIONS" }));
            }
            analyzeBtn.disabled = false;
            analyzeBtn.textContent = "Retry";
          }, 500);
        }
      });

    } catch (e) {
      console.error(e);
      updateProgressStep(1, 'error');
      setTimeout(() => {
        resultArea.innerHTML = `<p style="color:red">Error: ${e.message}</p>`;
        analyzeBtn.disabled = false;
        analyzeBtn.textContent = "Retry";
      }, 500);
    }
  });
}

function checkIsActivityPage() {
    return window.location.href.includes('/activities/');
}

// Helper function to show progress steps
function showProgressSteps(container) {
  const steps = [
    { id: 1, text: 'Scraping workout data from page' },
    { id: 2, text: 'Preparing AI analysis request' },
    { id: 3, text: 'Calling AI service (this may take 10-30s)' },
    { id: 4, text: 'Rendering analysis results' }
  ];

  let html = '<div class="iai-progress-container">';
  steps.forEach(step => {
    html += `
      <div class="iai-progress-step" data-step="${step.id}">
        <div class="iai-progress-icon" id="step-icon-${step.id}">⏳</div>
        <div class="iai-progress-text">${step.text}</div>
      </div>
    `;
  });
  html += '</div>';

  container.innerHTML = html;
}

// Helper function to update progress step status
function updateProgressStep(stepId, status) {
  const iconEl = document.getElementById(`step-icon-${stepId}`);
  const stepEl = document.querySelector(`[data-step="${stepId}"]`);

  if (!iconEl || !stepEl) return;

  // Remove previous status classes
  stepEl.classList.remove('pending', 'in-progress', 'completed', 'error');
  stepEl.classList.add(status);

  // Update icon
  switch(status) {
    case 'in-progress':
      iconEl.textContent = '⚙️';
      iconEl.classList.add('spinning');
      break;
    case 'completed':
      iconEl.textContent = '✅';
      iconEl.classList.remove('spinning');
      break;
    case 'error':
      iconEl.textContent = '❌';
      iconEl.classList.remove('spinning');
      break;
    default:
      iconEl.textContent = '⏳';
      iconEl.classList.remove('spinning');
  }
}

// Helper function for delays
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// Simple data scraping
function scrapeIntervalsData() {
  // Simply scrape visible page text, can be optimized later
  const title = document.querySelector('h1')?.innerText || "";
  const summary = document.body.innerText.substring(0, 1500);
  return { title, summary };
}

// Enhanced Markdown rendering with code block support
function parseMarkdown(text) {
  if (!text) return '';

  // Extract code blocks first (to avoid interfering with other replacements)
  const codeBlocks = [];
  let codeBlockIndex = 0;
  text = text.replace(/```(intervals)?\n([\s\S]*?)```/g, (match, lang, code) => {
    const placeholder = `__CODEBLOCK_${codeBlockIndex}__`;
    codeBlocks.push({ lang: lang || 'text', code: code.trim() });
    codeBlockIndex++;
    return placeholder;
  });

  // Standard markdown processing
  let html = text
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/^### (.*$)/gm, '<h3>$1</h3>')
      .replace(/^## (.*$)/gm, '<h3>$1</h3>') // Convert h2 to h3 to avoid being too large
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/^\s*[\-\*•]\s+(.*$)/gm, '<div style="margin-left:1em">• $1</div>')
      .replace(/\n/g, '<br>');

  // Restore code blocks with proper HTML
  codeBlockIndex = 0;
  html = html.replace(/__CODEBLOCK_(\d+)__/g, () => {
    const block = codeBlocks[codeBlockIndex++];
    const escapedCode = block.code
        .replace(/&amp;/g, "&")
        .replace(/&lt;/g, "<")
        .replace(/&gt;/g, ">"); // Unescape for code block
    return `<div class="iai-code-block" data-lang="${block.lang}">
      <div class="iai-code-header">
        <span class="iai-code-lang">${block.lang === 'intervals' ? 'Intervals.icu Workout' : block.lang}</span>
        <button class="iai-copy-btn" title="Copy to clipboard">Copy</button>
      </div>
      <pre><code>${escapeHtml(escapedCode)}</code></pre>
    </div>`;
  });

  return `<div class="iai-markdown">${html}</div>`;
}

// HTML escape helper
function escapeHtml(unsafe) {
  return unsafe
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
}

// Add copy buttons functionality to code blocks
function addCopyButtonsToCodeBlocks() {
  const copyButtons = document.querySelectorAll('.iai-copy-btn');
  copyButtons.forEach(btn => {
    btn.addEventListener('click', function() {
      const codeBlock = this.closest('.iai-code-block');
      const code = codeBlock.querySelector('code').textContent;

      navigator.clipboard.writeText(code).then(() => {
        const originalText = this.textContent;
        this.textContent = 'Copied!';
        this.style.background = '#10b981';

        setTimeout(() => {
          this.textContent = originalText;
          this.style.background = '';
        }, 2000);
      }).catch(err => {
        console.error('Failed to copy:', err);
        this.textContent = 'Failed';
        setTimeout(() => {
          this.textContent = 'Copy';
        }, 2000);
      });
    });
  });
}
