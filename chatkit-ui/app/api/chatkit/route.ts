import { NextRequest, NextResponse } from 'next/server';

// FastAPI backend URL - adjust this if your backend runs on a different port
const FASTAPI_BASE_URL = process.env.FASTAPI_BASE_URL || 'http://localhost:8000';

// CORS headers for ChatKit iframe requests
const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, Authorization, X-Requested-With',
};

// Handle OPTIONS preflight requests
export async function OPTIONS() {
  return new NextResponse(null, {
    status: 200,
    headers: corsHeaders,
  });
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.text();
    
    console.log('ChatKit API Request received:', body.substring(0, 200));
    
    // Forward the request to FastAPI backend
    const response = await fetch(`${FASTAPI_BASE_URL}/chatkit`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: body,
    });

    console.log('FastAPI Response status:', response.status);
    console.log('FastAPI Response content-type:', response.headers.get('content-type'));

    // If it's a streaming response, forward it as-is with CORS headers
    if (response.headers.get('content-type')?.includes('text/event-stream')) {
      return new Response(response.body, {
        headers: {
          'Content-Type': 'text/event-stream',
          'Cache-Control': 'no-cache',
          'Connection': 'keep-alive',
          ...corsHeaders,
        },
      });
    }

    // Otherwise, return the JSON response with CORS headers
    const data = await response.text();
    console.log('FastAPI Response data:', data.substring(0, 200));
    
    return new NextResponse(data, {
      status: response.status,
      headers: {
        'Content-Type': 'application/json',
        ...corsHeaders,
      },
    });
  } catch (error) {
    console.error('Error proxying to FastAPI:', error);
    return NextResponse.json(
      { error: 'Failed to connect to chat backend', details: String(error) },
      { 
        status: 500,
        headers: corsHeaders,
      }
    );
  }
}
