# Testing Guide for v0.2.1

**Version**: 0.2.1
**Release Date**: 2025-01-12
**Test Date**: _____________

## Overview

Version 0.2.1 introduces an **Agent-style architecture** with automatic workout format validation and self-correction. This guide helps you test the new features systematically.

---

## New Features to Test

### 1. Agent-Style Analysis with Self-Correction

**What Changed**:
- AI now automatically validates generated workout plans
- If validation fails, AI corrects the errors (up to 3 attempts)
- Ensures workouts comply with Intervals.icu format

**How to Test**:

1. Navigate to any Intervals.icu activity page (e.g., `https://intervals.icu/activities/123456`)
2. Click "Analyze" button in AI Coach widget
3. Observe the new 5-step progress:
   - ✅ Step 1: Scraping workout data from page
   - ✅ Step 2: Preparing AI analysis request
   - ⚙️ Step 3: Generating AI analysis
   - ⚙️ Step 4: Validating workout format
   - ⏳ Step 5: Rendering analysis results

4. Check if the generated workout plan contains code blocks marked as `intervals`
5. Verify that the workout format is correct:
   - Each line starts with `-` for steps
   - Contains duration (e.g., `10m`, `30s`) or distance (e.g., `5km`)
   - Contains intensity (e.g., `75%`, `Z2`, `200w`)

**Expected Behavior**:
- If the first attempt produces incorrect format, you should see:
  - Step 3 showing "Generating AI analysis (Attempt 2/3)"
  - Step 4 showing error details
- The final result should have properly formatted workout plans
- Console should show validation logs (open DevTools → Console)

**Test Cases**:

| Test ID | Description | Expected Result | Pass/Fail |
|---------|-------------|-----------------|-----------|
| TC-01 | Normal workout generation | Workout formatted correctly on first attempt | ☐ |
| TC-02 | Check console logs | Logs show AGENT_ANALYSIS_START, VALIDATION_COMPLETE | ☐ |
| TC-03 | Error handling | If format invalid, AI corrects (up to 3 attempts) | ☐ |
| TC-04 | Final validation | All workouts comply with Intervals.icu format | ☐ |

---

### 2. Enhanced Progress Feedback

**What Changed**:
- Progress steps increased from 4 to 5
- Real-time updates from background script
- Shows validation status and correction attempts

**How to Test**:

1. Click "Analyze" button
2. Observe progress indicators:
   - Icons change: ⏳ (pending) → ⚙️ (in-progress) → ✅ (completed)
   - Text updates dynamically (e.g., "Attempt 2/3")
   - Validation errors shown inline

**Expected Behavior**:
- Each step transitions smoothly
- Current step highlighted with spinning icon
- Completed steps show checkmark
- If correction needed, you see attempt number updates

**Test Cases**:

| Test ID | Description | Expected Result | Pass/Fail |
|---------|-------------|-----------------|-----------|
| TC-05 | Progress indicators visible | All 5 steps displayed | ☐ |
| TC-06 | Dynamic text updates | Attempt numbers update during correction | ☐ |
| TC-07 | Validation errors shown | Errors displayed in Step 4 if validation fails | ☐ |
| TC-08 | Visual feedback | Icons spin during in-progress, static when done | ☐ |

---

### 3. Operation Logging System

**What Changed**:
- All background operations are logged
- Logs stored in memory (last 100 operations)
- Console output for debugging

**How to Test**:

1. Open Chrome DevTools (F12)
2. Go to Console tab
3. Click "Analyze" button in the extension
4. Observe console logs:
   - `[INFO] ANALYZE_REQUEST_RECEIVED`
   - `[INFO] AGENT_ANALYSIS_START`
   - `[INFO] INITIAL_ANALYSIS_COMPLETE`
   - `[INFO] CODE_BLOCKS_EXTRACTED`
   - `[INFO] VALIDATION_COMPLETE`
   - `[SUCCESS] ANALYSIS_COMPLETE_VALID`

**Expected Behavior**:
- Logs appear in chronological order
- Each log has timestamp, level, operation name
- Error logs show stack traces

**Test Cases**:

| Test ID | Description | Expected Result | Pass/Fail |
|---------|-------------|-----------------|-----------|
| TC-09 | Logs visible in console | All log entries appear | ☐ |
| TC-10 | Log format correct | Timestamp, level, operation name visible | ☐ |
| TC-11 | Error logging | Errors show with stack trace | ☐ |
| TC-12 | Success logging | Success events logged with details | ☐ |

---

### 4. Workout Format Validator

**What Changed**:
- New `validator.js` module injected as content script
- Validates Intervals.icu workout syntax
- Provides detailed error messages

**How to Test**:

You can test the validator directly in the browser console:

1. Navigate to intervals.icu
2. Open DevTools Console
3. Test the validator:

```javascript
// Create validator instance
const validator = new IntervalsWorkoutValidator();

// Test valid workout
const validWorkout = `
Warmup
- 10m @ 60%

Main Set
- 5 x 3m @ 90% with 2m recovery

Cooldown
- 5m easy
`;

const result = validator.validate(validWorkout);
console.log(result);

// Test invalid workout
const invalidWorkout = `
No steps here
Just plain text
`;

const result2 = validator.validate(invalidWorkout);
console.log(result2);
```

**Expected Behavior**:
- Valid workout: `result.valid = true, errors = []`
- Invalid workout: `result.valid = false, errors = ['No workout steps found']`

**Test Cases**:

| Test ID | Description | Expected Result | Pass/Fail |
|---------|-------------|-----------------|-----------|
| TC-13 | Validate correct format | Returns valid=true | ☐ |
| TC-14 | Detect missing steps | Returns error 'No workout steps found' | ☐ |
| TC-15 | Detect missing duration | Returns warning about missing duration | ☐ |
| TC-16 | Detect missing intensity | Returns warning about missing intensity | ☐ |

---

## Integration Testing

### Scenario 1: Complete Analysis Flow

**Steps**:
1. Go to an Intervals.icu activity page
2. Click "Analyze"
3. Wait for completion
4. Verify result contains:
   - Analysis text
   - Workout plan in code block
   - Copy button on code block

**Expected**:
- All 5 progress steps complete
- Workout plan formatted correctly
- Copy button works
- No console errors

**Result**: ☐ Pass ☐ Fail

---

### Scenario 2: Format Correction

**Setup**:
To test correction, you may need to use a model that sometimes generates incorrect format (e.g., GPT-3.5-turbo with low temperature).

**Steps**:
1. Configure a less reliable model in settings
2. Click "Analyze"
3. Observe if validation detects errors
4. Verify AI attempts to correct

**Expected**:
- First attempt may have errors
- Step 3 shows "Attempt 2/3"
- Step 4 shows error details
- Final result is corrected

**Result**: ☐ Pass ☐ Fail ☐ N/A (no errors occurred)

---

### Scenario 3: Error Handling

**Steps**:
1. Set invalid API key in settings
2. Click "Analyze"
3. Verify error handling

**Expected**:
- Step 3 shows error icon (❌)
- Error message displayed
- Link to settings shown
- Console shows error log with stack trace

**Result**: ☐ Pass ☐ Fail

---

## Performance Testing

### Metrics to Measure

| Metric | Baseline (v0.2.0) | v0.2.1 | Notes |
|--------|-------------------|--------|-------|
| Time to first progress update | ~0ms | ____ms | |
| Total analysis time (no correction) | ~10-30s | ____s | |
| Total analysis time (with 1 correction) | N/A | ____s | |
| Console log count per analysis | ~5 | ____ | |
| Memory usage (DevTools → Memory) | ____ MB | ____ MB | |

---

## Regression Testing

Ensure existing features still work:

| Feature | Status | Notes |
|---------|--------|-------|
| Multi-AI provider support | ☐ Pass ☐ Fail | Test OpenAI, Claude, DeepSeek |
| One-click copy button | ☐ Pass ☐ Fail | Copy workout to clipboard |
| Settings page | ☐ Pass ☐ Fail | API key, model, prompt editing |
| Widget collapse/expand | ☐ Pass ☐ Fail | Toggle header |
| Manual injection (click icon) | ☐ Pass ☐ Fail | Click extension icon on intervals.icu |

---

## Browser Compatibility

| Browser | Version | Status | Notes |
|---------|---------|--------|-------|
| Chrome | ____ | ☐ Pass ☐ Fail | |
| Edge | ____ | ☐ Pass ☐ Fail | |
| Brave | ____ | ☐ Pass ☐ Fail | |

---

## Known Issues

Document any issues found during testing:

1.
2.
3.

---

## Sign-off

- [ ] All test cases passed
- [ ] No critical bugs found
- [ ] Performance acceptable
- [ ] Ready for release

**Tester**: _____________
**Date**: _____________
**Signature**: _____________

---

## Troubleshooting

### Issue: Validator not working

**Symptom**: No validation happening, workouts with errors pass through

**Solution**:
1. Check if validator.js is loaded: `typeof IntervalsWorkoutValidator` should return "function"
2. Check manifest.json includes validator.js in content_scripts
3. Check console for validator loading errors

### Issue: Progress not updating

**Symptom**: Progress stuck on step 3

**Solution**:
1. Check background script logs in service worker console
2. Verify `sendProgress()` is being called
3. Check if message listener in content.js is registered

### Issue: Corrections not happening

**Symptom**: Invalid workouts accepted without correction

**Solution**:
1. Check if `maxAttempts` is set correctly (should be 3)
2. Verify `validateWorkout()` is detecting errors
3. Check if AI is receiving correction prompt

---

**End of Testing Guide**
