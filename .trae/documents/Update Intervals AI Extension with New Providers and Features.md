I will update the Intervals AI Coach extension to support new providers, model presets, localization, and auto-analysis.

### 1. Update `options.html`
- **Add Providers**: Add "Claude (Anthropic)" and "Gemini (Google)" to the provider dropdown.
- **Model Presets**: Implement a dynamic model selection system. When a provider is selected, the "Model Name" input will be supported by a `<datalist>` containing common models for that provider (e.g., `gpt-4o`, `claude-3-5-sonnet`, `gemini-1.5-pro`). This allows users to easily select a recommended model or type a custom one.
- **Fix Display**: Correct the "DeepSeek" option text encoding.
- **Language Selector**: Add a language selection dropdown (Auto / English / Chinese).
- **Auto-Analyze Setting**: Add a checkbox for "Auto-Analyze on Open".

### 2. Create `options.js`
- **Dynamic Presets**: Implement logic to update the Model Name datalist and API Base URL when a provider is selected.
    - **OpenAI**: `gpt-4o`, `gpt-4o-mini`, `gpt-3.5-turbo`
    - **DeepSeek**: `deepseek-chat`, `deepseek-coder`
    - **Claude**: `claude-3-5-sonnet-20240620`, `claude-3-opus-20240229`, `claude-3-haiku-20240307`
    - **Gemini**: `gemini-1.5-flash`, `gemini-1.5-pro`, `gemini-pro`
- **Localization**: Implement UI text switching (English/Chinese) based on user preference or browser default.
- **Settings Management**: Save/Load all settings including the new "Auto-Analyze" preference.

### 3. Update `background.js`
- **Multi-Provider Support**: Refactor `handleAnalysis` to handle different API protocols:
    - **OpenAI/DeepSeek**: Standard logic.
    - **Claude**: Add specific headers (`x-api-key`, `anthropic-version`) and request body format (`max_tokens`, `messages`).
    - **Gemini**: specific URL structure and JSON body (`contents` -> `parts`).
- **Prompt Handling**: Ensure the correct prompt file is loaded and injected with the user's language.

### 4. Update `content.js`
- **Auto-Analyze Logic**: Detect the "Auto-Analyze" setting. If enabled, automatically trigger the analysis when the user expands the AI Coach panel.

### 5. Verify `prompt.txt`
- Ensure the file content matches the user's "Sports Health Expert" template.