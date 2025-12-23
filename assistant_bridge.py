#!/usr/bin/env python3
"""
Assistant Bridge - Interface for the local assistant to communicate
This script can be used by your local assistant to read user messages and send responses
"""

import json
import os
from datetime import datetime
import time

class AssistantBridge:
    def __init__(self):
        self.inbox_file = "assistant_inbox.json"
        self.outbox_file = "assistant_outbox.json"
        
    def get_new_messages(self):
        """Get unread messages from user"""
        if not os.path.exists(self.inbox_file):
            return []
        
        try:
            with open(self.inbox_file, 'r') as f:
                messages = json.load(f)
            
            # Get unread messages
            unread = [m for m in messages if not m.get('read', False)]
            
            # Mark as read
            for msg in messages:
                if not msg.get('read', False):
                    msg['read'] = True
            
            # Save back
            with open(self.inbox_file, 'w') as f:
                json.dump(messages, f, indent=2)
            
            return unread
            
        except Exception as e:
            print(f"Error reading messages: {e}")
            return []
    
    def send_message(self, message):
        """Send a response back to the user"""
        if not os.path.exists(self.outbox_file):
            messages = []
        else:
            try:
                with open(self.outbox_file, 'r') as f:
                    messages = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError, PermissionError):
                messages = []
        
        messages.append({
            "timestamp": datetime.now().isoformat(),
            "sender": "assistant",
            "message": message,
            "read": False
        })
        
        try:
            with open(self.outbox_file, 'w') as f:
                json.dump(messages, f, indent=2)
            return True
        except Exception as e:
            print(f"Error sending message: {e}")
            return False
    
    def monitor_and_respond(self, response_callback):
        """
        Monitor for new messages and call response_callback for each new message
        
        Args:
            response_callback: Function that takes a message dict and returns a response string
        """
        print("Assistant Bridge monitoring started...")
        print("Press Ctrl+C to stop")
        
        try:
            while True:
                messages = self.get_new_messages()
                
                for msg in messages:
                    print(f"\n[{msg['timestamp']}] New message: {msg['message']}")
                    
                    # Call the callback to get response
                    response = response_callback(msg)
                    
                    if response:
                        self.send_message(response)
                        print(f"Response sent: {response}")
                
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\nAssistant Bridge stopped")

def example_response_handler(message):
    """
    Example response handler - replace this with your assistant's logic
    """
    user_msg = message.get('message', '').lower()
    
    # Simple echo response for demonstration
    return f"Primio sam vašu poruku: '{message.get('message', '')}'"

def main():
    """Example usage"""
    bridge = AssistantBridge()
    
    print("=== Assistant Bridge Example ===")
    print("This is an example implementation.")
    print("Integrate this with your local assistant.\n")
    
    # Example 1: Check for messages once
    print("1. Checking for new messages...")
    messages = bridge.get_new_messages()
    print(f"   Found {len(messages)} new message(s)")
    
    # Example 2: Send a test message
    print("\n2. Sending test response...")
    bridge.send_message("Asistent je spreman za komunikaciju!")
    print("   Test message sent")
    
    # Example 3: Start monitoring (commented out by default)
    print("\n3. To start monitoring mode, uncomment the following line in the code:")
    print("   # bridge.monitor_and_respond(example_response_handler)")
    
    # Uncomment to enable monitoring:
    # bridge.monitor_and_respond(example_response_handler)

if __name__ == "__main__":
    main()
