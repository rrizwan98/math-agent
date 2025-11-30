# Implementation Plan: Math Agent – Function-Calling Add & Subtract Agent with OpenAI SDK and ChatKit UI

**Branch**: `001-add-subtract-agent` | **Date**: 2025-11-29 | **Spec**: [./spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-add-subtract-agent/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan outlines the implementation for a Math Agent capable of performing basic addition and subtraction operations through natural language function calling, leveraging the OpenAI Agent SDK. It will feature a user-friendly interface built with the OpenAI ChatKit SDK, interacting with a FastAPI backend. The agent will prioritize accuracy, clear and concise responses with flexible phrasing, robust input validation, and strict adherence to defined `add` and `subtract` functions, with all interactions mediated by the OpenAI Agent SDK. A mandatory 30-second delay for every Gemini API call will be incorporated. The core technical approach involves defining math functions as tools for the SDK, which will then interpret natural language queries, invoke these tools, and handle numerical inputs, providing structured error messages for invalid data or unsupported operations.

## Technical Context

**Language/Version**: Python 3.12 (Backend), JavaScript/TypeScript (Frontend for ChatKit)
**Primary Dependencies**: OpenAI Agent SDK, OpenAI ChatKit SDK, `pytest`, `FastAPI`, `uvicorn`, `React` (for ChatKit frontend)
**Storage**: N/A
**Testing**: `pytest` (for backend), potentially `Jest`/`React Testing Library` (for frontend, if scope allows)
**Target Platform**: Linux server (containerized deployment expected) for backend; Web browser for frontend.
**Project Type**: Hybrid (LLM-driven Agent backend with Web UI)
**Performance Goals**: Response time for any valid natural language request, including the mandatory 30-second Gemini API delay, should be within acceptable limits for a chat application (e.g., display response within 35 seconds for a single API call, as per SC-004 in spec.md).
**Constraints**: Only addition and subtraction allowed; Inputs must be numbers (integers or floats); Clear error messages for invalid inputs/unsupported operations (from FR-003, FR-004, FR-005, Constitution). Interaction primarily through natural language parsed by OpenAI Agent SDK and displayed via ChatKit UI. Mandatory 30-second sleep for every Gemini API call.
**Scale/Scope**: Low to Medium volume (initial assumption, NEEDS CLARIFICATION if higher scale is expected, e.g., concurrent requests)

### FastAPI Service

A FastAPI application (`src/main.py`) will be created to expose the `chat_with_agent()` function (or equivalent OpenAI Agent SDK method) via an HTTP endpoint. This will allow the ChatKit UI to interact with the math agent by sending natural language queries and receiving JSON responses. The service will:
- Accept POST requests to a `/chat` endpoint.
- Extract the natural language query from the request body.
- Pass the query to the OpenAI Agent SDK for processing.
- Incorporate a 30-second non-blocking delay for every Gemini API call within the agent's logic.
- Return the agent's response as a JSON object, compatible with ChatKit's expected input/output format, allowing for flexible phrasing around the numeric answer.
- Potentially serve static files for the React-based ChatKit frontend.

### Frontend (OpenAI ChatKit UI)

A React application will be developed to host the OpenAI ChatKit UI components. This application will:
- Provide a responsive and interactive chat interface for users.
- Connect to the FastAPI backend's `/chat` endpoint to send user messages.
- Display agent responses in the chat history.
- Ensure proper rendering of various response formats (flexible phrasing for math results, structured error messages).

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **PRINCIPLE_1: Accurate Math Results**: **PASS**. Covered by SC-001 in `spec.md` (100% resolution of queries) and `constitution.md` Core Principles.
- **PRINCIPLE_2: Clear and Concise Answers**: **PASS**. Covered by "Clear and concise output" in `spec.md` input, "Responses must be concise and direct" in `spec.md` constraints, and "Simple and consistent responses" in `constitution.md` success criteria. Now also includes flexible phrasing around numeric answers.
- **PRINCIPLE_3: Defined Function Usage**: **PASS**. Covered by FR-005 in `spec.md` ("MUST NOT perform any other mathematical operations") and `constitution.md` Core Principles.
- **PRINCIPLE_4: Input Validation**: **PASS**. Covered by FR-003/FR-004 in `spec.md` ("MUST only accept numbers", "MUST return a structured error message") and `constitution.md` Core Principles.
- **PRINCIPLE_5: Calculation via Function Calling**: **PASS**. Explicitly stated in the feature name "Function-Calling Add & Subtract Agent" and `constitution.md` Core Principles. This will now be mediated by the OpenAI Agent SDK.
- **PRINCIPLE_6: Minimal Extra Text**: **PASS**. Covered by "Minimal Extra Text" in `constitution.md` and "Responses must be concise and direct" in `spec.md` constraints.

## Project Structure

### Documentation (this feature)

```text
specs/001-add-subtract-agent/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── agent/                # Contains the core agent logic, function definitions, and OpenAI Agent SDK integration
├── main.py               # FastAPI application entry point, serves API and potentially static frontend files
└── lib/                  # Utility functions if any

frontend/                 # New directory for the ChatKit UI React application
├── public/               # Public assets
├── src/                  # React source files
│   ├── components/       # React components for ChatKit integration
│   └── App.tsx           # Main React application component
└── package.json          # Frontend dependencies

tests/
├── unit/                 # Unit tests for agent functions and validation
└── integration/          # Integration tests for the agent's overall behavior, including OpenAI SDK interaction and ChatKit UI interactions
```

**Structure Decision**: The "Hybrid" structure is chosen to accommodate both the Python backend and the JavaScript/TypeScript frontend. `src/agent` will house the core logic for function calling and processing, with extensions for OpenAI Agent SDK integration. `src/lib` will be for general utilities. A new `frontend/` directory will contain the React application for the ChatKit UI. `tests/unit` and `tests/integration` will cover the testing requirements, with integration tests expanding to cover the natural language interaction via the SDK and ChatKit UI.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | N/A | N/A |