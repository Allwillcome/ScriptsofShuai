// 避免重复注入
if (!document.getElementById('intervals-ai-root')) {
  initUI();
}

function initUI() {
  // 1. 创建悬浮球容器
  const container = document.createElement('div');
  container.id = 'intervals-ai-root';
  container.innerHTML = `
    <div class="iai-header" id="iai-toggle">
      <div class="iai-icon">⚡️</div>
      <div class="iai-title">AI Coach</div>
    </div>
    <div class="iai-content">
      <div id="iai-result-area">
        <p style="color:#666; font-size:13px;">点击分析，获取专业的运动解读。</p>
      </div>
      <button id="iai-analyze-btn" class="iai-btn">开始分析 (Analyze)</button>
      <div class="iai-settings-link" id="iai-go-settings">⚙️ 设置 API</div>
    </div>
  `;
  document.body.appendChild(container);

  // 2. 绑定交互事件
  const toggleBtn = document.getElementById('iai-toggle');
  const analyzeBtn = document.getElementById('iai-analyze-btn');
  const settingsBtn = document.getElementById('iai-go-settings');
  const resultArea = document.getElementById('iai-result-area');

  let hasAutoAnalyzed = false;

  // 展开/收起
  toggleBtn.addEventListener('click', () => {
    container.classList.toggle('expanded');
    
    // 自动分析逻辑
    if (container.classList.contains('expanded') && !hasAutoAnalyzed) {
      chrome.storage.sync.get(['autoAnalyze'], (items) => {
        if (items.autoAnalyze) {
          if (checkIsActivityPage()) {
             hasAutoAnalyzed = true; // 标记已自动分析过，避免重复触发
             analyzeBtn.click();
          }
        }
      });
    }
  });

  // 打开设置页
  settingsBtn.addEventListener('click', () => {
    chrome.runtime.sendMessage({ action: "OPEN_OPTIONS" });
  });

  // 点击分析
  analyzeBtn.addEventListener('click', async () => {
    if (!checkIsActivityPage()) {
        resultArea.innerHTML = "<p style='color:red'>请进入具体的运动详情页面后再点击分析。</p>";
        return;
    }

    analyzeBtn.disabled = true;
    analyzeBtn.textContent = "AI 正在思考...";
    resultArea.innerHTML = "<p>正在抓取数据并分析...</p>";

    try {
      // A. 抓取数据
      const data = scrapeIntervalsData();
      
      // B. 发送给后台处理 (跨域请求必须在后台做)
      // 注意：我们把抓到的数据传给 background
      chrome.runtime.sendMessage({ 
        action: "ANALYZE_ACTIVITY", 
        data: data,
        lang: navigator.language || "zh-CN"
      }, (response) => {
        analyzeBtn.disabled = false;
        analyzeBtn.textContent = "重新分析";

        if (response && response.success) {
          // 渲染结果
          resultArea.innerHTML = parseMarkdown(response.result);
        } else {
          resultArea.innerHTML = `<p style="color:red">分析失败: ${response.error || '未知错误'}</p>`;
          if (response && response.error && response.error.includes("API Key")) {
             resultArea.innerHTML += `<p><a style="cursor:pointer;text-decoration:underline" id="iai-fix-key">点击配置 API Key</a></p>`;
             document.getElementById('iai-fix-key').addEventListener('click', () => chrome.runtime.sendMessage({ action: "OPEN_OPTIONS" }));
          }
        }
      });

    } catch (e) {
      console.error(e);
      analyzeBtn.disabled = false;
      analyzeBtn.textContent = "重试";
      resultArea.innerHTML = `<p style="color:red">错误: ${e.message}</p>`;
    }
  });
}

function checkIsActivityPage() {
    return window.location.href.includes('/activities/');
}

// 简易数据抓取 (复用之前的逻辑)
function scrapeIntervalsData() {
  // 简单抓取页面可见文本，后续可优化
  const title = document.querySelector('h1')?.innerText || "";
  const summary = document.body.innerText.substring(0, 1500); 
  return { title, summary };
}

// 简易 Markdown 渲染
function parseMarkdown(text) {
  if (!text) return '';
  let html = text
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/^### (.*$)/gm, '<h3>$1</h3>')
      .replace(/^## (.*$)/gm, '<h3>$1</h3>') // h2 也转为 h3 避免太大
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/^\s*[\-\*•]\s+(.*$)/gm, '<div style="margin-left:1em">• $1</div>')
      .replace(/\n/g, '<br>');
  return `<div class="iai-markdown">${html}</div>`;
}
