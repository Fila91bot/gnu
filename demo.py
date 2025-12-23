#!/usr/bin/env python3
"""
Demo script - Simulates a conversation between user and assistant
"""

import json
import os
import time
from datetime import datetime

def clear_files():
    """Clear any existing communication files"""
    for f in ['assistant_inbox.json', 'assistant_outbox.json']:
        if os.path.exists(f):
            os.remove(f)

def create_demo_conversation():
    """Create a demo conversation"""
    print("=" * 60)
    print("DEMO: Communication System Simulation")
    print("=" * 60)
    print()
    
    # Clear existing files
    clear_files()
    
    # User message 1
    print("[USER] Zdravo! Jesi li tu?")
    with open('assistant_inbox.json', 'w') as f:
        json.dump([{
            "timestamp": datetime.now().isoformat(),
            "sender": "user",
            "message": "Zdravo! Jesi li tu?",
            "read": False
        }], f, indent=2)
    
    time.sleep(0.5)
    
    # Assistant response 1
    print("[ASSISTANT] Zdravo! Da, tu sam i spreman za pomoć! 👋")
    with open('assistant_outbox.json', 'w') as f:
        json.dump([{
            "timestamp": datetime.now().isoformat(),
            "sender": "assistant",
            "message": "Zdravo! Da, tu sam i spreman za pomoć! 👋",
            "read": False
        }], f, indent=2)
    
    time.sleep(0.5)
    
    # User message 2
    print("[USER] Odlično! Trebam pomoć sa organizacijom mapa.")
    with open('assistant_inbox.json', 'r') as f:
        inbox = json.load(f)
    inbox[0]['read'] = True
    inbox.append({
        "timestamp": datetime.now().isoformat(),
        "sender": "user",
        "message": "Odlično! Trebam pomoć sa organizacijom mapa.",
        "read": False
    })
    with open('assistant_inbox.json', 'w') as f:
        json.dump(inbox, f, indent=2)
    
    time.sleep(0.5)
    
    # Assistant response 2
    print("[ASSISTANT] Mogu ti pomoći! Što točno želiš organizirati?")
    with open('assistant_outbox.json', 'r') as f:
        outbox = json.load(f)
    outbox[0]['read'] = True
    outbox.append({
        "timestamp": datetime.now().isoformat(),
        "sender": "assistant",
        "message": "Mogu ti pomoći! Što točno želiš organizirati?",
        "read": False
    })
    with open('assistant_outbox.json', 'w') as f:
        json.dump(outbox, f, indent=2)
    
    time.sleep(0.5)
    
    # User message 3
    print("[USER] Desktop mi je prepun datoteka, trebam ih sortirati.")
    with open('assistant_inbox.json', 'r') as f:
        inbox = json.load(f)
    inbox[1]['read'] = True
    inbox.append({
        "timestamp": datetime.now().isoformat(),
        "sender": "user",
        "message": "Desktop mi je prepun datoteka, trebam ih sortirati.",
        "read": False
    })
    with open('assistant_inbox.json', 'w') as f:
        json.dump(inbox, f, indent=2)
    
    time.sleep(0.5)
    
    # Assistant response 3
    print("[ASSISTANT] Super! Mogu ti stvoriti mape po vrsti datoteka i sortirati ih automatski.")
    with open('assistant_outbox.json', 'r') as f:
        outbox = json.load(f)
    outbox[1]['read'] = True
    outbox.append({
        "timestamp": datetime.now().isoformat(),
        "sender": "assistant",
        "message": "Super! Mogu ti stvoriti mape po vrsti datoteka i sortirati ih automatski.",
        "read": False
    })
    with open('assistant_outbox.json', 'w') as f:
        json.dump(outbox, f, indent=2)
    
    print()
    print("=" * 60)
    print("DEMO COMPLETE!")
    print("=" * 60)
    print()
    print("✓ Communication files created with demo conversation")
    print("✓ Files: assistant_inbox.json, assistant_outbox.json")
    print()
    print("Now you can open:")
    print("  - communication_window.py (to see the conversation)")
    print("  - web_communication.py (to see it in browser)")
    print()
    
    # Display file contents
    print("\n📁 assistant_inbox.json:")
    print("-" * 60)
    with open('assistant_inbox.json', 'r') as f:
        print(f.read())
    
    print("\n📁 assistant_outbox.json:")
    print("-" * 60)
    with open('assistant_outbox.json', 'r') as f:
        print(f.read())

if __name__ == "__main__":
    create_demo_conversation()
