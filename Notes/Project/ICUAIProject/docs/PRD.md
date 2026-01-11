# Product Requirements Document (PRD)
## Intervals.icu AI Coach

**Version**: 0.2.0
**Last Updated**: 2025-01-07
**Product Owner**: Shuaibo Wang
**Status**: In Development

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Problem Statement](#problem-statement)
3. [Product Vision](#product-vision)
4. [Target Users](#target-users)
5. [Features](#features)
6. [User Stories](#user-stories)
7. [Technical Specifications](#technical-specifications)
8. [Success Metrics](#success-metrics)
9. [Roadmap](#roadmap)
10. [Dependencies](#dependencies)

---

## Executive Summary

Intervals.icu AI Coach is a Chrome extension that brings AI-powered workout analysis and personalized training plan generation to Intervals.icu users. By leveraging various AI models (OpenAI, Claude, DeepSeek, etc.), the extension provides instant, professional-level coaching feedback and generates structured workout plans in Intervals.icu's native format.

---

## Problem Statement

### Current Pain Points

1. **Lack of Immediate Feedback**: Athletes using Intervals.icu must manually analyze their training data or wait for coach feedback
2. **Training Plan Creation**: Creating structured workouts in Intervals.icu format requires knowledge of the syntax
3. **Data Overload**: Users have access to rich training data but lack tools to interpret it quickly
4. **Coaching Cost**: Professional coaching is expensive and not accessible to all athletes

### Opportunity

- Intervals.icu has a growing user base of data-driven endurance athletes
- AI models are now capable of providing sophisticated training analysis
- Plain text workout format makes automated plan generation feasible

---

## Product Vision

**"Democratize professional-level coaching feedback for every endurance athlete using Intervals.icu"**

By combining AI's analytical capabilities with Intervals.icu's comprehensive training data, we empower athletes to:
- Understand their training patterns
- Receive actionable feedback instantly
- Generate evidence-based training plans
- Improve their performance systematically

---

## Target Users

### Primary Personas

#### 1. Self-Coached Athlete
- **Demographics**: 25-45 years old, 3-5 years training experience
- **Goals**: Improve performance, optimize training load
- **Pain Points**: Uncertain about training effectiveness, lacks professional guidance
- **Usage**: Uses after every key workout

#### 2. Data-Driven Enthusiast
- **Demographics**: 30-50 years old, tech-savvy, uses multiple training tools
- **Goals**: Maximum training insights, data-driven decisions
- **Pain Points**: Too much data, not enough interpretation
- **Usage**: Daily analysis, experimenting with different AI models

#### 3. Recreational Athlete
- **Demographics**: 20-60 years old, trains 3-5x/week
- **Goals**: Stay fit, enjoy training, avoid overtraining
- **Pain Points**: Doesn't know if training is effective
- **Usage**: Weekly check-ins, occasional deep dives

---

## Features

### v0.1.0 (Released 2025-01-06)

#### F1: AI-Powered Workout Analysis
**Status**: ✅ Shipped

- **Description**: Analyze workout data and provide coaching feedback
- **User Value**: Instant professional-level insights without coach cost
- **Technical Implementation**:
  - Content script scrapes Intervals.icu activity page
  - Background worker calls AI API
  - Results rendered in floating widget with markdown formatting

#### F2: Multi-AI Provider Support
**Status**: ✅ Shipped

- **Description**: Support 13+ AI service providers
- **User Value**: Flexibility, cost optimization, access to latest models
- **Supported Providers**:
  - OpenAI (GPT-4, GPT-4o-mini)
  - Anthropic (Claude 3.5 Sonnet)
  - DeepSeek
  - Google Gemini
  - And 10+ more

#### F3: Floating Widget UI
**Status**: ✅ Shipped

- **Description**: Non-intrusive floating widget on activity pages
- **User Value**: Easy access without disrupting Intervals.icu UX
- **Features**:
  - Collapsible/expandable
  - Draggable (planned)
  - Responsive design

### v0.2.0 (Released 2025-01-07)

#### F4: AI-Generated Training Plans
**Status**: ✅ Shipped

- **Description**: Generate next workout based on current performance
- **User Value**: Structured training progression, time savings
- **Technical Implementation**:
  - Enhanced prompt includes workout format specification
  - AI outputs Intervals.icu plain text format
  - Plans rendered in code blocks

#### F5: One-Click Workout Copy
**Status**: ✅ Shipped

- **Description**: Copy generated workouts to clipboard
- **User Value**: Seamless workflow from analysis to planning
- **Features**:
  - Copy button on code blocks
  - Visual feedback (button changes to "Copied!")
  - Clipboard API integration

#### F6: Detailed Progress Feedback
**Status**: ✅ Shipped

- **Description**: Show step-by-step progress during analysis
- **User Value**: Transparency, reduced perceived wait time
- **Steps Displayed**:
  1. Scraping workout data
  2. Preparing AI request
  3. Calling AI service (with time estimate)
  4. Rendering results

#### F7: English Localization
**Status**: ✅ Shipped

- **Description**: All UI and code comments in English
- **User Value**: Accessibility for international users
- **Scope**: UI text, code comments, documentation

### Upcoming Features

#### F8: Custom Prompt Templates
**Status**: 📋 Planned for v0.3.0

- **Description**: Users can save and switch between prompt templates
- **User Value**: Personalized coaching style
- **Acceptance Criteria**:
  - [ ] Save multiple prompts with names
  - [ ] Quick-switch dropdown in widget
  - [ ] Export/import templates

#### F9: Training Load Analysis
**Status**: 📋 Planned for v0.3.0

- **Description**: Multi-workout analysis, training load trends
- **User Value**: Long-term training optimization
- **Acceptance Criteria**:
  - [ ] Analyze last 7/14/30 days
  - [ ] Load/stress balance assessment
  - [ ] Recovery recommendations

#### F10: Workout Library
**Status**: 💡 Idea for v0.4.0

- **Description**: Save and organize generated workouts
- **User Value**: Reuse successful sessions, build workout catalog
- **Acceptance Criteria**:
  - [ ] Save workouts with tags
  - [ ] Search and filter
  - [ ] One-click reuse

---

## User Stories

### As a self-coached athlete...

**US1**: I want to analyze my workout immediately after finishing so that I can understand how effective it was
- **Acceptance Criteria**:
  - [x] Analysis completes in < 30 seconds
  - [x] Results include data-backed observations
  - [x] Feedback is actionable

**US2**: I want AI to suggest my next workout so that I can maintain progressive overload
- **Acceptance Criteria**:
  - [x] Suggested workout is based on current fitness
  - [x] Workout format is compatible with Intervals.icu
  - [x] I can copy the workout with one click

### As a data-driven enthusiast...

**US3**: I want to use different AI models so that I can compare analysis quality
- **Acceptance Criteria**:
  - [x] Can switch providers in settings
  - [x] All major AI providers supported
  - [x] API key configuration is secure

**US4**: I want to see exactly what the extension is doing so that I understand the process
- **Acceptance Criteria**:
  - [x] Progress steps are clearly labeled
  - [x] Current step is visually highlighted
  - [x] Errors are clearly explained

### As a recreational athlete...

**US5**: I want simple, friendly feedback so that I don't need to interpret complex data
- **Acceptance Criteria**:
  - [x] Feedback uses conversational language
  - [x] Key points are highlighted
  - [x] Technical terms are explained

**US6**: I want the extension to stay out of my way so that it doesn't disrupt my workflow
- **Acceptance Criteria**:
  - [x] Widget is collapsible
  - [x] Widget doesn't cover important content
  - [ ] Widget position is customizable (planned)

---

## Technical Specifications

### Architecture

```
┌─────────────────┐
│ Intervals.icu   │
│ Activity Page   │
└────────┬────────┘
         │
         v
┌─────────────────┐
│  Content Script │  ← Scrapes data, renders UI
│   (content.js)  │
└────────┬────────┘
         │
         v
┌─────────────────┐
│ Background      │  ← Calls AI APIs
│  Service Worker │
│ (background.js) │
└────────┬────────┘
         │
         v
┌─────────────────┐
│   AI Services   │  ← OpenAI, Claude, etc.
│   (External)    │
└─────────────────┘
```

### Data Flow

1. **Scraping**: Content script extracts activity title and summary from DOM
2. **Processing**: Background worker prepares AI prompt with scraped data
3. **API Call**: Background worker sends request to configured AI service
4. **Rendering**: Content script receives response and renders markdown
5. **Interaction**: User can copy generated workouts to clipboard

### Technology Stack

- **Frontend**: Vanilla JavaScript, CSS3
- **Extension APIs**: Chrome Extension Manifest V3
- **AI Integration**: REST APIs (OpenAI-compatible)
- **Storage**: chrome.storage.sync for configuration
- **Rendering**: Custom markdown parser

### Security & Privacy

- **No Data Collection**: Extension doesn't send data to developer servers
- **Local Storage**: API keys stored in chrome.storage.sync (encrypted)
- **User Control**: All data sent to AI is user-initiated
- **Open Source**: Code is publicly auditable (planned)

---

## Success Metrics

### Adoption Metrics
- Chrome Web Store installs
- Daily Active Users (DAU)
- Weekly Active Users (WAU)
- User retention (D1, D7, D30)

### Engagement Metrics
- Analyses per user per week
- Average session duration
- Feature usage breakdown
- Return rate

### Quality Metrics
- User ratings (Chrome Web Store)
- Error rate
- API response time
- User feedback sentiment

### Business Metrics
- User acquisition cost (UAC)
- User churn rate
- Feature adoption rate
- NPS score

---

## Roadmap

### Phase 1: MVP (✅ Completed)
**Timeline**: 2025-01 Week 1
**Goal**: Launch basic analysis functionality

- [x] F1: AI-powered workout analysis
- [x] F2: Multi-AI provider support
- [x] F3: Floating widget UI

### Phase 2: Enhanced Experience (✅ Completed)
**Timeline**: 2025-01 Week 2
**Goal**: Add training plan generation

- [x] F4: AI-generated training plans
- [x] F5: One-click workout copy
- [x] F6: Detailed progress feedback
- [x] F7: English localization

### Phase 3: Customization (📋 Planned)
**Timeline**: 2025-02 Week 1-2
**Goal**: User personalization

- [ ] F8: Custom prompt templates
- [ ] F9: Training load analysis
- [ ] Widget position customization
- [ ] Multiple language support

### Phase 4: Advanced Features (💡 Future)
**Timeline**: 2025-03+
**Goal**: Power user features

- [ ] F10: Workout library
- [ ] Multi-workout analysis
- [ ] Training plan builder (multi-week)
- [ ] Social features (share analysis)

---

## Dependencies

### External Dependencies
- **Intervals.icu**: Activity page structure must remain consistent
- **AI Services**: API availability and pricing
- **Chrome**: Extension APIs and policies

### Technical Dependencies
- Manifest V3 compatibility
- chrome.storage.sync availability
- Clipboard API support
- Fetch API for AI calls

### Business Dependencies
- Chrome Web Store approval
- User adoption of Intervals.icu
- AI API cost sustainability

---

## Risks & Mitigation

### Risk 1: AI API Costs
**Severity**: Medium
**Mitigation**:
- User brings own API key
- Optimize prompts for token efficiency
- Support cost-effective providers (DeepSeek)

### Risk 2: Intervals.icu Changes
**Severity**: High
**Mitigation**:
- Robust data scraping with fallbacks
- Monitor Intervals.icu updates
- Quick response team for fixes

### Risk 3: Chrome Store Rejection
**Severity**: High
**Mitigation**:
- Follow all guidelines strictly
- Clear privacy policy
- Responsive developer support

### Risk 4: User Retention
**Severity**: Medium
**Mitigation**:
- Continuous value delivery
- Regular feature updates
- Community engagement

---

## Open Questions

1. Should we support offline analysis with local AI models?
2. How to monetize while keeping core features free?
3. Should we build a web app in addition to Chrome extension?
4. What's the optimal balance between automation and user control?

---

## Appendix

### A. Competitive Analysis
- **TrainingPeaks Coach**: $20/month, human coaches
- **Stryd PowerCenter**: Focused on running, no AI
- **Intervals.icu Native**: No AI analysis features

### B. User Research
- Forum feedback: Users want quick insights
- Survey results: 73% would use AI coaching
- Interview insights: Trust is key concern

### C. Technical References
- [Chrome Extension Documentation](https://developer.chrome.com/docs/extensions/)
- [Intervals.icu API](https://intervals.icu/api)
- [OpenAI API](https://platform.openai.com/docs)

---

**Document History**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1.0 | 2025-01-06 | Shuaibo Wang | Initial draft |
| 0.2.0 | 2025-01-07 | Shuaibo Wang | Added training plan features, progress feedback |

---

**Approval**

- [ ] Product Owner: _______________
- [ ] Tech Lead: _______________
- [ ] Design Lead: _______________
