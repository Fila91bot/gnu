#!/usr/bin/env python3
"""
Web-based Communication Interface (alternative to tkinter)
Use this if tkinter is not available on your system
"""

import json
import os
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import threading
import webbrowser

class CommunicationHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        """Suppress default logging"""
        pass
    
    def do_GET(self):
        """Serve the main page or API endpoints"""
        if self.path == '/' or self.path == '/index.html':
            self.serve_main_page()
        elif self.path == '/api/messages':
            self.get_messages()
        elif self.path.startswith('/api/'):
            self.send_response(404)
            self.end_headers()
        else:
            self.serve_main_page()
    
    def do_POST(self):
        """Handle message posting"""
        if self.path == '/api/send':
            self.send_message()
        else:
            self.send_response(404)
            self.end_headers()
    
    def serve_main_page(self):
        """Serve the HTML interface"""
        html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Assistant Communication</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            width: 100%;
            max-width: 600px;
            height: 700px;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
        }
        .messages {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .message {
            margin-bottom: 15px;
            padding: 12px 15px;
            border-radius: 10px;
            max-width: 80%;
            word-wrap: break-word;
            animation: fadeIn 0.3s;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .message.user {
            background: #e3f2fd;
            margin-left: auto;
            border-bottom-right-radius: 3px;
        }
        .message.assistant {
            background: #e8f5e9;
            margin-right: auto;
            border-bottom-left-radius: 3px;
        }
        .message .sender {
            font-weight: bold;
            font-size: 12px;
            margin-bottom: 5px;
            color: #666;
        }
        .message .text {
            font-size: 14px;
            line-height: 1.4;
        }
        .input-area {
            padding: 20px;
            background: white;
            border-top: 1px solid #ddd;
        }
        .input-group {
            display: flex;
            gap: 10px;
        }
        #messageInput {
            flex: 1;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 14px;
            font-family: inherit;
            resize: vertical;
        }
        #messageInput:focus {
            outline: none;
            border-color: #667eea;
        }
        button {
            padding: 12px 30px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 14px;
            font-weight: bold;
            transition: transform 0.2s;
        }
        button:hover {
            transform: translateY(-2px);
        }
        button:active {
            transform: translateY(0);
        }
        .status {
            text-align: center;
            padding: 10px;
            font-size: 12px;
            color: #666;
            background: #f9f9f9;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            💬 Komunikacija sa Asistentom
        </div>
        <div class="messages" id="messages"></div>
        <div class="input-area">
            <div class="input-group">
                <textarea id="messageInput" rows="2" placeholder="Napišite poruku..."></textarea>
                <button onclick="sendMessage()">Pošalji</button>
            </div>
        </div>
        <div class="status" id="status">Spreman</div>
    </div>

    <script>
        let lastMessageCount = 0;

        function loadMessages() {
            fetch('/api/messages')
                .then(r => r.json())
                .then(data => {
                    const messagesDiv = document.getElementById('messages');
                    messagesDiv.innerHTML = '';
                    
                    data.forEach(msg => {
                        const div = document.createElement('div');
                        div.className = 'message ' + msg.sender;
                        div.innerHTML = `
                            <div class="sender">${msg.sender === 'user' ? 'Vi' : 'Asistent'}</div>
                            <div class="text">${escapeHtml(msg.message)}</div>
                        `;
                        messagesDiv.appendChild(div);
                    });
                    
                    messagesDiv.scrollTop = messagesDiv.scrollHeight;
                    
                    if (data.length > lastMessageCount) {
                        updateStatus('Nova poruka primljena');
                        lastMessageCount = data.length;
                    }
                })
                .catch(err => {
                    console.error('Error loading messages:', err);
                    updateStatus('Greška pri učitavanju poruka');
                });
        }

        function sendMessage() {
            const input = document.getElementById('messageInput');
            const message = input.value.trim();
            
            if (!message) return;
            
            fetch('/api/send', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: message })
            })
            .then(r => r.json())
            .then(data => {
                if (data.success) {
                    input.value = '';
                    loadMessages();
                    updateStatus('Poruka poslana');
                }
            })
            .catch(err => {
                console.error('Error sending message:', err);
                updateStatus('Greška pri slanju poruke');
            });
        }

        function updateStatus(text) {
            const status = document.getElementById('status');
            status.textContent = text;
            setTimeout(() => {
                status.textContent = 'Spreman';
            }, 3000);
        }

        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }

        // Keyboard shortcut
        document.getElementById('messageInput').addEventListener('keydown', e => {
            if (e.ctrlKey && e.key === 'Enter') {
                sendMessage();
            }
        });

        // Auto-refresh messages
        setInterval(loadMessages, 1000);
        loadMessages();
    </script>
</body>
</html>
        """
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html.encode())
    
    def get_messages(self):
        """Get all messages"""
        messages = []
        
        # Load user messages (inbox)
        if os.path.exists('assistant_inbox.json'):
            try:
                with open('assistant_inbox.json', 'r') as f:
                    inbox = json.load(f)
                    for msg in inbox:
                        messages.append({
                            'sender': 'user',
                            'message': msg.get('message', ''),
                            'timestamp': msg.get('timestamp', '')
                        })
            except:
                pass
        
        # Load assistant messages (outbox)
        if os.path.exists('assistant_outbox.json'):
            try:
                with open('assistant_outbox.json', 'r') as f:
                    outbox = json.load(f)
                    for msg in outbox:
                        messages.append({
                            'sender': 'assistant',
                            'message': msg.get('message', ''),
                            'timestamp': msg.get('timestamp', '')
                        })
            except:
                pass
        
        # Sort by timestamp
        messages.sort(key=lambda x: x.get('timestamp', ''))
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(messages).encode())
    
    def send_message(self):
        """Send a message from user"""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data.decode())
            message = data.get('message', '').strip()
            
            if message:
                # Load existing messages
                if os.path.exists('assistant_inbox.json'):
                    with open('assistant_inbox.json', 'r') as f:
                        messages = json.load(f)
                else:
                    messages = []
                
                # Add new message
                messages.append({
                    "timestamp": datetime.now().isoformat(),
                    "sender": "user",
                    "message": message,
                    "read": False
                })
                
                # Save
                with open('assistant_inbox.json', 'w') as f:
                    json.dump(messages, f, indent=2)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": True}).encode())
            else:
                self.send_response(400)
                self.end_headers()
        except Exception as e:
            print(f"Error: {e}")
            self.send_response(500)
            self.end_headers()

def main():
    PORT = 8080
    
    print("=" * 50)
    print("WEB-BASED COMMUNICATION INTERFACE")
    print("=" * 50)
    print(f"\nStarting server on http://localhost:{PORT}")
    print("\nOtvorite web preglednik i idite na:")
    print(f"  http://localhost:{PORT}")
    print("\nPritisnite Ctrl+C za izlaz\n")
    
    server = HTTPServer(('localhost', PORT), CommunicationHandler)
    
    # Try to open browser automatically
    threading.Timer(1.5, lambda: webbrowser.open(f'http://localhost:{PORT}')).start()
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServer zaustavljen. Doviđenja!")
        server.shutdown()

if __name__ == "__main__":
    main()
