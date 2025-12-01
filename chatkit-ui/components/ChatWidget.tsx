'use client';

import { useState } from 'react';
import { ChatKit, useChatKit } from '@openai/chatkit-react';

export default function ChatWidget() {
  const [isOpen, setIsOpen] = useState(false);

  // ChatKit hook with custom backend API configuration
  // For localhost, domain verification is skipped (as shown in console)
  // Both 'url' and 'domainKey' are required by CustomApiConfig
  const chatKit = useChatKit({
    api: {
      url: '/api/chatkit',
      domainKey: 'dev', // Required but not verified on localhost
    },
    // Configure the start screen with math-related prompts
    startScreen: {
      greeting: 'Hello! I\'m your Math Assistant. How can I help you today?',
      prompts: [
        {
          label: 'Solve an equation',
          prompt: 'Can you help me solve this equation?',
          icon: 'write',
        },
        {
          label: 'Explain a concept',
          prompt: 'Can you explain a math concept to me?',
          icon: 'lightbulb',
        },
      ],
    },
  });

  return (
    <div className="fixed bottom-4 right-4 z-50">
      {!isOpen && (
        <button
          onClick={() => setIsOpen(true)}
          className="bg-blue-600 text-white rounded-full p-4 shadow-lg hover:bg-blue-700 transition-colors"
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

      {isOpen && (
        <div className="fixed bottom-4 right-4 w-96 h-[600px] bg-white dark:bg-gray-900 rounded-lg shadow-xl overflow-hidden flex flex-col border border-gray-200 dark:border-gray-700">
          {/* Header with close button */}
          <div className="flex justify-between items-center p-4 border-b border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800">
            <h3 className="font-semibold text-gray-900 dark:text-white">Math Assistant</h3>
            <button
              onClick={() => setIsOpen(false)}
              className="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200"
              aria-label="Close chat"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>

          {/* ChatKit Container - Critical: Must have height */}
          <div className="flex-1 relative min-h-0">
            <ChatKit
              control={chatKit.control}
              style={{
                height: '100%',
                width: '100%',
                border: 'none',
              }}
            />
          </div>
        </div>
      )}
    </div>
  );
}
