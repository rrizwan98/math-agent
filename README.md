# Math Agent

A production-ready math assistant that performs addition and subtraction operations through natural language interaction. Built with OpenAI Agent SDK, FastAPI, and ChatKit UI.

## 🚀 Features

- **Natural Language Processing**: Interact with the agent using conversational queries
- **Function Calling**: Uses OpenAI Agent SDK for intelligent function selection
- **Modern UI**: Beautiful ChatKit interface built with Next.js and React
- **RESTful API**: FastAPI backend with comprehensive error handling
- **Type Safety**: Full TypeScript support for frontend, Python type hints for backend
- **Testing**: Comprehensive unit and integration tests

## 📋 Table of Contents

- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Development](#development)
- [Troubleshooting](#troubleshooting)

## 🏗️ Architecture

The Math Agent follows a modern microservices architecture:

```
┌─────────────────┐
│   ChatKit UI    │  Next.js + React + ChatKit
│  (Frontend)     │  Port: 3000
└────────┬────────┘
         │ HTTP/SSE
         ▼
┌─────────────────┐
│  Next.js API    │  /api/chatkit (Proxy)
│     Route       │
└────────┬────────┘
         │ HTTP
         ▼
┌─────────────────┐
│  FastAPI        │  /chatkit endpoint
│   Backend       │  Port: 8000
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  OpenAI Agent   │  Function calling
│      SDK        │  + Gemini API
└─────────────────┘
```

### Components

- **Frontend**: Next.js application with ChatKit React components
- **API Gateway**: Next.js API route that proxies requests to FastAPI
- **Backend**: FastAPI server with ChatKit integration
- **Agent**: OpenAI Agent SDK with custom math functions
- **LLM**: Gemini 2.0 Flash Lite via LiteLLM

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.12+**
- **Node.js 18+** and **npm**
- **uv** (Python package manager) - [Installation Guide](https://github.com/astral-sh/uv)
- **Gemini API Key** - [Get your API key](https://aistudio.google.com/app/apikey)

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd math-agent
```

### 2. Install Backend Dependencies

```bash
# Install Python dependencies using uv
uv pip install -e .
```

### 3. Install Frontend Dependencies

```bash
cd chatkit-ui
npm install
cd ..
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### Optional Configuration

For the frontend, you can create `chatkit-ui/.env.local` to customize the FastAPI backend URL:

```env
FASTAPI_BASE_URL=http://localhost:8000
```

## 🎯 Usage

### Starting the Application

#### Terminal 1: Start FastAPI Backend

```bash
uvicorn src.main:app --reload --port 8000
```

The backend will be available at `http://localhost:8000`

#### Terminal 2: Start Next.js Frontend

```bash
cd chatkit-ui
npm run dev
```

The frontend will be available at `http://localhost:3000`

### Using the Chat Interface

1. Open `http://localhost:3000` in your browser
2. Click the chat button in the bottom-right corner
3. Type your math queries in natural language

### Example Queries

**Addition:**
- "What is 5 plus 3?"
- "Add 10 to 20"
- "Can you add 1.5 and 2.5?"

**Subtraction:**
- "Subtract 5 from 10"
- "What is 15 minus 7?"
- "Take 2.5 away from 10.5"

**Error Cases:**
- "Add 'hello' and 3" → Returns error message
- "Multiply 2 by 3" → Returns unsupported operation message

## 📁 Project Structure

```
math-agent/
├── src/
│   ├── agent/              # Agent implementation
│   │   ├── agent.py        # Main agent configuration
│   │   ├── math_core.py    # Core math functions
│   │   ├── math_functions.py  # OpenAI tool functions
│   │   └── openai_tools.py    # Tool definitions
│   ├── lib/
│   │   └── validation.py  # Input validation utilities
│   ├── chatkit_store.py    # In-memory ChatKit store
│   └── main.py            # FastAPI application
├── chatkit-ui/            # Next.js frontend
│   ├── app/
│   │   ├── api/
│   │   │   └── chatkit/
│   │   │       └── route.ts    # API proxy route
│   │   ├── page.tsx       # Main page
│   │   └── layout.tsx     # App layout
│   └── components/
│       └── ChatWidget.tsx # ChatKit widget component
├── tests/
│   ├── unit/              # Unit tests
│   └── integration/      # Integration tests
├── specs/                 # Feature specifications
├── pyproject.toml        # Python dependencies
└── README.md             # This file
```

## 📚 API Documentation

### FastAPI Endpoints

#### `POST /chatkit`

Handles ChatKit API requests for thread management and messaging.

**Request Body:**
```json
{
  "type": "threads.create",
  "params": {
    "input": {
      "content": [{"type": "input_text", "text": "What is 5+5?"}],
      "quoted_text": "",
      "attachments": [],
      "inference_options": {}
    }
  }
}
```

**Response:**
- **Streaming**: `text/event-stream` with Server-Sent Events
- **Non-streaming**: `application/json` with thread data

### ChatKit API Types

The backend supports the following ChatKit request types:

- `threads.create` - Create a new conversation thread
- `threads.list` - List all threads
- `threads.addUserMessage` - Add a user message to a thread

## 🧪 Testing

### Run All Tests

```bash
# Run unit tests
pytest tests/unit/

# Run integration tests
pytest tests/integration/

# Run all tests
pytest
```

### Test Coverage

```bash
pytest --cov=src --cov-report=html
```

## 💻 Development

### Code Style

- **Python**: Follow PEP 8 guidelines
- **TypeScript**: ESLint configuration included
- **Formatting**: Use black for Python, Prettier for TypeScript

### Adding New Math Functions

1. Add the function to `src/agent/math_core.py`
2. Create OpenAI tool wrapper in `src/agent/math_functions.py`
3. Register the tool in `src/agent/agent.py`
4. Add tests in `tests/unit/test_math_functions.py`

### Project Dependencies

**Backend:**
- `fastapi` - Web framework
- `openai-agents` - Agent SDK
- `openai-chatkit` - ChatKit server
- `litellm` - LLM abstraction layer
- `pytest` - Testing framework

**Frontend:**
- `next` - React framework
- `@openai/chatkit-react` - ChatKit React components
- `tailwindcss` - Styling

## 🔍 Troubleshooting

### Common Issues

#### 1. ModuleNotFoundError: No module named 'chatkit'

**Solution:**
```bash
uv pip install -e .
```

#### 2. 404 Error on /chatkit endpoint

**Solution:** Ensure the FastAPI server is running on port 8000 and the Next.js API route is correctly configured.

#### 3. CORS Errors

**Solution:** The FastAPI backend has CORS middleware configured. If issues persist, check that both servers are running.

#### 4. ChatKit Widget Not Appearing

**Solution:**
- Verify both servers are running
- Check browser console for errors
- Ensure `ChatWidget` is imported in `app/page.tsx`

### Debug Mode

Enable debug logging:

```bash
# Backend
uvicorn src.main:app --reload --log-level debug

# Frontend
cd chatkit-ui
npm run dev -- --debug
```

## 📖 Additional Documentation

- [ChatKit Setup Guide](./chatkit-ui/CHATKIT_SETUP.md) - Detailed ChatKit integration guide
- [Feature Specification](./specs/001-add-subtract-agent/spec.md) - Complete feature specification
- [API Contract](./specs/001-add-subtract-agent/contracts/openapi.yaml) - OpenAPI specification

## 🤝 Contributing

1. Create a feature branch from `main`
2. Make your changes
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📝 License

[Add your license here]

## 🙏 Acknowledgments

- OpenAI for the Agent SDK and ChatKit
- FastAPI for the excellent web framework
- Next.js team for the React framework

---

**Built with ❤️ using OpenAI Agent SDK, FastAPI, and ChatKit**

