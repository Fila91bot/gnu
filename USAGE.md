# Quick Start Guide - GNU Communication Window

## Za Korisnike na Hrvatskom

### Što je ovo?

Minimalni komunikacijski sustav za interakciju s lokalnim asistentom. Omogućava vam da pošaljete poruke asistentom i primite odgovore.

### Kako to Radi?

1. **Prozor za komunikaciju** - Ovdje pišete poruke
2. **Asistent** - Čita vaše poruke i šalje odgovore
3. **JSON datoteke** - Koriste se za razmjenu poruka između vas i asistenta

### Brzi Početak

#### 1. Pokrenite Sučelje

**Desktop verzija:**
```bash
python3 communication_window.py
```

**Web verzija** (ako desktop ne radi):
```bash
python3 web_communication.py
```

#### 2. Pokrenite Primjer Asistenta

U drugom terminalu:
```bash
python3 example_assistant.py
```

#### 3. Počnite Komunicirati!

- Napišite poruku u prozoru
- Pritisnite "Pošalji" ili Ctrl+Enter
- Čekajte odgovor od asistenta
- Razgovor se sprema automatski

### Integracija sa Vašim Asistentom

Ako već imate lokalnog asistenta, možete ga povezati:

```python
from assistant_bridge import AssistantBridge

bridge = AssistantBridge()

# Čitaj poruke korisnika
messages = bridge.get_new_messages()
for msg in messages:
    user_text = msg['message']
    # Procesuiraj sa svojim asistentom...
    
    # Pošalji odgovor
    bridge.send_message("Odgovor vašeg asistenta")
```

### Prečaci

- **Ctrl+Enter** - Pošalji poruku (desktop verzija)
- **Očisti** - Briše razgovor (ne briše datoteke)

---

## For English Users

### What is This?

A minimal communication system to interact with a local assistant. It allows you to send messages to your assistant and receive responses.

### How it Works?

1. **Communication Window** - Where you write messages
2. **Assistant** - Reads your messages and sends responses
3. **JSON Files** - Used to exchange messages between you and the assistant

### Quick Start

#### 1. Start the Interface

**Desktop version:**
```bash
python3 communication_window.py
```

**Web version** (if desktop doesn't work):
```bash
python3 web_communication.py
```

#### 2. Start Example Assistant

In another terminal:
```bash
python3 example_assistant.py
```

#### 3. Start Communicating!

- Write a message in the window
- Press "Send" or Ctrl+Enter
- Wait for assistant's response
- Conversation is saved automatically

### Integration with Your Assistant

If you already have a local assistant, you can connect it:

```python
from assistant_bridge import AssistantBridge

bridge = AssistantBridge()

# Read user messages
messages = bridge.get_new_messages()
for msg in messages:
    user_text = msg['message']
    # Process with your assistant...
    
    # Send response
    bridge.send_message("Your assistant's response")
```

### Shortcuts

- **Ctrl+Enter** - Send message (desktop version)
- **Clear** - Clears conversation (doesn't delete files)

---

## Troubleshooting / Rješavanje Problema

### Desktop GUI ne radi / Desktop GUI doesn't work
- Install tkinter: `sudo apt-get install python3-tk`
- Or use web version: `python3 web_communication.py`

### Nema odgovora od asistenta / No response from assistant
- Check that assistant is running (`example_assistant.py`)
- Check `assistant_outbox.json` for messages
- Check that your assistant writes to this file

### Poruke se ne šalju / Messages not sending
- Check file permissions
- Look for errors in terminal
- Try running tests: `python3 test_communication.py`

### Port 8080 zauzet / Port 8080 busy
- Edit `web_communication.py` and change `PORT = 8080` to another port
- Or stop other programs using port 8080

---

## Advanced Usage

### Running Tests
```bash
python3 test_communication.py
```

### Custom Port for Web Interface
```bash
# Edit web_communication.py, line ~370:
# Change: PORT = 8080
# To:     PORT = 9000  (or any other port)
```

### File-based Integration

Read from: `assistant_inbox.json`
```json
[
  {
    "timestamp": "2025-12-20T20:43:19.096Z",
    "sender": "user",
    "message": "Hello!",
    "read": false
  }
]
```

Write to: `assistant_outbox.json`
```json
[
  {
    "timestamp": "2025-12-20T20:43:20.096Z",
    "sender": "assistant",
    "message": "Hi there!",
    "read": false
  }
]
```

### Using the Startup Script
```bash
./start.sh
```
Then choose option 1-4 from the menu.
