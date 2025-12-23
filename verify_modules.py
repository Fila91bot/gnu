#!/usr/bin/env python3
"""
Verify the GUI can be initialized (headless test)
"""

import sys
import os

# Test if tkinter is available
try:
    import tkinter as tk
    print("✓ tkinter is available")
except ImportError:
    print("✗ tkinter is not available")
    print("  Install with: sudo apt-get install python3-tk")
    sys.exit(1)

# Test importing the communication window module
try:
    # Don't actually create the window, just test imports
    import communication_window
    print("✓ communication_window module loads successfully")
except Exception as e:
    print(f"✗ Error loading communication_window: {e}")
    sys.exit(1)

# Test importing the assistant bridge
try:
    import assistant_bridge
    print("✓ assistant_bridge module loads successfully")
except Exception as e:
    print(f"✗ Error loading assistant_bridge: {e}")
    sys.exit(1)

# Test importing the example assistant
try:
    import example_assistant
    print("✓ example_assistant module loads successfully")
except Exception as e:
    print(f"✗ Error loading example_assistant: {e}")
    sys.exit(1)

print("\n" + "=" * 50)
print("All modules verified successfully!")
print("=" * 50)
print("\nTo use the communication window:")
print("  1. Run: python3 communication_window.py")
print("  2. In another terminal: python3 example_assistant.py")
print("  3. Type messages in the GUI window")
print("  4. See responses from the assistant")
