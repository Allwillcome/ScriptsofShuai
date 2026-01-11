# Changelog

All notable changes to Intervals.icu AI Coach will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Documentation for development workflow
- Unit tests for core functions (planned)

---

## [0.2.0] - 2025-01-07

### ✨ Added
- **AI-Generated Training Plans**: AI now suggests personalized next workout based on current performance
  - Plans generated in native Intervals.icu plain text format
  - Includes Warmup, Main Set, and Cooldown sections
  - Appropriate intensity and duration based on fitness level
- **One-Click Copy Button**: Code blocks now have a copy button in top-right corner
  - Click to copy workout to clipboard
  - Visual feedback with "Copied!" message
  - Smooth animation on interaction
- **Detailed Progress Feedback**: Analysis process now shows step-by-step progress
  - Step 1: Scraping workout data from page
  - Step 2: Preparing AI analysis request
  - Step 3: Calling AI service (with time estimate)
  - Step 4: Rendering analysis results
  - Each step shows status icon (⏳ pending, ⚙️ in-progress, ✅ completed, ❌ error)
  - Current step highlighted with background color
- **Intervals.icu Format Documentation**: Comprehensive guide saved in `docs/INTERVALS_ICU_WORKOUT_FORMAT.md`
  - Complete syntax reference
  - Training zones table
  - Multiple examples
  - Best practices
  - Community resources

### 🌐 Changed
- **English Localization**: All UI text and code comments translated to English
  - Widget messages
  - Button labels
  - Progress steps
  - Error messages
  - Code comments
- **Enhanced Prompt**: Updated `prompt.txt` with training plan generation instructions
  - Includes Intervals.icu format specification
  - Clear examples
  - Zone definitions
- **Improved Markdown Rendering**: Enhanced `parseMarkdown()` function
  - Support for code blocks with language identifier
  - Proper HTML escaping
  - Better formatting

### 📚 Documentation
- Created `PRD.md` - Product Requirements Document
  - Features roadmap
  - User stories
  - Technical specifications
  - Success metrics
- Created `CHANGELOG.md` - Version history tracking
- Created `INTERVALS_ICU_WORKOUT_FORMAT.md` - Format reference guide

### 🐛 Fixed
- None in this release

### 🔒 Security
- No security changes

---

## [0.1.0] - 2025-01-06

### ✨ Added
- **Initial Release** - First public version of Intervals.icu AI Coach
- **AI-Powered Workout Analysis**: Analyze training data with AI
  - Natural language coaching feedback
  - Data-driven insights
  - Actionable recommendations
- **Multi-AI Provider Support**: Compatible with 13+ AI services
  - OpenAI (GPT-4, GPT-4o-mini, GPT-3.5-turbo)
  - Anthropic (Claude 3.5 Sonnet, Claude 3 Opus)
  - DeepSeek (deepseek-chat)
  - Google Gemini
  - API2D proxy
  - And 8 more providers
- **Floating Widget UI**: Non-intrusive interface on Intervals.icu
  - Collapsible/expandable design
  - Fixed position on activity pages
  - Clean, modern styling
  - Smooth animations
- **Secure Configuration**: Settings page for API management
  - Provider selection dropdown
  - API key storage (chrome.storage.sync)
  - Custom API endpoint support
  - Model selection
  - Custom prompt editing
- **Content Scraping**: Automatic data extraction from activity pages
  - Activity title
  - Activity description
  - Summary statistics (truncated to 1500 chars)
- **Markdown Rendering**: Basic markdown support in results
  - Headers (H2, H3)
  - Bold text
  - Lists
  - Line breaks
- **Error Handling**: User-friendly error messages
  - API key missing notification
  - Network error handling
  - Quick link to settings

### 📚 Documentation
- Created `README.md` with installation and usage instructions
- Created `LICENSE` file (MIT)
- Created `.gitignore` for development
- Created `docs/chrome-store-submission.md` for store listing

### 🛠️ Technical
- **Extension Structure**:
  - Manifest V3 compliant
  - Content script injection on `intervals.icu/*`
  - Background service worker for API calls
  - Options page for configuration
- **Icons**: Four sizes generated (16x16, 32x32, 48x48, 128x128)
- **Development Standards**: Created `DEVELOPMENT_STANDARDS.md`
  - Chrome extension guidelines
  - Icon requirements
  - Manifest configuration rules
  - Code quality standards

### 🐛 Fixed
- Chrome Web Store rejection: "Could not decode image"
  - Regenerated all icons from original 2048x2048 source
  - Updated manifest paths to `icons/` subdirectory

### 🗂️ Project Structure
- Reorganized from `IntervalsAI` to `ICUAIProject`
- Separated plugin code (`intervals-icu-ai-coach/`) from documentation (`docs/`)
- Deleted duplicate `IntervalsPal.AI` directory

---

## Version Naming Convention

- **Major version (X.0.0)**: Breaking changes, major features
- **Minor version (0.X.0)**: New features, backwards compatible
- **Patch version (0.0.X)**: Bug fixes, minor improvements

---

## Comparison Links

- [Unreleased changes](https://github.com/yourusername/intervals-icu-ai-coach/compare/v0.2.0...HEAD)
- [0.2.0 vs 0.1.0](https://github.com/yourusername/intervals-icu-ai-coach/compare/v0.1.0...v0.2.0)

---

## Categories Explained

- **Added**: New features
- **Changed**: Changes to existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security-related changes

---

**Note**: For detailed commit history, see [GitHub Commits](https://github.com/yourusername/intervals-icu-ai-coach/commits)
