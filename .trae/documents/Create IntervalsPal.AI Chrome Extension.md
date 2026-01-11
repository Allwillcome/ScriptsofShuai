I will create a new directory `IntervalsPal.AI` and populate it with the Chrome Extension source code based on the PRD.

### 1. Project Setup
- Create directory: `/Users/wangshuaibo/Documents/ScriptsofShuai/Notes/Project/IntervalsPal.AI/`

### 2. Configuration (`manifest.json`)
- Implement Manifest V3.
- Define permissions: `activeTab`, `scripting`, `storage`.
- Define host permissions for `https://intervals.icu/*` and all URLs (for API access).
- Configure `content_scripts` (CSS/JS), `background` service worker, `options_ui`, and `action`.

### 3. Core Logic
- **`content.js`**:
    - Implement the Floating Widget (UI).
    - Implement the Expanded Card (Analysis Panel).
    - Implement Data Scraping (Activity title, summary, description from DOM).
    - Handle messages from/to background script.
- **`background.js`**:
    - Handle API proxying to avoid CORS.
    - Manage Prompt loading (User custom -> Built-in file -> Hardcoded fallback).
    - Handle "Emergency" icon click events (inject scripts if needed).
- **`styles.css`**:
    - Style the floating widget (fixed position, transitions).
    - Style the analysis card (Markdown rendering support, dark/light mode compatibility).

### 4. Settings Page (`options.html` & `options.js`)
- **UI**:
    - Provider selection (OpenAI, DeepSeek, API2D, Custom).
    - Fields for API Base URL, API Key, Model Name.
    - Custom Prompt text area.
- **Logic**:
    - Save/Load settings using `chrome.storage.sync`.
    - Auto-fill defaults based on selected provider.

### 5. Resources
- **`prompt.txt`**: Create the default prompt template as defined in the PRD (Persona, Output format).
- **`icon.png`**: (Note: I will not generate a binary image, but I will ensure the manifest references it. You may need to add an actual image file later).

### 6. Verification
- Since I cannot run a Chrome Extension directly in this environment, I will verify the file structure and syntax of the generated code.
