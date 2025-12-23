#!/usr/bin/env python3
"""
Test script to verify the communication system works
"""

import json
import os
import time
from assistant_bridge import AssistantBridge

def test_communication_system():
    print("Testing Communication System")
    print("=" * 50)
    
    # Clean up any existing files
    for f in ['assistant_inbox.json', 'assistant_outbox.json']:
        if os.path.exists(f):
            os.remove(f)
            print(f"✓ Cleaned up {f}")
    
    # Test 1: Initialize bridge
    print("\n[Test 1] Initializing Assistant Bridge...")
    bridge = AssistantBridge()
    print("✓ Bridge initialized")
    
    # Test 2: Send a test message (simulating user)
    print("\n[Test 2] Simulating user message...")
    with open('assistant_inbox.json', 'w') as f:
        json.dump([{
            "timestamp": "2025-12-20T20:43:19.096Z",
            "sender": "user",
            "message": "Test message from user",
            "read": False
        }], f)
    print("✓ User message created")
    
    # Test 3: Read messages
    print("\n[Test 3] Reading messages as assistant...")
    messages = bridge.get_new_messages()
    assert len(messages) == 1, "Should have 1 message"
    assert messages[0]['message'] == "Test message from user"
    print(f"✓ Read {len(messages)} message(s)")
    print(f"  Message: {messages[0]['message']}")
    
    # Test 4: Send response
    print("\n[Test 4] Sending response as assistant...")
    bridge.send_message("Test response from assistant")
    print("✓ Response sent")
    
    # Test 5: Verify response
    print("\n[Test 5] Verifying response file...")
    with open('assistant_outbox.json', 'r') as f:
        responses = json.load(f)
    assert len(responses) == 1, "Should have 1 response"
    assert responses[0]['message'] == "Test response from assistant"
    print(f"✓ Response verified")
    print(f"  Response: {responses[0]['message']}")
    
    # Test 6: Mark as read
    print("\n[Test 6] Checking read status...")
    with open('assistant_inbox.json', 'r') as f:
        inbox = json.load(f)
    assert inbox[0]['read'] == True, "Message should be marked as read"
    print("✓ Message marked as read")
    
    # Test 7: Multiple messages
    print("\n[Test 7] Testing multiple messages...")
    bridge.send_message("Second message")
    bridge.send_message("Third message")
    with open('assistant_outbox.json', 'r') as f:
        responses = json.load(f)
    assert len(responses) == 3, "Should have 3 messages total"
    print(f"✓ Multiple messages handled ({len(responses)} total)")
    
    print("\n" + "=" * 50)
    print("ALL TESTS PASSED! ✓")
    print("=" * 50)
    print("\nThe communication system is working correctly.")
    print("You can now use:")
    print("  - communication_window.py  (GUI interface)")
    print("  - example_assistant.py     (example assistant)")
    print("  - assistant_bridge.py      (for integration)")
    
    # Clean up
    print("\nCleaning up test files...")
    for f in ['assistant_inbox.json', 'assistant_outbox.json']:
        if os.path.exists(f):
            os.remove(f)
    print("✓ Test files cleaned up")

if __name__ == "__main__":
    try:
        test_communication_system()
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        exit(1)
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
