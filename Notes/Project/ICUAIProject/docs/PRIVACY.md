# Privacy Policy for Intervals.icu AI Coach

**Last Updated:** January 1, 2026
**Version:** 2.1

## Overview

Intervals.icu AI Coach is a browser extension that provides AI-powered analysis of your training data from Intervals.icu. We are committed to protecting your privacy and being transparent about how your data is handled.

## Data Collection

### What Data We Collect

This extension collects and processes the following data:

1. **Training Data from Intervals.icu**
   - Activity metrics (heart rate, pace, duration, zones, etc.)
   - Sleep data (if available)
   - Workout descriptions and metadata

2. **User Settings**
   - AI service provider selection (OpenAI, DeepSeek, Claude, etc.)
   - API keys for your chosen AI service
   - Language preferences
   - Auto-analysis preferences

### What Data We DO NOT Collect

- We do NOT collect any personal identification information
- We do NOT track your browsing history
- We do NOT share your data with third parties (except the AI service you choose)
- We do NOT store your training data on any servers

## How We Use Your Data

### Local Storage Only

- All your settings and API keys are stored **locally on your device** using Chrome's storage API
- Your training data is **never stored** by this extension
- Data is only read from Intervals.icu pages when you explicitly trigger analysis

### Third-Party AI Services

When you click "Analyze":

1. The extension reads your current activity data from the Intervals.icu page
2. Sends this data to **your chosen AI service** (using your own API key)
3. Displays the AI's response in the extension interface

**Important:** The data is sent directly to the AI service provider you configure. Please review their privacy policies:

- [OpenAI Privacy Policy](https://openai.com/privacy/)
- [Anthropic Privacy Policy](https://www.anthropic.com/privacy)
- [DeepSeek Privacy Policy](https://www.deepseek.com/privacy)
- [Google AI Privacy Policy](https://policies.google.com/privacy)
- [Cohere Privacy Policy](https://cohere.com/privacy)
- Other providers: Please check their respective websites

## Data Security

- **API Keys:** Stored locally using Chrome's `chrome.storage.sync` API with encryption
- **No Server Storage:** We do not operate any servers that store your data
- **HTTPS Only:** All API communications use secure HTTPS connections
- **No Analytics:** We do not use any analytics or tracking services

## Your Rights

You have the right to:

- **Access:** View all data stored by the extension in the Settings page
- **Delete:** Remove all stored data by uninstalling the extension or clearing extension data
- **Control:** Choose which AI service to use or disable the extension at any time

## Data Retention

- Settings and API keys: Retained until you uninstall the extension or manually clear them
- Training data: Not retained; only processed in real-time when you trigger analysis

## Third-Party Services

This extension connects to the following services:

### Required Services
- **Intervals.icu:** Source of your training data (not affiliated with this extension)

### Optional AI Services (You Choose)
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

You must provide your own API key for your chosen service. We are not responsible for the privacy practices of these third-party services.

## Changes to Privacy Policy

We may update this privacy policy from time to time. Changes will be reflected in the "Last Updated" date above and in the extension's changelog.

## Contact

If you have questions about this privacy policy or data handling, please:

- Open an issue on our GitHub repository (if applicable)
- Contact via the Chrome Web Store support page

## Permissions Explanation

This extension requests the following permissions:

- **activeTab:** To read training data from the current Intervals.icu page
- **scripting:** To inject the AI Coach interface into Intervals.icu pages
- **storage:** To save your settings and API keys locally
- **host_permissions:** To communicate with Intervals.icu and your chosen AI service API

## Compliance

This extension complies with:
- Chrome Web Store Developer Program Policies
- GDPR principles (data minimization, user control, transparency)
- Privacy by design principles

---

**Note:** This extension is an independent tool and is not officially affiliated with Intervals.icu or any AI service provider.
