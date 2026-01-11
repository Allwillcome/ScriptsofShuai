# Intervals.icu AI Coach

> AI-powered workout analysis and personalized training plans for Intervals.icu

[![Chrome Web Store](https://img.shields.io/badge/Chrome-Extension-success)](https://chromewebstore.google.com)
[![Version](https://img.shields.io/badge/version-0.2.0-blue)](https://github.com/yourusername/intervals-icu-ai-coach/releases)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

Transform your training data into actionable insights with AI-powered analysis. Get personalized workout feedback and generate structured training plans in Intervals.icu format—all with a single click.

## ✨ Features

### 🎯 **AI-Powered Workout Analysis**
- **Instant Feedback**: Get professional-level analysis of your training sessions
- **Data-Driven Insights**: Heart rate zones, pace, power metrics analyzed automatically
- **Conversational Tone**: Friendly, coach-like feedback that's easy to understand

### 📋 **Personalized Training Plans** *(NEW in v0.2.0)*
- **Auto-Generated Workouts**: AI suggests next training session based on your performance
- **Intervals.icu Format**: Plans generated in native plain text format
- **One-Click Copy**: Copy workout plans with a single click to paste into Intervals.icu

### 🔧 **Flexible AI Provider Support**
- OpenAI (GPT-4, GPT-4o-mini)
- Anthropic (Claude)
- DeepSeek
- Google Gemini
- And 10+ more AI services

### 🔒 **Privacy-First Design**
- Your data stays between you, Intervals.icu, and your chosen AI service
- No data collection or tracking
- API keys stored locally on your device

## 🚀 Installation

### From Chrome Web Store
1. Visit [Chrome Web Store](https://chromewebstore.google.com) *(Coming Soon)*
2. Click "Add to Chrome"
3. Configure your API key in settings

### From Source
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/intervals-icu-ai-coach.git
   cd intervals-icu-ai-coach
   ```

2. Load the extension in Chrome:
   - Open `chrome://extensions/`
   - Enable "Developer mode"
   - Click "Load unpacked"
   - Select the `intervals-icu-ai-coach` folder

3. Configure your API key:
   - Click the extension icon
   - Go to Settings
   - Enter your AI provider API key

## 📖 Usage

### Basic Analysis
1. Navigate to any activity page on [Intervals.icu](https://intervals.icu)
2. Click the floating ⚡️ AI Coach widget
3. Click "Analyze" to get instant feedback

### Training Plan Generation
After analysis, you'll see a personalized workout plan like this:

```intervals
Warmup
- 15m 60%

Main Set 4x
- 5m 95-105%
- 3m 50%

Cooldown
- 10m 60%
```

Click the "Copy" button and paste directly into Intervals.icu workout builder!

### Intervals.icu Workout Format

The extension generates workouts in Intervals.icu plain text format:

| Element | Format | Example |
|---------|--------|---------|
| Time | `10m`, `30s`, `1m30`, `1h` | `15m 75%` |
| Distance | `5km`, `3mi` | `2km Z2` |
| Power (cycling) | `75%`, `200w`, `85-95%`, `Z2` | `20m 60-70%` |
| Pace (running) | `80% pace`, `Z3 Pace` | `1mi Z2 Pace` |
| Heart Rate | `70% HR`, `95% LTHR` | `10m 75% HR` |
| Repetitions | `4x` after section title | `Main Set 4x` |

**Full Format Documentation**: [ZonePace - Intervals Workout Format](https://zonepace.cc/intervals-workout-format)

## ⚙️ Configuration

### Supported AI Providers

| Provider | API Base URL | Model Example |
|----------|--------------|---------------|
| OpenAI | `https://api.openai.com/v1` | `gpt-4o-mini`, `gpt-4` |
| Anthropic (Claude) | `https://api.anthropic.com` | `claude-3-5-sonnet-20241022` |
| DeepSeek | `https://api.deepseek.com` | `deepseek-chat` |
| Google Gemini | `https://generativelanguage.googleapis.com/v1beta/models/` | `gemini-pro` |

### Getting API Keys

- **OpenAI**: [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- **Anthropic**: [console.anthropic.com](https://console.anthropic.com)
- **DeepSeek**: [platform.deepseek.com/api_keys](https://platform.deepseek.com/api_keys)

## 🛠️ Development

### Project Structure

```
ICUAIProject/
├── intervals-icu-ai-coach/    # Extension source code
│   ├── manifest.json          # Extension manifest
│   ├── content.js             # Content script (UI)
│   ├── background.js          # Background service worker (API calls)
│   ├── options.html           # Settings page
│   ├── options.js             # Settings logic
│   ├── styles.css             # Widget styles
│   ├── prompt.txt             # AI coaching prompt template
│   └── icons/                 # Extension icons (16/32/48/128)
├── docs/                      # Documentation
└── README.md                  # This file
```

### Building from Source

```bash
# Install dependencies (none required - vanilla JS!)

# Package for distribution
cd ICUAIProject
zip -r intervals-icu-ai-coach.zip intervals-icu-ai-coach/ -x "*.DS_Store" -x "__MACOSX"
```

### Contributing

Contributions are welcome! Please read [DEVELOPMENT_STANDARDS.md](./docs/DEVELOPMENT_STANDARDS.md) first.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📝 Changelog

### v0.2.0 (2025-01-07)
- ✨ **NEW**: AI-generated training plans in Intervals.icu format
- ✨ **NEW**: One-click copy button for workout plans
- 🌐 **CHANGED**: All UI and comments translated to English
- 🎨 **IMPROVED**: Enhanced markdown rendering with code block support
- 📚 **DOCS**: Added comprehensive Intervals.icu format documentation

### v0.1.0 (2025-01-06)
- 🎉 Initial release
- ✨ AI-powered workout analysis
- 🔧 Multi-provider AI support (OpenAI, Claude, DeepSeek, etc.)
- 🎨 Floating widget UI

## 🤝 Acknowledgments

- [Intervals.icu](https://intervals.icu) - Amazing training platform for endurance athletes
- [ZonePace](https://zonepace.cc) - Intervals.icu workout format documentation
- All contributors and users of this extension

## 📄 License

MIT License - see [LICENSE](./LICENSE) file for details

## 🔗 Links

- **Chrome Web Store**: *Coming Soon*
- **GitHub Repository**: [https://github.com/yourusername/intervals-icu-ai-coach](https://github.com/yourusername/intervals-icu-ai-coach)
- **Issue Tracker**: [GitHub Issues](https://github.com/yourusername/intervals-icu-ai-coach/issues)
- **Intervals.icu Forum**: [forum.intervals.icu](https://forum.intervals.icu)

---

**Made with ❤️ for endurance athletes**

**Sources:**
- [Intervals.icu Workout Builder Forum](https://forum.intervals.icu/t/workout-builder/1163)
- [Intervals.icu Workout Markdown Format](https://forum.intervals.icu/t/intervals-icu-workout-markdown-format-rules/115629)
- [ZonePace Intervals Format Documentation](https://zonepace.cc/intervals-workout-format)
