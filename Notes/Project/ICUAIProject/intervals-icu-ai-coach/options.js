// Localization
const i18n = {
  en: {
    settingsTitle: "⚙️ Intervals AI Settings",
    languageLabel: "Language / 语言",
    providerLabel: "AI Provider",
    selectProviderPlaceholder: "-- Select Provider --",
    customProvider: "Custom",
    baseUrlLabel: "API Base URL",
    modelNameLabel: "Model Name",
    getKeyLink: "👉 Get API Key",
    autoAnalyzeLabel: "Auto-Analyze when opening panel",
    promptLabel: "Custom Prompt",
    promptHint: "If empty, uses the default prompt from prompt.txt.",
    saveBtn: "Save Settings",
    saveSuccess: "✅ Saved!",
    saveError: "❌ Save Failed"
  },
  zh: {
    settingsTitle: "⚙️ Intervals AI 设置",
    languageLabel: "语言 / Language",
    providerLabel: "AI 服务商",
    selectProviderPlaceholder: "-- 请选择服务商 --",
    customProvider: "自定义 (Custom)",
    baseUrlLabel: "API 接口地址 (Base URL)",
    modelNameLabel: "模型名称 (Model Name)",
    getKeyLink: "👉 点此获取该平台的 API Key",
    autoAnalyzeLabel: "打开面板时自动开始分析",
    promptLabel: "自定义提示词 (Prompt)",
    promptHint: "如果不填，将使用 prompt.txt 中的默认提示词。",
    saveBtn: "保存配置",
    saveSuccess: "✅ 保存成功！",
    saveError: "❌ 保存失败"
  }
};

const PROVIDERS = {
  openai: {
    url: "https://api.openai.com/v1/chat/completions",
    models: ["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo"],
    keyUrl: "https://platform.openai.com/api-keys"
  },
  deepseek: {
    url: "https://api.deepseek.com/chat/completions",
    models: ["deepseek-chat", "deepseek-reasoner"],
    keyUrl: "https://platform.deepseek.com/api_keys"
  },
  claude: {
    url: "https://api.anthropic.com/v1/messages",
    models: ["claude-3-5-sonnet-20240620", "claude-3-opus-20240229", "claude-3-haiku-20240307"],
    keyUrl: "https://console.anthropic.com/settings/keys"
  },
  gemini: {
    url: "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent", // Will need to append key or handle in bg
    models: ["gemini-pro", "gemini-1.5-flash", "gemini-1.5-pro"],
    keyUrl: "https://aistudio.google.com/app/apikey"
  },
  api2d: {
    url: "https://openai.api2d.net/v1/chat/completions",
    models: ["gpt-4-turbo", "gpt-3.5-turbo"],
    keyUrl: "https://api2d.com/"
  }
};

// UI Elements
const els = {
  langSelect: document.getElementById('langSelect'),
  provider: document.getElementById('provider'),
  apiBaseUrl: document.getElementById('apiBaseUrl'),
  apiKey: document.getElementById('apiKey'),
  getKeyLink: document.getElementById('getKeyLink'),
  modelName: document.getElementById('modelName'),
  modelList: document.getElementById('modelList'),
  autoAnalyze: document.getElementById('autoAnalyze'),
  customPrompt: document.getElementById('customPrompt'),
  saveBtn: document.getElementById('saveBtn'),
  status: document.getElementById('status')
};

// Init
document.addEventListener('DOMContentLoaded', restoreOptions);
els.saveBtn.addEventListener('click', saveOptions);
els.provider.addEventListener('change', onProviderChange);
els.langSelect.addEventListener('change', updateLanguage);

function updateLanguage() {
  const lang = els.langSelect.value === 'auto' 
    ? (navigator.language.startsWith('zh') ? 'zh' : 'en') 
    : els.langSelect.value;
  
  const texts = i18n[lang] || i18n.en;
  
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (texts[key]) {
      if (el.tagName === 'INPUT' && el.type !== 'checkbox') {
        // For placeholders if needed, currently we use static placeholders but could translate
      } else {
        el.innerText = texts[key];
      }
    }
  });
}

function onProviderChange() {
  const key = els.provider.value;
  const config = PROVIDERS[key];
  if (config) {
    els.apiBaseUrl.value = config.url;
    
    // Update Key Link
    els.getKeyLink.href = config.keyUrl;
    els.getKeyLink.style.display = 'inline-block';
    
    // Update Model List
    els.modelList.innerHTML = '';
    config.models.forEach(m => {
      const option = document.createElement('option');
      option.value = m;
      els.modelList.appendChild(option);
    });
    
    // Auto-fill model if empty or not in list
    if (!els.modelName.value) {
      els.modelName.value = config.models[0];
    }
  } else {
    // Custom
    els.getKeyLink.style.display = 'none';
    els.modelList.innerHTML = '';
  }
}

function saveOptions() {
  const settings = {
    language: els.langSelect.value,
    provider: els.provider.value,
    apiBaseUrl: els.apiBaseUrl.value,
    apiKey: els.apiKey.value,
    modelName: els.modelName.value,
    autoAnalyze: els.autoAnalyze.checked,
    customPrompt: els.customPrompt.value
  };

  chrome.storage.sync.set(settings, () => {
    const lang = els.langSelect.value === 'auto' 
      ? (navigator.language.startsWith('zh') ? 'zh' : 'en') 
      : els.langSelect.value;
    els.status.textContent = i18n[lang].saveSuccess;
    els.status.style.display = 'inline';
    setTimeout(() => {
      els.status.style.display = 'none';
    }, 2000);
  });
}

function restoreOptions() {
  chrome.storage.sync.get({
    language: 'auto',
    provider: '',
    apiBaseUrl: '',
    apiKey: '',
    modelName: '',
    autoAnalyze: false,
    customPrompt: ''
  }, (items) => {
    els.langSelect.value = items.language;
    els.provider.value = items.provider;
    els.apiBaseUrl.value = items.apiBaseUrl;
    els.apiKey.value = items.apiKey;
    els.modelName.value = items.modelName;
    els.autoAnalyze.checked = items.autoAnalyze;
    els.customPrompt.value = items.customPrompt;

    updateLanguage();
    if (items.provider) {
      // Re-populate datalist, but don't overwrite user's custom URL/Model if they differ from default
      const config = PROVIDERS[items.provider];
      if (config) {
        els.getKeyLink.href = config.keyUrl;
        els.getKeyLink.style.display = 'inline-block';
        els.modelList.innerHTML = '';
        config.models.forEach(m => {
          const option = document.createElement('option');
          option.value = m;
          els.modelList.appendChild(option);
        });
      }
    }
  });
}
