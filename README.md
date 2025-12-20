# GNU - Minimal Communication Window

A simple communication interface for interacting with a local assistant.

## Overview

This project provides a minimal GUI window for bidirectional communication with a local assistant. It uses file-based message passing (JSON files) to enable communication between the user interface and your local assistant.

## Features

- ✅ Simple, lightweight GUI interface
- ✅ Bidirectional communication (send and receive messages)
- ✅ Real-time message monitoring
- ✅ File-based communication (no network ports needed)
- ✅ Easy integration with any assistant/automation system
- ✅ Croatian language interface

## Requirements

- Python 3.x (with tkinter - usually included by default)
- No additional dependencies needed!

## Quick Start

### 1. Start the Communication Window

Run the communication window to start interacting:

```bash
python3 communication_window.py
```

This will open a GUI window where you can:
- Type messages to your assistant
- Receive responses from your assistant
- View conversation history
- Clear the conversation

### 2. Integrate with Your Assistant

Your local assistant needs to read from and write to the communication files:

#### Option A: Use the Assistant Bridge Module

```python
from assistant_bridge import AssistantBridge

# Create bridge instance
bridge = AssistantBridge()

# Check for new messages from user
messages = bridge.get_new_messages()
for msg in messages:
    user_message = msg['message']
    # Process the message with your assistant...
    
    # Send response back
    bridge.send_message("Your assistant's response here")
```

#### Option B: Run the Bridge in Monitor Mode

```python
from assistant_bridge import AssistantBridge

def my_response_handler(message):
    user_msg = message.get('message', '')
    # Your assistant logic here
    response = process_with_my_assistant(user_msg)
    return response

bridge = AssistantBridge()
bridge.monitor_and_respond(my_response_handler)
```

#### Option C: Direct File Access

Read from: `assistant_inbox.json` - Contains messages from the user
Write to: `assistant_outbox.json` - Contains responses to the user

File format:
```json
[
  {
    "timestamp": "2025-12-20T20:43:19.096Z",
    "sender": "user",
    "message": "Hello assistant!",
    "read": false
  }
]
```

## Files

- `communication_window.py` - Main GUI application for user interaction
- `assistant_bridge.py` - Bridge module for assistant integration
- `assistant_inbox.json` - Messages from user to assistant (auto-created)
- `assistant_outbox.json` - Messages from assistant to user (auto-created)

## Usage Tips

- **Ctrl+Enter** in the input field sends the message
- The window automatically checks for new assistant responses every second
- Messages are persistent - they're saved to JSON files
- You can run multiple instances of your assistant that read/write to these files

## Integration Examples

### Example 1: Simple Python Assistant

```python
from assistant_bridge import AssistantBridge
import time

bridge = AssistantBridge()

while True:
    messages = bridge.get_new_messages()
    for msg in messages:
        user_text = msg['message']
        # Simple echo response
        bridge.send_message(f"Razumijem: {user_text}")
    time.sleep(1)
```

### Example 2: Shell Script Integration

```bash
#!/bin/bash
while true; do
    # Read new messages (implement JSON parsing as needed)
    # Process with your assistant
    # Write response back to assistant_outbox.json
    sleep 1
done
```

## Troubleshooting

- **Window doesn't open**: Make sure Python 3 and tkinter are installed
- **No responses**: Check that your assistant is writing to `assistant_outbox.json`
- **Messages not received**: Verify your assistant is reading from `assistant_inbox.json`

## License

See LICENSE file for details.
