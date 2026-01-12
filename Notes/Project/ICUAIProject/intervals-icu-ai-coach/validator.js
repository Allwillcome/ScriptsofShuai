/**
 * Intervals.icu Workout Format Validator
 * Validates workout plans against Intervals.icu plain text format specification
 */

class IntervalsWorkoutValidator {
  constructor() {
    // Time patterns
    this.timePattern = /\b(\d+h|\d+'|\d+m|\d+"|\d+s|\d+m\d+s?)\b/i;

    // Distance patterns
    this.distancePattern = /\b(\d+\.?\d*)(km|mi|m)\b/i;

    // Intensity patterns
    this.intensityPatterns = {
      percent: /\b(\d+)%\b/,
      watts: /\b(\d+)w\b/i,
      range: /\b(\d+)-(\d+)(%|w)\b/i,
      zone: /\bZ[1-7]\b/i,
      hr: /\b(\d+)%\s*(HR|LTHR)\b/i,
      pace: /\b(\d+)%\s*pace\b/i,
      ramp: /\bramp\s+(\d+)(%|w)-(\d+)(%|w)\b/i
    };

    // Repetition pattern
    this.repetitionPattern = /\b(\d+)x\b/i;

    // Step pattern (lines starting with -)
    this.stepPattern = /^\s*-\s+/;
  }

  /**
   * Main validation function
   * @param {string} workoutText - Workout plan text
   * @returns {Object} - { valid: boolean, errors: [], warnings: [], info: {} }
   */
  validate(workoutText) {
    const result = {
      valid: true,
      errors: [],
      warnings: [],
      info: {
        sections: 0,
        steps: 0,
        hasDuration: false,
        hasIntensity: false,
        hasRepetitions: false
      }
    };

    if (!workoutText || typeof workoutText !== 'string') {
      result.valid = false;
      result.errors.push('Workout text is empty or invalid');
      return result;
    }

    const lines = workoutText.trim().split('\n');

    if (lines.length === 0) {
      result.valid = false;
      result.errors.push('Workout is empty');
      return result;
    }

    let currentSection = null;
    let stepCount = 0;
    let sectionCount = 0;

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i].trim();

      // Skip empty lines
      if (!line) continue;

      // Check if it's a step (starts with -)
      if (this.stepPattern.test(line)) {
        stepCount++;
        result.info.steps++;

        // Validate step content
        const stepValidation = this.validateStep(line, i + 1);

        if (!stepValidation.valid) {
          result.valid = false;
          result.errors.push(...stepValidation.errors);
        }

        if (stepValidation.warnings.length > 0) {
          result.warnings.push(...stepValidation.warnings);
        }

        if (stepValidation.hasDuration) result.info.hasDuration = true;
        if (stepValidation.hasIntensity) result.info.hasIntensity = true;

      } else {
        // It's a section title
        sectionCount++;
        result.info.sections++;
        currentSection = line;

        // Check for repetitions
        if (this.repetitionPattern.test(line)) {
          result.info.hasRepetitions = true;
        }
      }
    }

    // Validation rules
    if (stepCount === 0) {
      result.valid = false;
      result.errors.push('No workout steps found (lines must start with "-")');
    }

    if (sectionCount === 0) {
      result.warnings.push('No section titles found (recommended: Warmup, Main Set, Cooldown)');
    }

    if (!result.info.hasDuration) {
      result.warnings.push('No duration or distance found in any step');
    }

    if (!result.info.hasIntensity) {
      result.warnings.push('No intensity targets found in any step');
    }

    return result;
  }

  /**
   * Validate individual step
   * @param {string} step - Step text (including leading "- ")
   * @param {number} lineNum - Line number for error reporting
   * @returns {Object} - Validation result
   */
  validateStep(step, lineNum) {
    const result = {
      valid: true,
      errors: [],
      warnings: [],
      hasDuration: false,
      hasIntensity: false
    };

    // Remove leading "- "
    const content = step.replace(this.stepPattern, '').trim();

    if (!content) {
      result.valid = false;
      result.errors.push(`Line ${lineNum}: Step has no content`);
      return result;
    }

    // Check for duration (time or distance)
    const hasTime = this.timePattern.test(content);
    const hasDistance = this.distancePattern.test(content);

    if (hasTime || hasDistance) {
      result.hasDuration = true;
    } else {
      result.warnings.push(`Line ${lineNum}: Step missing duration or distance`);
    }

    // Check for intensity
    const hasIntensity = Object.values(this.intensityPatterns).some(pattern =>
      pattern.test(content)
    );

    if (hasIntensity) {
      result.hasIntensity = true;
    } else {
      result.warnings.push(`Line ${lineNum}: Step missing intensity target`);
    }

    // Validate specific formats
    this.validateTimeFormat(content, lineNum, result);
    this.validateIntensityFormat(content, lineNum, result);

    return result;
  }

  /**
   * Validate time format
   */
  validateTimeFormat(content, lineNum, result) {
    // Check for common errors
    if (/\b\d+hr\b/i.test(content)) {
      result.warnings.push(`Line ${lineNum}: Use "1h" instead of "1hr"`);
    }

    if (/\b\d+min\b/i.test(content)) {
      result.warnings.push(`Line ${lineNum}: Use "10m" or "10'" instead of "10min"`);
    }

    if (/\b\d+sec\b/i.test(content)) {
      result.warnings.push(`Line ${lineNum}: Use "30s" or '30"' instead of "30sec"`);
    }
  }

  /**
   * Validate intensity format
   */
  validateIntensityFormat(content, lineNum, result) {
    // Check for percentage without %
    const matches = content.match(/\b(\d{2,3})\s+(FTP|HR|LTHR|pace)\b/i);
    if (matches) {
      result.warnings.push(`Line ${lineNum}: Add "%" symbol (e.g., "${matches[1]}% ${matches[2]}")`);
    }

    // Check for Zone without Z
    if (/\b(zone\s*[1-7])\b/i.test(content)) {
      result.warnings.push(`Line ${lineNum}: Use "Z1-Z7" instead of "Zone 1-7"`);
    }
  }

  /**
   * Quick format check (lighter validation)
   * @param {string} workoutText
   * @returns {boolean}
   */
  isValidFormat(workoutText) {
    const result = this.validate(workoutText);
    return result.valid && result.errors.length === 0;
  }

  /**
   * Get validation summary
   * @param {Object} validationResult
   * @returns {string}
   */
  getSummary(validationResult) {
    let summary = '';

    if (validationResult.valid && validationResult.errors.length === 0) {
      summary += '✅ Workout format is valid\n\n';
    } else {
      summary += '❌ Workout has errors:\n';
      validationResult.errors.forEach(err => {
        summary += `  • ${err}\n`;
      });
      summary += '\n';
    }

    if (validationResult.warnings.length > 0) {
      summary += '⚠️ Warnings:\n';
      validationResult.warnings.forEach(warn => {
        summary += `  • ${warn}\n`;
      });
      summary += '\n';
    }

    summary += `📊 Workout Info:\n`;
    summary += `  • Sections: ${validationResult.info.sections}\n`;
    summary += `  • Steps: ${validationResult.info.steps}\n`;
    summary += `  • Has Duration: ${validationResult.info.hasDuration ? 'Yes' : 'No'}\n`;
    summary += `  • Has Intensity: ${validationResult.info.hasIntensity ? 'Yes' : 'No'}\n`;
    summary += `  • Has Repetitions: ${validationResult.info.hasRepetitions ? 'Yes' : 'No'}\n`;

    return summary;
  }

  /**
   * Extract all code blocks from markdown text
   * @param {string} markdown - Markdown text potentially containing code blocks
   * @returns {Array} - Array of {lang: string, code: string}
   */
  static extractCodeBlocks(markdown) {
    const codeBlocks = [];
    const pattern = /```(intervals)?\n([\s\S]*?)```/g;
    let match;

    while ((match = pattern.exec(markdown)) !== null) {
      codeBlocks.push({
        lang: match[1] || 'text',
        code: match[2].trim()
      });
    }

    return codeBlocks;
  }

  /**
   * Validate all intervals code blocks in markdown
   * @param {string} markdown
   * @returns {Object} - {allValid: boolean, results: []}
   */
  validateMarkdown(markdown) {
    const codeBlocks = IntervalsWorkoutValidator.extractCodeBlocks(markdown);
    const results = [];
    let allValid = true;

    codeBlocks.forEach((block, index) => {
      if (block.lang === 'intervals') {
        const validation = this.validate(block.code);
        results.push({
          blockIndex: index,
          ...validation
        });

        if (!validation.valid || validation.errors.length > 0) {
          allValid = false;
        }
      }
    });

    return {
      allValid,
      blockCount: codeBlocks.length,
      results
    };
  }
}

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
  module.exports = IntervalsWorkoutValidator;
}
