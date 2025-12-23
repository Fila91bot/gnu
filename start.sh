#!/bin/bash

# Simple startup script for the communication system

echo "=================================================="
echo "GNU - Minimal Communication Window"
echo "=================================================="
echo ""
echo "Choose an option:"
echo "1. Desktop GUI (requires tkinter)"
echo "2. Web Browser Interface"
echo "3. Example Assistant"
echo "4. Run Tests"
echo "5. Exit"
echo ""
read -p "Enter choice [1-5]: " choice

case $choice in
    1)
        echo ""
        echo "Starting Desktop GUI..."
        python3 communication_window.py
        ;;
    2)
        echo ""
        echo "Starting Web Interface..."
        echo "Will open in browser at http://localhost:8080"
        python3 web_communication.py
        ;;
    3)
        echo ""
        echo "Starting Example Assistant..."
        echo "Open the communication window in another terminal"
        python3 example_assistant.py
        ;;
    4)
        echo ""
        echo "Running Tests..."
        python3 test_communication.py
        ;;
    5)
        echo "Goodbye!"
        exit 0
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac
