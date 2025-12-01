---

description: "Task list for Math Agent – Function-Calling Add & Subtract Agent with OpenAI SDK and ChatKit UI"
---

# Tasks: Math Agent – Function-Calling Add & Subtract Agent with OpenAI SDK and ChatKit UI

**Input**: Design documents from `/specs/001-add-subtract-agent/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: This task list includes test tasks as part of the implementation for each user story.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure: `src/agent/`, `src/lib/`, `tests/unit/`, `tests/integration/`, `frontend/`
- [X] T002 Initialize Python 3.12 project using 'uv' (automatically creates .venv and .toml files)
- [X] T003 Install dependencies from pyproject.toml: `litellm>=1.80.7`, `openai>=2.8.1`, `openai-agents[litellm]>=0.6.1`, `openai-chatkit>=0.1.0`, `pytest>=9.0.1`, `pytest-asyncio>=1.3.0`, `python-dotenv>=1.2.1`, `fastapi>=0.111.0`, `uvicorn>=0.30.1`, `python-multipart>=0.0.9`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Implement input validation utility `is_numeric` in `src/lib/validation.py`
- [X] T005 Create base structure for `math_functions` module in `src/agent/math_functions.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: OpenAI Agent SDK Integration

**Purpose**: Integrate the math functions with the OpenAI Agent SDK for natural language function calling.

- [X] T005.1 Define `add` function as an OpenAI tool within `src/agent/openai_tools.py`
- [X] T005.2 Define `subtract` function as an OpenAI tool within `src/agent/openai_tools.py`
- [X] T005.3 Modify `src/agent/agent.py` to initialize the OpenAI client, load tools, and process natural language queries.
- [X] T005.4 Update `src/agent/agent.py` to handle tool calls and return results.
- [X] T005.5 Implement error handling for `ValueError` from math functions within `src/agent/agent.py`'s tool calling mechanism.

---

## Phase 4: User Story 1 - Basic Addition (Priority: P1) 🎯 MVP

**Goal**: Enable natural language interaction for the `add` function via the OpenAI Agent SDK.

**Independent Test**: Provide a natural language query for addition and verify the correct function call and result, including flexible response formats.

### Tests for User Story 1
> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T006 [P] [US1] Unit test for `add` function with positive integers in `tests/unit/test_math_functions.py`
- [X] T007 [P] [US1] Unit test for `add` function with negative integers in `tests/unit/test_math_functions.py`
- [X] T008 [P] [US1] Unit test for `add` function with floats in `tests/unit/test_math_functions.py`
- [X] T009 [P] [US1] Integration test for `/add` endpoint with valid inputs in `tests/integration/test_math_api.py`
- [X] T009.1 [US1] Integration test for natural language addition via OpenAI SDK, checking flexible response formats in `tests/integration/test_openai_agent.py`

### Implementation for User Story 1
(Already covered by OpenAI Agent SDK Integration phase and previous `math_functions.py` tasks)

---

## Phase 5: User Story 2 - Basic Subtraction (Priority: P1)

**Goal**: Enable natural language interaction for the `subtract` function via the OpenAI Agent SDK.

**Independent Test**: Provide a natural language query for subtraction and verify the correct function call and result, including flexible response formats.

### Tests for User Story 2
> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T012 [P] [US2] Unit test for `subtract` function with positive integers in `tests/unit/test_math_functions.py`
- [X] T013 [P] [US2] Unit test for `subtract` function with negative integers in `tests/unit/test_math_functions.py`
- [X] T014 [P] [US2] Unit test for `subtract` function with floats in `tests/unit/test_math_functions.py`
- [X] T015 [P] [US2] Integration test for `/subtract` endpoint with valid inputs in `tests/integration/test_math_api.py`
- [X] T015.1 [US2] Integration test for natural language subtraction via OpenAI SDK, checking flexible response formats in `tests/integration/test_openai_agent.py`

### Implementation for User Story 2
(Already covered by OpenAI Agent SDK Integration phase and previous `math_functions.py` tasks)

---

## Phase 6: User Story 3 - Error Handling for Invalid Inputs and Unsupported Operations (Priority: P1)

**Goal**: Ensure robust error handling for invalid inputs and unsupported operations via natural language.

**Independent Test**: Provide non-numeric inputs or request unsupported operations via natural language and check for structured error messages.

### Tests for User Story 3
> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T018 [P] [US3] Unit test for `add` with non-numeric inputs in `tests/unit/test_math_functions.py`
- [X] T019 [P] [US3] Unit test for `subtract` with non-numeric inputs in `tests/unit/test_math_functions.py`
- [X] T020 [P] [US3] Integration test for `/add` endpoint with non-numeric inputs in `tests/integration/test_math_api.py`
- [X] T021 [P] [US3] Integration test for `/subtract` endpoint with non-numeric inputs in `tests/integration/test_math_api.py`
- [X] T021.1 [US3] Integration test for non-numeric inputs via natural language via OpenAI SDK in `tests/integration/test_openai_agent.py`
- [X] T021.2 [US3] Integration test for unsupported operations via natural language via OpenAI SDK in `tests/integration/test_openai_agent.py`

### Implementation for User Story 3
(Already covered by OpenAI Agent SDK Integration phase and previous `math_functions.py` and `validation.py` tasks)

---

## Phase 7: FastAPI Integration

**Goal**: Expose the `chat_with_agent` function via a FastAPI endpoint for external consumption and potentially serve the ChatKit UI.

### Tests for FastAPI Integration
> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T022 [P] [FASTAPI] Integration test for `/chat` endpoint with valid addition query in `tests/integration/test_fastapi_agent.py`
- [ ] T023 [P] [FASTAPI] Integration test for `/chat` endpoint with valid subtraction query in `tests/integration/test_fastapi_agent.py`
- [ ] T024 [P] [FASTAPI] Integration test for `/chat` endpoint with invalid inputs in `tests/integration/test_fastapi_agent.py`

### Implementation for FastAPI Integration


- [ ] T026 [P] [FASTAPI] Create `src/main.py` with a basic FastAPI application instance.
- [ ] T027 [P] [FASTAPI] Define a POST endpoint `/chat` in `src/main.py` that accepts a `query: str` in the request body.
- [ ] T028 [P] [FASTAPI] Call `chat_with_agent(query)` from the `/chat` endpoint in `src/main.py`.
- [ ] T029 [P] [FASTAPI] Return the agent's response as a JSON object from the `/chat` endpoint, compatible with ChatKit.
- [ ] T030 [P] [FASTAPI] Configure `src/main.py` to serve static files from the `frontend/dist` directory (or similar build output).

---

## Phase 8: User Story 4 - ChatKit UI Integration (Priority: P1)

**Goal**: Implement a functional and visually appealing ChatKit UI that interacts with the FastAPI backend.

### Tests for User Story 4
> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T031 [P] [US4] Integration test: ChatKit UI loads correctly and displays initial elements.
- [ ] T032 [P] [US4] Integration test: User input is sent to the backend `/chat` endpoint and appears in chat history.
- [ ] T033 [P] [US4] Integration test: Agent responses are received from the backend and displayed in the ChatKit UI.
- [ ] T034 [P] [US4] Integration test: Successful addition query through ChatKit UI displays correct, flexibly formatted response.
- [ ] T035 [P] [US4] Integration test: Successful subtraction query through ChatKit UI displays correct, flexibly formatted response.
- [ ] T036 [P] [US4] Integration test: Invalid input through ChatKit UI displays structured error message.

### Implementation for User Story 4

- [ ] T037 [P] [US4] Initialize a new React project in the `frontend/` directory (e.g., using `create-react-app` or `Vite`).
- [ ] T038 [P] [US4] Install `openai-chatkit` and its dependencies in the frontend project.
- [ ] T039 [P] [US4] Implement a basic ChatKit component in `frontend/src/App.tsx` (or similar) that connects to the FastAPI `/chat` endpoint.
- [ ] T040 [P] [US4] Configure ChatKit to handle different response formats from the backend.
- [ ] T041 [P] [US4] Build the frontend project to `frontend/dist` (or similar) for static file serving by FastAPI.

---

## Phase 9: Cross-Cutting Concerns & Polish

**Purpose**: Improvements that affect multiple user stories and ensure compliance with NFRs.

- [ ] T042 [P] [NFR] Implement 30-second non-blocking delay for every Gemini API call within `src/agent/` (e.g., in `math_core.py` or where Gemini API is called).
- [X] T043 Code cleanup and refactoring in `src/` and `tests/`.
- [X] T044 Ensure all Success Criteria (SC-001, SC-002, SC-003, SC-004, SC-005, SC-006) from `spec.md` are met.
- [ ] T045 Validate `quickstart.md` against implemented functionality (now including natural language interaction and ChatKit UI).

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion
- **OpenAI Agent SDK Integration (Phase 3)**: Depends on Foundational phase completion. BLOCKS user stories.
- **User Stories (Phase 4, 5, 6, 8)**: All depend on OpenAI Agent SDK Integration phase completion.
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4)
- **FastAPI Integration (Phase 7)**: Depends on OpenAI Agent SDK Integration phase completion. Can be done in parallel with User Stories.
- **Cross-Cutting Concerns & Polish (Phase 9)**: Depends on all desired user stories AND FastAPI Integration being complete, and the 30-second delay for Gemini API calls.

### User Story Dependencies

- **User Story 1 (P1)**: Can start after OpenAI Agent SDK Integration - No dependencies on other stories
- **User Story 2 (P1)**: Can start after OpenAI Agent SDK Integration - No dependencies on other stories
- **User Story 3 (P1)**: Can start after OpenAI Agent SDK Integration - No dependencies on other stories
- **User Story 4 (P1)**: Depends on FastAPI Integration for backend connectivity.

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks (T001-T003.1) can run in parallel (T003.1 depends on T002).
- Foundational tasks (T004-T005) can run in parallel.
- OpenAI Agent SDK Integration tasks (T005.1-T005.5) have some internal dependencies but can be largely parallelized.
- Once OpenAI Agent SDK Integration phase completes, User Stories 1, 2, and 3 can start in parallel by different team members.
- FastAPI Integration (Phase 7) can also be worked on in parallel once OpenAI Agent SDK Integration is complete.
- Tests within each user story marked [P] can run in parallel.

---

## Parallel Example: OpenAI Agent SDK Integration Phase

```bash
# Define tools in parallel
Task: "Define `add` function as an OpenAI tool within src/agent/openai_tools.py"
Task: "Define `subtract` function as an OpenAI tool within src/agent/openai_tools.py"

# Then modify agent.py
Task: "Modify src/agent/agent.py to initialize the OpenAI client, load tools, and process natural language queries."
Task: "Update src/agent/agent.py to handle tool calls and return results."
Task: "Implement error handling for ValueError from math functions within src/agent/agent.py's tool calling mechanism."
```

---

## Implementation Strategy

### MVP First (User Story 1 Only via OpenAI SDK and basic ChatKit UI)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: OpenAI Agent SDK Integration
4. Complete Phase 4: User Story 1 (updated tests/implementation)
5. Complete Phase 7: FastAPI Integration (basic chat endpoint)
6. Complete Phase 8: User Story 4 (basic ChatKit UI with connectivity)
7. Complete T042: Implement 30-second delay for Gemini API calls.
8. **STOP and VALIDATE**: Test User Story 1 and basic ChatKit UI independently (natural language interaction)
9. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Complete OpenAI Agent SDK Integration → SDK ready
3. Complete FastAPI Integration → API ready
4. Complete User Story 4 (basic ChatKit UI) → UI ready
5. Complete T042 (30-second delay) → NFR met
6. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
7. Add User Story 2 → Test independently → Deploy/Demo
8. Add User Story 3 → Test independently → Deploy/Demo
9. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational + OpenAI Agent SDK Integration together
2. Once Integration is done:
   - Developer A: User Story 1 (updated)
   - Developer B: User Story 2 (updated)
   - Developer C: User Story 3 (updated)
   - Developer D: FastAPI Integration (Phase 7)
   - Developer E: User Story 4 (Phase 8) - dependent on Phase 7
3. Implement T042 (30-second delay) once relevant Gemini API calls are identified.
4. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
