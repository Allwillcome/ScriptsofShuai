/**
 * Operation Logger Instance
 * Logs all background operations for debugging
 */
class OperationLogger {
  constructor() {
    this.logs = [];
    this.maxLogs = 100;
  }

  log(level, operation, details = {}) {
    const entry = {
      timestamp: new Date().toISOString(),
      level,
      operation,
      ...details
    };

    this.logs.push(entry);
    if (this.logs.length > this.maxLogs) {
      this.logs.shift();
    }

    const consoleMethod = level === 'error' ? 'error' : level === 'warn' ? 'warn' : 'log';
    console[consoleMethod](`[${level.toUpperCase()}] ${operation}:`, details);

    return entry;
  }

  info(operation, details) { return this.log('info', operation, details); }
  warn(operation, details) { return this.log('warn', operation, details); }
  error(operation, details) { return this.log('error', operation, details); }
  success(operation, details) { return this.log('success', operation, details); }
}

const logger = new OperationLogger();

// Listen to messages from content script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "OPEN_OPTIONS") {
    chrome.runtime.openOptionsPage();
  }

  if (request.action === "ANALYZE_ACTIVITY") {
    logger.info('ANALYZE_REQUEST_RECEIVED', { tabId: sender.tab?.id });

    // Start async agent process
    handleAgentAnalysis(request.data, request.lang, sender.tab?.id).then(result => {
      sendResponse({ success: true, result: result });
    }).catch(err => {
      logger.error('ANALYSIS_FAILED', { error: err.message, stack: err.stack });
      sendResponse({ success: false, error: err.message });
    });
    return true;
  }
});

// Logic when clicking extension icon (emergency injection)
chrome.action.onClicked.addListener(async (tab) => {
  if (tab.url && tab.url.includes("intervals.icu")) {
    try {
      await chrome.scripting.insertCSS({
        target: { tabId: tab.id },
        files: ["styles.css"]
      });
      await chrome.scripting.executeScript({
        target: { tabId: tab.id },
        files: ["validator.js"]
      });
      await chrome.scripting.executeScript({
        target: { tabId: tab.id },
        files: ["content.js"]
      });
      logger.info('MANUAL_INJECTION_SUCCESS', { tabId: tab.id });
    } catch (e) {
      logger.error('INJECTION_FAILED', { error: e.message });
      chrome.runtime.openOptionsPage();
    }
  } else {
    chrome.runtime.openOptionsPage();
  }
});

/**
 * Send progress update to content script
 */
function sendProgress(tabId, stage, data = {}) {
  if (!tabId) return;

  chrome.tabs.sendMessage(tabId, {
    action: 'ANALYSIS_PROGRESS',
    stage: stage,
    data: data
  }).catch(err => {
    logger.warn('PROGRESS_SEND_FAILED', { stage, error: err.message });
  });
}

/**
 * Extract code blocks from markdown
 */
function extractCodeBlocks(markdown) {
  const codeBlocks = [];
  const pattern = /```(intervals)?\\n([\\s\\S]*?)```/g;
  let match;

  while ((match = pattern.exec(markdown)) !== null) {
    codeBlocks.push({
      lang: match[1] || 'text',
      code: match[2].trim()
    });
  }

  return codeBlocks;
}

/**
 * Validate Intervals.icu workout format
 * Simplified version - full validation happens in content script with validator.js
 */
function validateWorkout(workoutText) {
  const errors = [];
  const warnings = [];

  if (!workoutText || !workoutText.trim()) {
    errors.push('Workout is empty');
    return { valid: false, errors, warnings };
  }

  const lines = workoutText.trim().split('\\n');
  const stepPattern = /^\\s*-\\s+/;
  let hasSteps = false;

  for (const line of lines) {
    if (stepPattern.test(line)) {
      hasSteps = true;
      break;
    }
  }

  if (!hasSteps) {
    errors.push('No workout steps found (lines must start with "-")');
  }

  return {
    valid: errors.length === 0,
    errors,
    warnings
  };
}

/**
 * Agent-style analysis with self-correction
 * Workflow:
 * 1. Generate initial analysis + workout plan
 * 2. Validate workout format
 * 3. If invalid, ask AI to correct (max 3 attempts)
 * 4. Return validated result
 */
async function handleAgentAnalysis(activityData, lang, tabId) {
  const maxAttempts = 3;
  let attempt = 0;
  let finalResult = '';
  let validationErrors = [];

  try {
    logger.info('AGENT_ANALYSIS_START', { attempt: 1, maxAttempts });
    sendProgress(tabId, 'generating', { attempt: 1 });

    // Step 1: Generate initial analysis
    const initialResult = await callAI(activityData, lang, null);
    finalResult = initialResult;

    logger.info('INITIAL_ANALYSIS_COMPLETE', { length: initialResult.length });
    sendProgress(tabId, 'validating', { attempt: 1 });

    // Step 2: Extract and validate workout plans
    const codeBlocks = extractCodeBlocks(initialResult);
    const intervalsBlocks = codeBlocks.filter(block => block.lang === 'intervals');

    logger.info('CODE_BLOCKS_EXTRACTED', { total: codeBlocks.length, intervals: intervalsBlocks.length });

    if (intervalsBlocks.length === 0) {
      logger.warn('NO_INTERVALS_BLOCKS_FOUND', {});
      // No workout plans to validate, return as-is
      return finalResult;
    }

    // Validate each intervals block
    let allValid = true;
    const validationResults = [];

    for (const block of intervalsBlocks) {
      const validation = validateWorkout(block.code);
      validationResults.push(validation);

      if (!validation.valid) {
        allValid = false;
        validationErrors.push(...validation.errors);
      }
    }

    logger.info('VALIDATION_COMPLETE', {
      allValid,
      totalBlocks: intervalsBlocks.length,
      errors: validationErrors.length
    });

    // Step 3: Self-correction loop if validation failed
    attempt = 1;
    while (!allValid && attempt < maxAttempts) {
      attempt++;
      logger.info('SELF_CORRECTION_ATTEMPT', { attempt, errors: validationErrors });
      sendProgress(tabId, 'correcting', { attempt, errors: validationErrors });

      // Ask AI to fix the errors
      const correctionPrompt = `The workout plan you generated has formatting errors:\n\n${validationErrors.join('\\n')}\n\nPlease fix these errors and regenerate the workout plan in correct Intervals.icu format. Remember:\n- Each step must start with "-"\n- Include duration (e.g., 10m, 30s) or distance (e.g., 5km)\n- Include intensity (e.g., 75%, Z2, 200w)\n\nPrevious output:\n${finalResult}`;

      const correctedResult = await callAI(activityData, lang, correctionPrompt);
      finalResult = correctedResult;

      // Re-validate
      const newCodeBlocks = extractCodeBlocks(correctedResult);
      const newIntervalsBlocks = newCodeBlocks.filter(block => block.lang === 'intervals');

      validationErrors = [];
      allValid = true;

      for (const block of newIntervalsBlocks) {
        const validation = validateWorkout(block.code);
        if (!validation.valid) {
          allValid = false;
          validationErrors.push(...validation.errors);
        }
      }

      logger.info('CORRECTION_VALIDATION', {
        attempt,
        allValid,
        errorsRemaining: validationErrors.length
      });
    }

    if (allValid) {
      logger.success('ANALYSIS_COMPLETE_VALID', { attempts: attempt });
      sendProgress(tabId, 'complete', { valid: true, attempts: attempt });
    } else {
      logger.warn('ANALYSIS_COMPLETE_WITH_ERRORS', {
        attempts: attempt,
        errors: validationErrors
      });
      sendProgress(tabId, 'complete', {
        valid: false,
        attempts: attempt,
        errors: validationErrors
      });
    }

    return finalResult;

  } catch (error) {
    logger.error('AGENT_ANALYSIS_ERROR', { error: error.message, stack: error.stack });
    sendProgress(tabId, 'error', { error: error.message });
    throw error;
  }
}

/**
 * Call AI service (extracted from handleAnalysis)
 * @param {Object} activityData - Activity data to analyze
 * @param {string} lang - Language for response
 * @param {string|null} customUserPrompt - Optional custom prompt for correction
 */
async function callAI(activityData, lang, customUserPrompt = null) {
  try {
    // 1. Read configuration
    const config = await chrome.storage.sync.get(['provider', 'apiBaseUrl', 'apiKey', 'modelName', 'customPrompt']);

    if (!config.apiKey) {
      throw new Error("API Key missing. Please configure in settings.");
    }

    const provider = config.provider || 'openai';
    const apiUrl = config.apiBaseUrl || "https://api.openai.com/v1/chat/completions";
    const model = config.modelName || "gpt-4o-mini";

    // 2. Prepare prompt
    let systemPrompt = config.customPrompt;
    if (!systemPrompt) {
      try {
        const url = chrome.runtime.getURL('prompt.txt');
        const response = await fetch(url);
        if (!response.ok) throw new Error("Prompt file not found");
        const text = await response.text();
        systemPrompt = text.replace(/{{LANG}}/g, lang);
      } catch (e) {
        console.warn("Failed to load prompt.txt, using fallback:", e);
        systemPrompt = `You are a professional sports coach. Please analyze the following data in ${lang} and provide brief feedback.`;
      }
    }

    // Build final prompt
    let finalPrompt;
    if (customUserPrompt) {
      // For correction requests, use custom prompt
      finalPrompt = customUserPrompt;
    } else {
      // For initial analysis, use system prompt + data
      finalPrompt = `${systemPrompt}\n\nData: ${JSON.stringify(activityData)}`;
    }

    // 3. Call API
    let fetchOptions = {};
    let responseText = "";

    if (provider === 'claude') {
      // Anthropic / Claude
      fetchOptions = {
        method: 'POST',
        headers: {
          'x-api-key': config.apiKey,
          'anthropic-version': '2023-06-01',
          'content-type': 'application/json'
        },
        body: JSON.stringify({
          model: model,
          max_tokens: 1024,
          messages: [{ role: "user", content: finalPrompt }]
        })
      };
    } else if (provider === 'gemini') {
      // Google Gemini
      // URL usually needs ?key=API_KEY
      const urlWithKey = `${apiUrl}?key=${config.apiKey}`;
      fetchOptions = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          contents: [{ parts: [{ text: finalPrompt }] }]
        })
      };
      // Override URL for fetch
      var fetchUrl = urlWithKey; 
    } else {
      // OpenAI / DeepSeek / API2D / Custom (OpenAI Compatible)
      
      // Auto-fix URL if missing endpoint
      let url = apiUrl;
      if (!url.endsWith('/chat/completions') && !url.endsWith('/v1/messages')) {
         // Simple heuristic: if it looks like a base URL, append standard endpoint
         if (url.includes('deepseek') || url.includes('openai') || url.includes('api2d')) {
            if (url.endsWith('/')) {
                url += 'chat/completions';
            } else {
                url += '/chat/completions';
            }
         }
      }

      fetchOptions = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${config.apiKey}`
        },
        body: JSON.stringify({
          model: model,
          messages: [{ role: "user", content: finalPrompt }],
          temperature: 0.7
        })
      };
      
      // Update targetUrl to the normalized one
      if (provider !== 'gemini') {
         // We need to pass this new url to fetch
         // Since targetUrl is const defined later, we need to handle this.
         // Let's refactor slightly below.
      }
    }

    let targetUrl = apiUrl;
    if (provider === 'gemini') {
        targetUrl = fetchUrl;
    } else if (provider === 'claude') {
        targetUrl = apiUrl;
    } else {
        // Apply the fix logic again or use the one we calculated
         let url = apiUrl;
         if (!url.endsWith('/chat/completions') && !url.endsWith('/v1/messages')) {
            if (url.includes('deepseek') || url.includes('openai') || url.includes('api2d')) {
                url = url.endsWith('/') ? url + 'chat/completions' : url + '/chat/completions';
            }
         }
         targetUrl = url;
    }

    const res = await fetch(targetUrl, fetchOptions);

    if (!res.ok) {
      const errText = await res.text();
      let errMsg = errText;
      try {
        const errJson = JSON.parse(errText);
        if (errJson.error && errJson.error.message) errMsg = errJson.error.message;
      } catch(e) {}
      throw new Error(`API Request Failed (${res.status}): ${errMsg}`);
    }

    const json = await res.json();

    // 4. Parse response
    if (provider === 'claude') {
      if (json.content && json.content.length > 0) {
        return json.content[0].text;
      }
    } else if (provider === 'gemini') {
      if (json.candidates && json.candidates.length > 0 && json.candidates[0].content) {
        return json.candidates[0].content.parts[0].text;
      }
    } else {
      // OpenAI Compatible
      if (json.choices && json.choices.length > 0) {
        return json.choices[0].message.content;
      }
    }

    throw new Error("API returned empty content. Check model name or permissions.");

  } catch (error) {
    logger.error("CALL_AI_ERROR", { error: error.message, stack: error.stack });
    throw error;
  }
}
