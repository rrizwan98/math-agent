'use client';

import { useState } from 'react';
import { ChatKit, useChatKit } from '@openai/chatkit-react';
import type { ChatKitOptions } from '@openai/chatkit-react';

// Pure ChatKit configuration - no custom UI code
const chatKitOptions: ChatKitOptions = {
  api: {
    url: '/api/chatkit',
    domainKey: 'dev', // Required but not verified on localhost
    // TODO: configure your ChatKit API integration (URL, auth, uploads).
  },
  theme: {
    colorScheme: 'dark',
    radius: 'pill',
    density: 'normal',
    color: {
      grayscale: {
        hue: 0,
        tint: 0,
        shade: -1
      },
      accent: {
        primary: '#dfd7d7',
        level: 1
      },
      surface: {
        background: '#212121',
        foreground: '#0d0d0d'
      }
    },
    typography: {
      baseSize: 16,
      fontFamily: '"OpenAI Sans", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", sans-serif',
      fontFamilyMono: 'ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "DejaVu Sans Mono", "Courier New", monospace',
      fontSources: [
        {
          family: 'OpenAI Sans',
          src: 'https://cdn.openai.com/common/fonts/openai-sans/v2/OpenAISans-Regular.woff2',
          weight: 400,
          style: 'normal',
          display: 'swap'
        }
        // ...and 7 more font sources
      ]
    }
  },
  composer: {
    placeholder: 'Message the mathagent',
    attachments: {
      enabled: false
    },
  },
  startScreen: {
    greeting: '',
    prompts: [],
  },
  // Optional fields not shown: locale, initialThread, threadItemActions, header, onClientTool, entities, widgets
};

export default function ChatWidget() {
  const [isOpen, setIsOpen] = useState(false);
  // Pure ChatKit hook - no custom state management needed
  const chatKit = useChatKit(chatKitOptions);

  return (
    <>
      {/* Toggle Button - Always visible */}
      {!isOpen && (
        <button
          onClick={() => setIsOpen(true)}
          className="fixed bottom-4 right-4 z-50 bg-blue-600 hover:bg-blue-700 text-white rounded-full p-4 shadow-lg transition-colors"
          aria-label="Open chat"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"
            />
          </svg>
        </button>
      )}

      {/* ChatKit Widget - Only visible when isOpen is true */}
      {isOpen && (
        <div className="fixed bottom-4 right-4 z-50 w-96 h-[600px] rounded-2xl overflow-hidden shadow-2xl">
          {/* Close button */}
          <button
            onClick={() => setIsOpen(false)}
            className="absolute top-2 right-2 z-10 bg-gray-800 hover:bg-gray-700 text-white rounded-full p-2 transition-colors"
            aria-label="Close chat"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-5 w-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
          
          {/* Pure ChatKit - no custom header or toggle buttons */}
          <ChatKit
            control={chatKit.control}
            style={{
              height: '100%',
              width: '100%',
              border: 'none',
              borderRadius: '16px',
            }}
          />
        </div>
      )}
    </>
  );
}
