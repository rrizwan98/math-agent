# Quickstart Guide: Math Agent with OpenAI SDK and ChatKit UI

This guide provides a quick overview of how to set up and interact with the Math Agent. The agent now features a web-based chat interface built with OpenAI ChatKit, communicating with a FastAPI backend that leverages the OpenAI Agent SDK for basic addition and subtraction operations using natural language.

## 1. Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.12** or higher
*   **uv** (for Python package management)
*   **Node.js** and **npm** (or Yarn) for the frontend development

## 2. Setup Environment Variables

The agent uses the Gemini API. You need to set your `GEMINI_API_KEY` as an environment variable. Create a `.env` file in the root of your project directory with the following content:

```
GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

Replace `"YOUR_GEMINI_API_KEY"` with your actual Gemini API key.

## 3. Install Backend Dependencies

Navigate to the root directory of your project and install the Python dependencies:

```bash
uv pip install -e .
```

## 4. Start the FastAPI Backend

From the root directory of your project, run the FastAPI application:

```bash
uvicorn src.main:app --reload
```

The backend API will be running on `http://127.0.0.1:8000`. This server will serve both the `/chat` API endpoint and the static files for the frontend application.

## 5. Install Frontend Dependencies and Build

First, navigate into the `frontend` directory:

```bash
cd frontend
```

Then, install the Node.js dependencies:

```bash
npm install
```

Now, build the frontend project. This will create the `dist` directory which the FastAPI backend will serve:

```bash
npm run build
```

## 6. Interact with the Agent via ChatKit UI

Once the backend is running and the frontend is built, open your web browser and navigate to:

```
http://127.0.0.1:8000/app
```

You should see the ChatKit UI.

### Key Interaction Points:

*   **Natural Language Queries**: Type your math questions directly into the chat input.
*   **Flexible Responses**: The agent is designed to provide answers in various natural language formats (e.g., "The answer is 4", "4", "Your sum is 4").
*   **30-Second Delay**: Expect a ~30-second delay for each agent response, as per the system's requirement for Gemini API calls.

### Examples:

1.  **Addition**: Type "What is 5 plus 3?" or "Add 10 to 20".
2.  **Subtraction**: Type "Subtract 5 from 10" or "What is 15 minus 7?".
3.  **Decimal Numbers**: Type "Add 1.5 to 2.5" or "Take 2.5 away from 10.5".
4.  **Error Handling (Invalid Input)**: Type "Can you add 'hello' and 3?".
5.  **Error Handling (Unsupported Operation)**: Type "What is 2 multiplied by 3?".

Observe the agent's responses in the chat history. For math operations, verify that the numerical result is correct, regardless of the phrasing. For invalid inputs or unsupported operations, ensure a clear error message is displayed.