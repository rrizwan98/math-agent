---

description: "Task list for Math Agent – Function-Calling Add & Subtract Agent"
---

# Tasks: Math Agent – Function-Calling Add & Subtract Agent

**Input**: Design documents from `/specs/001-add-subtract-agent/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: This task list includes test tasks as part of the implementation for each user story.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure: `src/agent/`, `src/lib/`, `tests/unit/`, `tests/integration/`
- [ ] T002 Initialize Python 3.12 project using 'uv' (automatically creates .venv and .toml files)
- [ ] T003 Install `pytest` for testing (add to `pyproject.toml` or `requirements.txt`)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T004 Implement input validation utility `is_numeric` in `src/lib/validation.py`
- [ ] T005 Create base structure for `math_functions` module in `src/agent/math_functions.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Basic Addition (Priority: P1) 🎯 MVP

**Goal**: Implement the `add` function to correctly sum two numbers, and integrate it.

**Independent Test**: Provide two numbers to the `add` function and verify the correct sum, both via unit and integration tests.

### Tests for User Story 1
> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T006 [P] [US1] Unit test for `add` function with positive integers in `tests/unit/test_math_functions.py`
- [ ] T007 [P] [US1] Unit test for `add` function with negative integers in `tests/unit/test_math_functions.py`
- [ ] T008 [P] [US1] Unit test for `add` function with floats in `tests/unit/test_math_functions.py`
- [ ] T009 [P] [US1] Integration test for `/add` endpoint with valid inputs in `tests/integration/test_math_api.py`

### Implementation for User Story 1

- [ ] T010 [US1] Implement `add` function in `src/agent/math_functions.py`
- [ ] T011 [US1] Integrate `add` function into the agent's callable interface (e.g., `src/agent/agent.py` or main entry point)

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Basic Subtraction (Priority: P1)

**Goal**: Implement the `subtract` function to correctly find the difference between two numbers, and integrate it.

**Independent Test**: Provide two numbers to the `subtract` function and verify the correct difference, both via unit and integration tests.

### Tests for User Story 2
> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T012 [P] [US2] Unit test for `subtract` function with positive integers in `tests/unit/test_math_functions.py`
- [ ] T013 [P] [US2] Unit test for `subtract` function with negative integers in `tests/unit/test_math_functions.py`
- [ ] T014 [P] [US2] Unit test for `subtract` function with floats in `tests/unit/test_math_functions.py`
- [ ] T015 [P] [US2] Integration test for `/subtract` endpoint with valid inputs in `tests/integration/test_math_api.py`

### Implementation for User Story 2

- [ ] T016 [US2] Implement `subtract` function in `src/agent/math_functions.py`
- [ ] T017 [US2] Integrate `subtract` function into the agent's callable interface (e.g., `src/agent/agent.py` or main entry point)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Error Handling for Invalid Inputs (Priority: P1)

**Goal**: Ensure the agent returns clear, structured error messages for invalid inputs.

**Independent Test**: Provide non-numeric inputs to `add` and `subtract` functions and check for structured error messages, both via unit and integration tests.

### Tests for User Story 3
> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T018 [P] [US3] Unit test for `add` with non-numeric inputs in `tests/unit/test_math_functions.py`
- [ ] T019 [P] [US3] Unit test for `subtract` with non-numeric inputs in `tests/unit/test_math_functions.py`
- [ ] T020 [P] [US3] Integration test for `/add` with non-numeric inputs in `tests/integration/test_math_api.py`
- [ ] T021 [P] [US3] Integration test for `/subtract` with non-numeric inputs in `tests/integration/test_math_api.py`

### Implementation for User Story 3

- [ ] T022 [US3] Refine input validation in `src/lib/validation.py` to return structured errors (if not already handled by T004).
- [ ] T023 [US3] Ensure agent's callable interface (`src/agent/agent.py` or main entry point) correctly handles and returns validation errors.

**Checkpoint**: All user stories should now be independently functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T024 Code cleanup and refactoring in `src/` and `tests/`.
- [ ] T025 Ensure all Success Criteria (SC-001, SC-002, SC-003, SC-004) from `spec.md` are met.
- [ ] T026 Validate `quickstart.md` against implemented functionality.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks (T001-T003) can run in parallel.
- Foundational tasks (T004-T005) can run in parallel.
- Once Foundational phase completes, all user stories (US1, US2, US3) can start in parallel by different team members.
- Tests within each user story marked [P] can run in parallel.

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Unit test for add function with positive integers in tests/unit/test_math_functions.py"
Task: "Unit test for add function with negative integers in tests/unit/test_math_functions.py"
Task: "Unit test for add function with floats in tests/unit/test_math_functions.py"
Task: "Integration test for /add endpoint with valid inputs in tests/integration/test_math_api.py"

# Implementation tasks will proceed sequentially after tests are written.
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
