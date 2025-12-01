# ChatKit Integration Setup

This guide explains how to set up and run the ChatKit widget with your FastAPI backend.

## Architecture

- **Frontend (Next.js)**: Math website with ChatKit widget in bottom-right corner
- **Next.js API Route**: `/api/chatkit` - Proxies requests to FastAPI backend
- **Backend (FastAPI)**: `/chatkit` endpoint - Handles ChatKit requests via OpenAI Agents SDK

## Setup Instructions

### 1. Start the FastAPI Backend

First, make sure your FastAPI backend is running. From the project root:

```bash
# Install Python dependencies (if not already done)
uv sync

# Start the FastAPI server (usually runs on port 8000)
# This project defines the FastAPI app in `src/main.py` as `app`
uvicorn src.main:app --reload --port 8000
```

### 2. Configure Backend URL (Optional)

If your FastAPI backend runs on a different port or URL, update the environment variable:

Create or update `chatkit-ui/.env.local`:

```env
FASTAPI_BASE_URL=http://localhost:8000
```

If not set, it defaults to `http://localhost:8000`.

### 3. Start the Next.js Frontend

From the `chatkit-ui` directory:

```bash
cd chatkit-ui
npm install  # If not already done
npm run dev
```

The website will be available at `http://localhost:3000`

### 4. Test the Integration

1. Open `http://localhost:3000` in your browser
2. You should see the Math Explorer website
3. Click the chat button in the bottom-right corner
4. The ChatKit widget should open and connect to your FastAPI backend
5. Try sending a message to test the connection

## How It Works

1. **User sends message** → ChatKit widget sends request to `/api/chatkit`
2. **Next.js API route** → Proxies request to FastAPI backend at `http://localhost:8000/chatkit`
3. **FastAPI backend** → Processes via ChatKit server and Agents SDK
4. **Response streams back** → Through Next.js API route to ChatKit widget

## Troubleshooting

### Chat widget not appearing
- Make sure both servers are running
- Check browser console for errors
- Verify the ChatWidget component is imported in `app/page.tsx`

### Connection errors
- Verify FastAPI backend is running on port 8000 (or update `FASTAPI_BASE_URL`)
- Check CORS settings in FastAPI (should allow `http://localhost:3000`)
- Check browser network tab for failed requests

### CORS issues
- The FastAPI backend has CORS middleware configured to allow all origins in development
- For production, update `allow_origins` in `src/main.py`

## Files Modified/Created

- `chatkit-ui/components/ChatWidget.tsx` - Chat widget component
- `chatkit-ui/app/api/chatkit/route.ts` - Next.js API proxy route
- `chatkit-ui/app/page.tsx` - Added ChatWidget to the page

## References

- [ChatKit Documentation](https://platform.openai.com/docs/guides/chatkit)
- [Custom ChatKit Guide](https://platform.openai.com/docs/guides/custom-chatkit)
- [ChatKit Starter App](https://github.com/openai/openai-chatkit-starter-app)

