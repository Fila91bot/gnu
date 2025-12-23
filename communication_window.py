#!/usr/bin/env python3
"""
Minimal Communication Window for Local Assistant
A simple GUI interface to communicate with a local assistant
"""

import tkinter as tk
from tkinter import scrolledtext
import json
import os
from datetime import datetime
import threading
import time

class CommunicationWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Assistant Communication")
        self.root.geometry("500x600")
        
        # Communication files
        self.inbox_file = "assistant_inbox.json"
        self.outbox_file = "assistant_outbox.json"
        
        # Initialize communication files if they don't exist
        self._init_files()
        
        # Create UI elements
        self._create_ui()
        
        # Start monitoring for responses
        self.running = True
        self.monitor_thread = threading.Thread(target=self._monitor_responses, daemon=True)
        self.monitor_thread.start()
    
    def _init_files(self):
        """Initialize communication files"""
        if not os.path.exists(self.inbox_file):
            with open(self.inbox_file, 'w') as f:
                json.dump([], f)
        
        if not os.path.exists(self.outbox_file):
            with open(self.outbox_file, 'w') as f:
                json.dump([], f)
    
    def _create_ui(self):
        """Create the user interface"""
        # Title label
        title_label = tk.Label(
            self.root, 
            text="Komunikacija sa Asistentom", 
            font=("Arial", 14, "bold")
        )
        title_label.pack(pady=10)
        
        # Conversation display area
        conversation_frame = tk.Frame(self.root)
        conversation_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        tk.Label(conversation_frame, text="Razgovor:", font=("Arial", 10, "bold")).pack(anchor=tk.W)
        
        self.conversation_area = scrolledtext.ScrolledText(
            conversation_frame,
            wrap=tk.WORD,
            width=50,
            height=20,
            font=("Arial", 10)
        )
        self.conversation_area.pack(fill=tk.BOTH, expand=True)
        self.conversation_area.config(state=tk.DISABLED)
        
        # Input area
        input_frame = tk.Frame(self.root)
        input_frame.pack(padx=10, pady=5, fill=tk.X)
        
        tk.Label(input_frame, text="Vaša poruka:", font=("Arial", 10, "bold")).pack(anchor=tk.W)
        
        self.input_field = tk.Text(
            input_frame,
            wrap=tk.WORD,
            width=50,
            height=4,
            font=("Arial", 10)
        )
        self.input_field.pack(fill=tk.X, pady=5)
        
        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(padx=10, pady=5)
        
        self.send_button = tk.Button(
            button_frame,
            text="Pošalji",
            command=self._send_message,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=20
        )
        self.send_button.pack(side=tk.LEFT, padx=5)
        
        clear_button = tk.Button(
            button_frame,
            text="Očisti",
            command=self._clear_conversation,
            bg="#f44336",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=20
        )
        clear_button.pack(side=tk.LEFT, padx=5)
        
        # Bind Enter key to send message (Ctrl+Enter)
        self.input_field.bind('<Control-Return>', lambda e: self._send_message())
        
        # Status bar
        self.status_label = tk.Label(
            self.root,
            text="Status: Spreman",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)
    
    def _send_message(self):
        """Send message to assistant"""
        message = self.input_field.get("1.0", tk.END).strip()
        
        if not message:
            return
        
        # Add to conversation
        self._add_to_conversation("Vi", message, "#E3F2FD")
        
        # Save to inbox file for assistant to read
        try:
            with open(self.inbox_file, 'r') as f:
                messages = json.load(f)
            
            messages.append({
                "timestamp": datetime.now().isoformat(),
                "sender": "user",
                "message": message,
                "read": False
            })
            
            with open(self.inbox_file, 'w') as f:
                json.dump(messages, f, indent=2)
            
            self.status_label.config(text="Status: Poruka poslana")
            self.input_field.delete("1.0", tk.END)
            
        except Exception as e:
            self._add_to_conversation("Sistem", f"Greška: {str(e)}", "#FFEBEE")
            self.status_label.config(text=f"Status: Greška - {str(e)}")
    
    def _monitor_responses(self):
        """Monitor outbox file for assistant responses"""
        last_check = 0
        
        while self.running:
            try:
                if os.path.exists(self.outbox_file):
                    with open(self.outbox_file, 'r') as f:
                        messages = json.load(f)
                    
                    # Check for new messages
                    unread = [m for m in messages if not m.get('read', False)]
                    
                    for msg in unread:
                        self._add_to_conversation(
                            "Asistent",
                            msg.get('message', ''),
                            "#E8F5E9"
                        )
                        msg['read'] = True
                    
                    # Update file if there were unread messages
                    if unread:
                        with open(self.outbox_file, 'w') as f:
                            json.dump(messages, f, indent=2)
                        
                        self.status_label.config(text="Status: Primljena nova poruka")
                
            except Exception as e:
                print(f"Monitor error: {e}")
            
            time.sleep(1)
    
    def _add_to_conversation(self, sender, message, bg_color):
        """Add message to conversation display"""
        self.conversation_area.config(state=tk.NORMAL)
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Create tags for styling
        tag_name = f"msg_{timestamp}_{sender}"
        self.conversation_area.tag_config(tag_name, background=bg_color, lmargin1=10, lmargin2=10)
        
        # Insert message
        self.conversation_area.insert(tk.END, f"\n[{timestamp}] {sender}:\n", "bold")
        self.conversation_area.insert(tk.END, f"{message}\n", tag_name)
        
        self.conversation_area.config(state=tk.DISABLED)
        self.conversation_area.see(tk.END)
    
    def _clear_conversation(self):
        """Clear the conversation display"""
        self.conversation_area.config(state=tk.NORMAL)
        self.conversation_area.delete("1.0", tk.END)
        self.conversation_area.config(state=tk.DISABLED)
        self.status_label.config(text="Status: Razgovor očišćen")
    
    def on_closing(self):
        """Handle window closing"""
        self.running = False
        self.root.destroy()

def main():
    root = tk.Tk()
    app = CommunicationWindow(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
