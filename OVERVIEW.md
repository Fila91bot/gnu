# GNU - Minimal Communication Window

## Project Overview

A lightweight, file-based communication system for interacting with local assistants. Created to solve the problem of communicating with locally-running automation and assistant tools.

## 🎯 Problem Solved

When developing local assistants for tasks like:
- Desktop organization
- File management
- Folder cleanup
- System automation

You need a simple way to communicate with them without complex network setups or APIs.

## ✅ Solution

A minimal communication interface using:
- **File-based messaging** (JSON) - No network ports needed
- **Dual interfaces** - Desktop GUI (tkinter) or Web browser
- **Simple integration** - Easy to connect with existing assistants
- **Bidirectional** - Send and receive messages
- **Real-time** - Automatic message monitoring

## 📦 What's Included

### User Interfaces
- **communication_window.py** - Desktop GUI using tkinter
- **web_communication.py** - Web browser interface (port 8080)

### Integration Tools
- **assistant_bridge.py** - Python module for easy integration
- **example_assistant.py** - Working example assistant
- **demo.py** - Demo conversation generator

### Utilities
- **start.sh** - Menu-based launcher
- **test_communication.py** - Test suite
- **verify_modules.py** - Module verification

### Documentation
- **README.md** - Main documentation
- **USAGE.md** - Detailed usage guide (Croatian + English)

## 🚀 Quick Start

```bash
# Option 1: Desktop GUI
python3 communication_window.py

# Option 2: Web Interface
python3 web_communication.py

# Option 3: Use menu
./start.sh
```

Then in another terminal:
```bash
# Start example assistant
python3 example_assistant.py
```

## 🔧 How It Works

```
┌──────────────────┐         ┌────────────────────┐
│ Communication    │         │ Assistant          │
│ Window           │         │ (Your Code)        │
└──────────────────┘         └────────────────────┘
         │                            │
         ▼                            ▼
┌──────────────────┐         ┌────────────────────┐
│ assistant_       │◄────────┤ Reads messages     │
│ inbox.json       │         │ from user          │
└──────────────────┘         └────────────────────┘
         │                            │
         │                            ▼
         │                   ┌────────────────────┐
         │                   │ Processes with     │
         │                   │ assistant logic    │
         │                   └────────────────────┘
         │                            │
         ▼                            ▼
┌──────────────────┐         ┌────────────────────┐
│ Displays         │◄────────┤ Writes response    │
│ responses        │         │ to outbox          │
└──────────────────┘         └────────────────────┘
                             ┌────────────────────┐
                             │ assistant_         │
                             │ outbox.json        │
                             └────────────────────┘
```

## 🔌 Integration Examples

### Python Assistant
```python
from assistant_bridge import AssistantBridge

bridge = AssistantBridge()
messages = bridge.get_new_messages()

for msg in messages:
    response = process_message(msg['message'])
    bridge.send_message(response)
```

### Any Language (File-based)
Read from `assistant_inbox.json`, write to `assistant_outbox.json`

## ✨ Features

- ✅ No network configuration needed
- ✅ Works with any programming language
- ✅ Persistent message history
- ✅ Real-time updates
- ✅ Multiple interface options
- ✅ Simple file-based protocol
- ✅ Croatian language support
- ✅ Cross-platform (Windows, Linux, macOS)

## 📝 Testing

```bash
# Run test suite
python3 test_communication.py

# Run demo
python3 demo.py
```

## 🌍 Language Support

- **Interface**: Croatian (Hrvatska verzija)
- **Code**: English
- **Documentation**: Croatian + English

## 📄 License

See LICENSE file for details.

## 🤝 Contributing

This is a minimal, focused project. It does one thing well: enable communication with local assistants.

## 💡 Use Cases

- Desktop file organization tools
- Local AI assistants
- Automation scripts
- Task management systems
- System maintenance tools
- Custom productivity assistants

---

Made with ❤️ for local assistant communication
