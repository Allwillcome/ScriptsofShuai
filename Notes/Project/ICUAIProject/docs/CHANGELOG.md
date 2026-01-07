# Changelog

All notable changes to Intervals.icu AI Coach will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2026-01-01

### Added
- Support for 10 additional AI service providers:
  - Anthropic (Claude)
  - Google AI (Gemini)
  - Cohere
  - Baidu AI (文心一言)
  - Alibaba Cloud (通义千问)
  - Zhipu AI (ChatGLM)
  - Moonshot AI (Kimi)
  - iFlytek (讯飞星火)
  - Azure OpenAI
  - Hugging Face
- Comprehensive privacy policy documentation
- Detailed README with setup instructions
- Chrome Web Store listing materials

### Changed
- Updated `host_permissions` to use specific AI service domains instead of wildcard
- Improved security by removing overly broad permissions
- Enhanced error handling for API calls
- Updated UI for better responsiveness

### Fixed
- Version number consistency across manifest.json and version.json
- Improved extension icon resolution

### Security
- Removed `*://*/*` permission for better security compliance
- Added specific host permissions for each supported AI service
- Enhanced API key storage security

## [2.0.0] - 2024-01-28

### Added
- Auto-analyze feature (optional setting)
- Customizable AI prompt template
- Support for multiple languages in analysis output
- Settings page with user-friendly configuration
- DeepSeek AI support
- API2D proxy support

### Changed
- Migrated to Manifest V3
- Redesigned floating widget UI
- Improved content script injection reliability

### Fixed
- Widget position on different screen sizes
- Multiple injection prevention
- Storage sync issues

## [1.2.0] - 2023-12-15

### Added
- Initial support for OpenAI GPT models
- Custom prompt editing capability
- Language selection option

### Changed
- Improved analysis prompt for better output quality
- Enhanced CSS styling for better readability

### Fixed
- Widget not appearing on some Intervals.icu pages
- API error handling improvements

## [1.1.0] - 2023-11-20

### Added
- Collapsible widget interface
- Settings page for API configuration
- Base URL customization for different API providers

### Changed
- Updated UI with modern design
- Improved error messages

### Fixed
- Extension icon display issues
- Storage permission handling

## [1.0.0] - 2023-10-15

### Added
- Initial release
- Basic AI analysis integration for Intervals.icu
- OpenAI ChatGPT support
- Floating widget on activity pages
- Simple settings interface
- Markdown-formatted AI responses

---

## Roadmap

### Planned for v2.2.0
- [ ] Batch analysis for multiple activities
- [ ] Analysis history saving (optional)
- [ ] Export analysis as PDF or image
- [ ] Custom training plan suggestions
- [ ] Integration with workout calendar

### Future Considerations
- [ ] Offline mode with cached models
- [ ] Comparison analysis between activities
- [ ] Training trend visualization
- [ ] Community-shared prompts library
- [ ] Mobile browser support (if feasible)

---

## Legend

- **Added** - New features
- **Changed** - Changes in existing functionality
- **Deprecated** - Soon-to-be removed features
- **Removed** - Removed features
- **Fixed** - Bug fixes
- **Security** - Security improvements
