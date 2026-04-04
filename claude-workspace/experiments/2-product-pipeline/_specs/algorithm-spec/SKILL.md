---
name: algorithm-spec
description: Use when writing algorithm requirements documents, specifications, or logic documentation that involves decision trees, edge cases, and iterative improvements
---

# Algorithm Spec

## Overview

Algorithm spec is a documentation pattern for algorithm requirements that prioritizes clarity, boundary conditions, and iterative improvement. Define terms first, then logic, then admit limitations.

## When to Use

```
Need to document algorithm logic? → Yes
  │
  ├─ Is it a multi-step decision process?
  │   └─ Yes → Use algorithm-spec
  │
  └─ Does it have edge cases or exceptions?
      └─ Yes → Use algorithm-spec
```

Use when:
- Writing algorithm requirements or specifications
- Documenting decision trees or flow-based logic
- Describing systems with multiple input conditions
- Working on logic that will be implemented by others or your future self

## Core Pattern

**Before** (typical ad-hoc documentation):
- Mix of logic and examples
- Terms defined inline when first used
- Edge cases scattered or missing
- No discussion of limitations

**After** (algorithm-spec pattern):
```
1. Key Terms Definition → 2. Input → 3. Core Logic → 4. Limitations
```

## Structure

### 1. Key Terms Definition

Define all terms and assumptions upfront. This avoids ambiguity and ensures shared understanding.

**Format**: List format (not tables)

### 2. Input

Clearly specify what data/parameters the algorithm requires.

**Format**: List with parameter names and descriptions

### 3. Core Logic

Present the decision tree or flow. Use code blocks for visual clarity.

Include edge cases directly in the logic branches (not separate section).

### 4. Detailed Steps (Optional)

If logic is complex, add detailed execution steps after core logic.

**Format**: Numbered list

### 5. Limitations and Future Improvements

Honestly acknowledge current limitations and how they could be improved.

**Format**: List with "Current" and "Future" descriptions

## Format Guidelines

- **Avoid tables** - Use lists instead (better for Feishu/collaborative docs)
- **Use code blocks** - For decision trees and flows
- **No emoji markers** - Keep text professional and AI-neutral
- **Include examples** - Each logic branch should have a concrete example

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Defining terms inline when first used | Move all definitions to front |
| Scattering edge cases throughout | Include edge cases in logic branches |
| Using tables that break in collaborative tools | Use lists instead |
| No discussion of limitations | Always include limitations section |
| Examples without concrete values | Use real numbers and scenarios |

## Principles

1. **Definition First**: Terms and assumptions before logic
2. **Clear Logic**: Decision paths should be obvious
3. **Example Driven**: Abstract logic paired with concrete examples
4. **Complete Boundaries**: Edge cases in logic branches, not separate
5. **Iterative Mindset**: Admit limitations, leave room for expansion

## Quick Reference

```
Algorithm Spec Template:

## Key Terms Definition
- Term: Definition

## Input
- Input name: Description

## Core Logic
```
Decision tree
```

## Limitations and Future Improvements
- Item: Current / Future
```

## Reference

Complete example: See `references/training-scheduling-algorithm.md` for a full implementation of the algorithm-spec pattern.
