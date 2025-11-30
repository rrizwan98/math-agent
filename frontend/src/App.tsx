import { ChatKit, useChatKit } from '@openai/chatkit-react';
import './App.css';

function App() {
  const { control } = useChatKit({
    api: {
      url: 'http://localhost:8000/chat',
      // Adding a placeholder domainKey as required by CustomApiConfig
      domainKey: 'placeholder-domain-key', 
      fetch: async (input: RequestInfo | URL, init?: RequestInit) => {
        if (init && init.body) {
          try {
            const chatkitPayload = JSON.parse(init.body.toString());
            // Assuming the ChatKit payload has a 'text' field or an array of 'messages'
            // and we want the last user message from that array.
            let userQuery = '';

            if (chatkitPayload.text) {
                userQuery = chatkitPayload.text;
            } else if (chatkitPayload.messages && chatkitPayload.messages.length > 0) {
              const lastMessage = chatkitPayload.messages[chatkitPayload.messages.length - 1];
              if (lastMessage.role === 'user') {
                userQuery = lastMessage.content;
              }
            }

            if (userQuery) {
                const newInit = {
                  ...init,
                  method: 'POST', // Ensure method is POST
                  body: JSON.stringify({ query: userQuery }),
                  headers: {
                    ...init.headers,
                    'Content-Type': 'application/json',
                  },
                };
                // Ensure the URL is correctly set to our FastAPI chat endpoint
                return fetch('http://localhost:8000/chat', newInit);
            }
          } catch (e) {
            console.error('Error parsing ChatKit payload or preparing fetch:', e);
          }
        }
        // Fallback for non-message-sending requests or if parsing fails
        // This might also be for requests ChatKit makes internally that we don't want to intercept.
        return fetch(input, init);
      },
    },
  });

  return (
    <div style={{ height: '100vh', width: '100vw', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
      <ChatKit
        control={control}
        title="Math Agent"
      />
    </div>
  );
}

export default App;