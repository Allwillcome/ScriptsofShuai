# Intervals.icu AI Coach 🏃‍♂️⚡️

An intelligent Chrome extension that brings AI-powered training analysis directly to your Intervals.icu experience. Get instant, personalized insights about your workouts, sleep, and health data using advanced AI models.

![Version](https://img.shields.io/badge/version-2.1-blue)
![Chrome Web Store](https://img.shields.io/badge/chrome-extension-green)

## Features

- **🤖 AI-Powered Analysis**: Get expert-level insights on your training data using state-of-the-art AI models
- **🌐 Multiple AI Providers**: Support for 13+ AI services including OpenAI, Claude, DeepSeek, Gemini, and more
- **🎯 Context-Aware**: Analyzes heart rate zones, pace, duration, load, and recovery metrics
- **🌍 Multi-Language**: Supports analysis in multiple languages
- **⚙️ Flexible Configuration**: Easy-to-use settings page for API configuration
- **🔒 Privacy-First**: All data stays between you, Intervals.icu, and your chosen AI service
- **⚡️ One-Click Analysis**: Embedded floating widget on Intervals.icu pages
- **📊 Smart Insights**: Friendly, actionable advice tailored to your training patterns

## Supported AI Services

- OpenAI (ChatGPT)
- Anthropic (Claude)
- DeepSeek
- Google AI (Gemini)
- Cohere
- Baidu AI (文心一言)
- Alibaba Cloud (通义千问)
- Zhipu AI (ChatGLM)
- Moonshot AI (Kimi)
- iFlytek (讯飞星火)
- Azure OpenAI
- Hugging Face
- API2D

## Installation

### From Chrome Web Store
1. Visit the [Chrome Web Store page](#) (coming soon)
2. Click "Add to Chrome"
3. Follow the setup instructions

### Manual Installation (Developer Mode)
1. Clone or download this repository
2. Open Chrome and navigate to `chrome://extensions/`
3. Enable "Developer mode" in the top right
4. Click "Load unpacked"
5. Select the extension directory

## Setup

### 1. Configure Your AI Service

1. Click the extension icon in your toolbar
2. Click "⚙️ 设置 API" to open settings
3. Enter your API credentials:
   - **API Key**: Your AI service API key
   - **Base URL**: The API endpoint (or use default)
   - **Model**: Choose your preferred model
   - **Language**: Select analysis language

### 2. Get Your API Key

Choose an AI service and get your API key:

- **OpenAI**: [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- **Anthropic**: [console.anthropic.com](https://console.anthropic.com/)
- **DeepSeek**: [platform.deepseek.com](https://platform.deepseek.com/)
- **Google AI**: [makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

### 3. Optional Settings

- **Auto-analyze**: Automatically analyze when opening an activity
- **Custom Prompt**: Modify the analysis style (advanced)

## Usage

1. Navigate to any activity page on [Intervals.icu](https://intervals.icu)
2. Look for the **⚡️ AI Coach** floating widget on the right side
3. Click the header to expand the widget
4. Click **"开始分析 (Analyze)"** to get AI insights
5. Read your personalized training analysis

## Example Analysis Output

The AI Coach provides:

- **Overall impression** of your workout with specific data points
- **2-4 short observations** combining context, data, and advice
- **Actionable recommendations** for your next training session
- **Natural, friendly tone** like talking to a knowledgeable coach

## Privacy & Security

- **No data collection**: We don't collect or store any of your data
- **Local storage only**: Settings stored on your device
- **Direct API calls**: Data sent only to your chosen AI service
- **You control everything**: Use your own API keys, choose your provider

Read our full [Privacy Policy](PRIVACY.md).

## Permissions Explained

- **activeTab**: Read training data from Intervals.icu pages
- **scripting**: Inject the AI Coach interface
- **storage**: Save your settings locally
- **host_permissions**: Connect to Intervals.icu and AI services

## Troubleshooting

### No Analysis Results?
- Check your API key is valid
- Verify your API credits/quota
- Check browser console for error messages

### Widget Not Showing?
- Refresh the Intervals.icu page
- Click the extension icon to reset UI
- Make sure you're on an activity page

### API Error Messages?
- Verify Base URL is correct for your provider
- Check your API key hasn't expired
- Ensure sufficient API credits

## Development

### Project Structure
```
IntervalsAI/
├── manifest.json       # Extension configuration
├── content.js          # Main content script
├── background.js       # Service worker
├── options.html        # Settings page UI
├── options.js          # Settings page logic
├── styles.css          # UI styles
├── prompt.txt          # AI analysis prompt template
├── icon.png            # Extension icon
└── version.json        # Version info
```

### Build & Package
```bash
# Create distribution zip
zip -r IntervalsAI-v2.1.zip . -x "*.git*" "*.DS_Store" "node_modules/*"
```

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Disclaimer

This extension is an independent tool and is **not officially affiliated** with Intervals.icu or any AI service provider.

## Support

- Report bugs via GitHub Issues
- Feature requests welcome
- Questions? Open a discussion

## Acknowledgments

- Thanks to [Intervals.icu](https://intervals.icu) for the amazing platform
- Built with love for the endurance sports community

---

Made with ⚡️ by athletes, for athletes
