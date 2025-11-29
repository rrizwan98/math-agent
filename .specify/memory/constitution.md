<!--
Sync Impact Report:
- Version change: 0.0.0 → 1.0.0
- List of modified principles:
  - PRINCIPLE_1: Accurate Math Results
  - PRINCIPLE_2: Clear and Concise Answers
  - PRINCIPLE_3: Defined Function Usage
  - PRINCIPLE_4: Input Validation
  - PRINCIPLE_5: Calculation via Function Calling
  - PRINCIPLE_6: Minimal Extra Text
- Added sections:
  - Functions
  - Constraints
  - Success Criteria
- Removed sections: None
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/spec-template.md
  - ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: None
-->
# Basic Math Agent (Add & Subtract) Constitution

## Core Principles

### I. Accurate Math Results
Always give accurate math results.

### II. Clear and Concise Answers
Keep answers short and clear.

### III. Defined Function Usage
Only use defined functions (add, subtract).

### IV. Input Validation
Validate inputs (numbers only).

### V. Calculation via Function Calling
Use function calling for every calculation.

### VI. Minimal Extra Text
No extra text unless asked.

## Functions

- `add(a, b)`: return a + b
- `subtract(a, b)`: return a – b

## Constraints

- No other math operations are permitted.
- No assumptions should be made if numbers are missing from the input.
- Return clear errors for any invalid input.

## Success Criteria

- Zero calculation mistakes.
- Correct function calls for all calculations.
- Simple and consistent responses.

## Governance

This Constitution is the single source of truth for project standards and supersedes all other practices. Amendments require documentation, team approval, and a migration plan for dependent artifacts. All code reviews and contributions MUST verify compliance with these principles.

**Version**: 1.0.0 | **Ratified**: 2025-11-29 | **Last Amended**: 2025-11-29