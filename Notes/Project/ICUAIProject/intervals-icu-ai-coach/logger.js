/**
 * Operation Logger for Intervals.icu AI Coach
 * Logs all operations for debugging and analytics
 */

class OperationLogger {
  constructor() {
    this.logs = [];
    this.maxLogs = 100; // Keep last 100 logs
  }

  /**
   * Log an operation
   * @param {string} level - 'info', 'warn', 'error', 'success'
   * @param {string} operation - Operation name
   * @param {Object} details - Additional details
   */
  log(level, operation, details = {}) {
    const entry = {
      timestamp: new Date().toISOString(),
      level,
      operation,
      ...details
    };

    this.logs.push(entry);

    // Keep only last maxLogs entries
    if (this.logs.length > this.maxLogs) {
      this.logs.shift();
    }

    // Also log to console for debugging
    const consoleMethod = level === 'error' ? 'error' : level === 'warn' ? 'warn' : 'log';
    console[consoleMethod](`[${level.toUpperCase()}] ${operation}:`, details);

    // Save to storage periodically
    this.saveToStorage();

    return entry;
  }

  info(operation, details) {
    return this.log('info', operation, details);
  }

  warn(operation, details) {
    return this.log('warn', operation, details);
  }

  error(operation, details) {
    return this.log('error', operation, details);
  }

  success(operation, details) {
    return this.log('success', operation, details);
  }

  /**
   * Get recent logs
   * @param {number} count - Number of logs to retrieve
   * @returns {Array}
   */
  getRecent(count = 10) {
    return this.logs.slice(-count);
  }

  /**
   * Get logs by operation
   * @param {string} operation
   * @returns {Array}
   */
  getByOperation(operation) {
    return this.logs.filter(log => log.operation === operation);
  }

  /**
   * Get logs by level
   * @param {string} level
   * @returns {Array}
   */
  getByLevel(level) {
    return this.logs.filter(log => log.level === level);
  }

  /**
   * Clear all logs
   */
  clear() {
    this.logs = [];
    chrome.storage.local.remove('operationLogs');
  }

  /**
   * Save logs to Chrome storage
   */
  async saveToStorage() {
    try {
      await chrome.storage.local.set({
        operationLogs: this.logs
      });
    } catch (e) {
      console.error('Failed to save logs:', e);
    }
  }

  /**
   * Load logs from Chrome storage
   */
  async loadFromStorage() {
    try {
      const result = await chrome.storage.local.get(['operationLogs']);
      if (result.operationLogs) {
        this.logs = result.operationLogs;
      }
    } catch (e) {
      console.error('Failed to load logs:', e);
    }
  }

  /**
   * Export logs as JSON
   * @returns {string}
   */
  export() {
    return JSON.stringify(this.logs, null, 2);
  }

  /**
   * Get statistics
   * @returns {Object}
   */
  getStats() {
    const stats = {
      total: this.logs.length,
      byLevel: {},
      byOperation: {},
      recentErrors: []
    };

    this.logs.forEach(log => {
      // Count by level
      stats.byLevel[log.level] = (stats.byLevel[log.level] || 0) + 1;

      // Count by operation
      stats.byOperation[log.operation] = (stats.byOperation[log.operation] || 0) + 1;

      // Collect recent errors
      if (log.level === 'error') {
        stats.recentErrors.push(log);
      }
    });

    // Keep only last 5 errors
    stats.recentErrors = stats.recentErrors.slice(-5);

    return stats;
  }
}

// Create global logger instance
const logger = new OperationLogger();

// Load logs on startup
if (typeof chrome !== 'undefined' && chrome.storage) {
  logger.loadFromStorage();
}

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
  module.exports = OperationLogger;
}
