// 监听来自 content script 的消息
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "OPEN_OPTIONS") {
    chrome.runtime.openOptionsPage();
  }

  if (request.action === "ANALYZE_ACTIVITY") {
    // 异步处理需要 return true
    handleAnalysis(request.data, request.lang).then(result => {
      sendResponse({ success: true, result: result });
    }).catch(err => {
      console.error("Analysis failed:", err);
      sendResponse({ success: false, error: err.message });
    });
    return true; 
  }
});

// 点击插件图标时的逻辑 (急救功能)
chrome.action.onClicked.addListener(async (tab) => {
  if (tab.url && tab.url.includes("intervals.icu")) {
    try {
      await chrome.scripting.insertCSS({
        target: { tabId: tab.id },
        files: ["styles.css"]
      });
      await chrome.scripting.executeScript({
        target: { tabId: tab.id },
        files: ["content.js"]
      });
      console.log("已尝试手动注入 UI");
    } catch (e) {
      console.warn("注入失败:", e);
      chrome.runtime.openOptionsPage();
    }
  } else {
    chrome.runtime.openOptionsPage();
  }
});

async function handleAnalysis(activityData, lang) {
  try {
    // 1. 读取配置
    const config = await chrome.storage.sync.get(['provider', 'apiBaseUrl', 'apiKey', 'modelName', 'customPrompt']);
    
    if (!config.apiKey) {
      throw new Error("API Key missing. Please configure in settings.");
    }
    
    const provider = config.provider || 'openai';
    const apiUrl = config.apiBaseUrl || "https://api.openai.com/v1/chat/completions";
    const model = config.modelName || "gpt-4o-mini";

    // 2. 准备 Prompt
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

    const finalPrompt = `${systemPrompt}\n\nData: ${JSON.stringify(activityData)}`;

    // 3. 调用 API
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
    
    // 4. 解析响应
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
    console.error("HandleAnalysis Error:", error);
    throw error;
  }
}
