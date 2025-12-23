#!/usr/bin/env python3
"""
Simple Example Assistant
Demonstrates how to integrate your assistant with the communication window
"""

from assistant_bridge import AssistantBridge
import time

def simple_assistant_logic(user_message):
    """
    Simple example of assistant logic
    Replace this with your actual assistant's processing
    """
    msg_lower = user_message.lower()
    
    # Example responses
    if 'zdravo' in msg_lower or 'hello' in msg_lower or 'hi' in msg_lower:
        return "Zdravo! Kako vam mogu pomoći?"
    
    elif 'kako si' in msg_lower or 'how are you' in msg_lower:
        return "Dobro sam, hvala! Spreman sam za rad."
    
    elif 'pomoć' in msg_lower or 'help' in msg_lower:
        return "Mogu vam pomoći sa:\n- Organizacijom mapa\n- Čišćenjem desktopa\n- Upravljanjem datotekama\n- I još mnogo toga!"
    
    elif 'hvala' in msg_lower or 'thanks' in msg_lower:
        return "Molim! Uvijek tu sam ako trebate pomoć."
    
    elif 'doviđenja' in msg_lower or 'bye' in msg_lower or 'goodbye' in msg_lower:
        return "Doviđenja! Javite se kada god trebate pomoć."
    
    else:
        return f"Primio sam vašu poruku: '{user_message}'. Integrirajte ovaj dio sa vašim asistentom za pravu funkcionalnost."

def main():
    bridge = AssistantBridge()
    
    print("=" * 50)
    print("SIMPLE EXAMPLE ASSISTANT")
    print("=" * 50)
    print("\nAsistent je pokrenut i čeka poruke...")
    print("Otvorite communication_window.py da počnete komunicirati.")
    print("\nPritisnite Ctrl+C za izlaz\n")
    
    # Send initial greeting
    bridge.send_message("Asistent je online i spreman za komunikaciju! 👋")
    
    # Monitor for messages and respond
    try:
        while True:
            messages = bridge.get_new_messages()
            
            for msg in messages:
                user_message = msg.get('message', '')
                timestamp = msg.get('timestamp', '')
                
                print(f"[{timestamp}] Nova poruka: {user_message}")
                
                # Process with assistant logic
                response = simple_assistant_logic(user_message)
                
                # Send response
                bridge.send_message(response)
                print(f"[ODGOVOR] {response}\n")
            
            time.sleep(1)
    
    except KeyboardInterrupt:
        print("\n\nAsistent zaustavljen. Doviđenja!")
        bridge.send_message("Asistent se isključuje... Doviđenja! 👋")

if __name__ == "__main__":
    main()
