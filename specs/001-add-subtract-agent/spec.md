# Feature Specification: Math Agent – Function-Calling Add & Subtract Agent with OpenAI SDK and ChatKit UI

**Feature Branch**: `001-add-subtract-agent`
**Created**: 2025-11-29
**Status**: Draft (Updated)
**Input**: User description: "**Project:** Math Agent – Function-Calling Add & Subtract Agent with ChatKit UI **Target Audience:** * Users needing accurate, reliable basic arithmetic answers through an intuitive chat interface * Developers integrating a simple function-calling math agent through natural language interaction * Developers building UIs with OpenAI ChatKit **Focus:** * Correct computation using `add` and `subtract` functions via OpenAI Agent SDK function calling * Clear and concise output * Robust error handling for invalid inputs and unsupported operations * Seamless user experience via OpenAI ChatKit UI * Proper integration of OpenAI Agent SDK with ChatKit UI * Consistent response time with mandatory Gemini API call delays. **Success Criteria:** * Correctly resolves all natural language addition and subtraction queries * Uses only the defined functions (`add`, `subtract`) via the OpenAI Agent SDK * Returns numeric results consistently, allowing for flexible natural language phrasing * Provides structured error messages for invalid inputs and when other operations are requested * Presents a functional and intuitive chat UI using ChatKit **Constraints:** * Only addition and subtraction allowed * Inputs must be numbers (integers or floats) * No assumptions beyond provided numbers * Responses must be concise and direct, but allow for flexible phrasing around the numeric answer * Interaction primarily through natural language parsed by OpenAI Agent SDK and displayed via ChatKit UI * Mandatory 30-second sleep for every Gemini API call. **Not Building:** * Multiplication, division, or advanced math * Direct programmatic API calls (instead, use natural language through SDK) * Interpretations or guesses * Explanations beyond requested outputs"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Basic Addition (Priority: P1)

As a user, I want to add two numbers using natural language via the ChatKit UI and get the correct sum, even if the response format varies.

**Why this priority**: This is the most fundamental function of the agent, now with natural language interaction and a user-friendly UI.

**Independent Test**: Can be tested by providing a natural language query through the ChatKit UI and checking if the returned sum is correct via function calling, allowing for flexible phrasing around the numeric answer.

**Acceptance Scenarios**:

1. **Given** the user says "add 2 and 3" via the ChatKit UI, **When** the agent processes the request using the OpenAI Agent SDK, **Then** the agent should call the `add` function with `2` and `3` and return `5` (e.g., "The answer is 5", "5", "Result: 5").
2. **Given** the user says "what is -10 plus 5" via the ChatKit UI, **When** the agent processes the request using the OpenAI Agent SDK, **Then** the agent should call the `add` function with `-10` and `5` and return `-5` (e.g., "Your sum is -5", "-5", "Minus five").
3. **Given** the user says "add 1.5 to 2.5" via the ChatKit UI, **When** the agent processes the request using the OpenAI Agent SDK, **Then** the agent should call the `add` function with `1.5` and `2.5` and return `4.0` (e.g., "Four point zero", "Ans: 4.0", "4.0").

---

### User Story 2 - Basic Subtraction (Priority: P1)

As a user, I want to subtract one number from another using natural language via the ChatKit UI and get the correct difference, even if the response format varies.

**Why this priority**: This is the other core function of the agent, now with natural language interaction and a user-friendly UI.

**Independent Test**: Can be tested by providing a natural language query through the ChatKit UI and checking if the returned difference is correct via function calling, allowing for flexible phrasing around the numeric answer.

**Acceptance Scenarios**:

1. **Given** the user says "subtract 3 from 5" via the ChatKit UI, **When** the agent processes the request using the OpenAI Agent SDK, **Then** the agent should call the `subtract` function with `5` and `3` and return `2` (e.g., "The difference is 2", "2", "Two").
2. **Given** the user says "what is 3 minus 5" via the ChatKit UI, **When** the agent processes the request using the OpenAI Agent SDK, **Then** the agent should call the `subtract` function with `3` and `5` and return `-2` (e.g., "The answer is -2", "-2", "Negative two").
3. **Given** the user says "take 2.5 away from 10.5" via the ChatKit UI, **When** the agent processes the request using the OpenAI Agent SDK, **Then** the agent should call the `subtract` function with `10.5` and `2.5` and return `8.0` (e.g., "Your result is 8.0", "8.0", "Eight point zero").

---

### User Story 3 - Error Handling for Invalid Inputs (Priority: P1)

As a user, I want to receive a clear error message via the ChatKit UI if I provide invalid inputs or request unsupported operations via natural language.

**Why this priority**: Robustness and user experience depend on good error handling, especially with natural language.

**Independent Test**: Can be tested by providing non-numeric inputs or requesting unsupported operations through the ChatKit UI and checking for a structured error message.

**Acceptance Scenarios**:

1. **Given** the user says "add 'hello' and 3" via the ChatKit UI, **When** the agent processes the request using the OpenAI Agent SDK, **Then** the agent should return a structured error message indicating that inputs must be numbers.
2. **Given** the user says "subtract 5 from 'world'" via the ChatKit UI, **When** the agent processes the request using the OpenAI Agent SDK, **Then** the agent should return a structured error message indicating that inputs must be numbers.
3. **Given** the user says "multiply 2 by 3" via the ChatKit UI, **When** the agent processes the request using the OpenAI Agent SDK, **Then** the agent should return a structured error message indicating that multiplication is not supported.

---

### User Story 4 - ChatKit UI Interaction (Priority: P1)

As a user, I want to interact with the Math Agent through a functional and visually appealing ChatKit user interface.

**Why this priority**: This introduces the core UI component for the agent, improving user accessibility and experience.

**Independent Test**: Can be tested by visually confirming the ChatKit UI loads correctly, allows input, displays responses, and handles basic chat interactions.

**Acceptance Scenarios**:

1. **Given** the ChatKit UI is loaded in a web browser, **When** the user types a message and sends it, **Then** the message should appear in the chat history.
2. **Given** the ChatKit UI is loaded, **When** the agent responds, **Then** the agent's response should appear in the chat history.
3. **Given** the ChatKit UI is loaded and the agent is functional, **When** the user enters a valid math query, **Then** the ChatKit UI should display the agent's correct response.

---

### Edge Cases

- What happens when very large numbers are provided via natural language through the ChatKit UI?
- What happens when the user tries to call a function other than `add` or `subtract` via natural language through the ChatKit UI?
- What happens when the user provides no input or an ambiguous query through the ChatKit UI?
- What happens if the backend API is unavailable?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The agent MUST provide a function `add(a: number, b: number)` that returns the sum of `a` and `b`, callable via the OpenAI Agent SDK.
- **FR-002**: The agent MUST provide a function `subtract(a: number, b: number)` that returns the difference of `a` and `b`, callable via the OpenAI Agent SDK.
- **FR-003**: The agent MUST only accept numbers (integers or floats) as input to the `add` and `subtract` functions, validated before function execution.
- **FR-004**: The agent MUST return a structured error message if any input is not a number, as detected by the OpenAI Agent SDK or internal validation.
- **FR-005**: The agent MUST NOT perform any other mathematical operations besides addition and subtraction, and MUST return a structured error if such an operation is requested via natural language.
- **FR-006**: The agent MUST use the OpenAI Agent SDK for processing natural language queries, invoking the `add` and `subtract` functions, and managing chat sessions.
- **FR-007**: A FastAPI endpoint MUST be created to receive natural language queries from the ChatKit UI, pass them to the `chat_with_agent()` function (or equivalent Agent SDK method), and return the agent's response as a JSON object, compatible with ChatKit's expected input/output format.
- **FR-008**: The UI MUST be implemented using the OpenAI ChatKit SDK, providing a responsive and interactive chat experience.
- **FR-009**: The ChatKit UI MUST connect to the FastAPI backend to send user messages and receive agent responses.

### Non-Functional Requirements

- **NFR-001**: Every call to the Gemini API MUST include a 30-second delay. This delay should be implemented in a non-blocking manner if possible (e.g., using `asyncio.sleep` in an async context).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: The agent correctly resolves 100% of natural language addition and subtraction queries with valid numeric inputs via the OpenAI Agent SDK and displays results in the ChatKit UI.
- **SC-002**: The agent returns a numeric result for all successful computations, with the response text allowing for flexible phrasing around the numeric answer.
- **SC-003**: The agent returns a structured error message for 100% of requests with invalid inputs or unsupported operations, displayed in the ChatKit UI.
- **SC-004**: The agent's response time for any valid natural language request, including the mandatory 30-second Gemini API delay, is within acceptable limits for a chat application (e.g., display response within 35 seconds for a single API call).
- **SC-005**: The agent successfully integrates and utilizes the OpenAI Agent SDK for all function calling interactions and chat session management.
- **SC-006**: The ChatKit UI successfully loads, allows user input, displays agent responses, and maintains chat history.