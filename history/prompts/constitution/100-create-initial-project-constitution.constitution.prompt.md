---
id: 100
title: Create Initial Project Constitution
stage: constitution
date: 2025-11-29
surface: agent
model: gemini-cli
feature: none
branch: main
user: unspecified
command: /sp.constitution
labels: [constitution, setup]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - none
---

## Prompt

/sp.constitution Project: Basic Math Agent (Add & Subtract)

Core Principles:

Always give accurate math results

Keep answers short and clear

Only use defined functions (add, subtract)

Standards:

Validate inputs (numbers only)

Use function calling for every calculation

No extra text unless asked

Functions:

add(a, b): return a + b

subtract(a, b): return a – b

Constraints:

No other math operations

No assumptions if numbers missing

Return clear errors for invalid input

Success Criteria:

Zero calculation mistakes

Correct function calls

Simple, consistent responses

## Response snapshot

Constitution updated to v1.0.0 and written to `.specify/memory/constitution.md`.

## Outcome

- ✅ Impact: Created the initial project constitution, defining core principles and standards.
- 🧪 Tests: No tests were run.
- 📁 Files: 1 file modified: `.specify/memory/constitution.md`.
- 🔁 Next prompts: The user can now proceed with other commands like `/sp.specify` or `/sp.plan`.
- 🧠 Reflection: The `create-phr.sh` script failed silently, requiring a manual fallback. The directory for the PHR did not exist and had to be created.

## Evaluation notes (flywheel)

- Failure modes observed: Script failure, missing directory.
- Graders run and results (PASS/FAIL): n/a
- Prompt variant (if applicable): n/a
- Next experiment (smallest change to try): n/a
