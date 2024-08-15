import ctypes
from ctypes import wintypes

def show_message_box(message, title, style):
    ctypes.windll.user32.MessageBoxW(None, message, title, style)

# Constants for message box styles
MB_OK = 0x0
MB_ICONEXCLAMATION = 0x50
MB_ICONINFORMATION = 0x60

# Show a warning message box
show_message_box("Your current screen scaling setting is not optimized for this application.\nPlease change your screen scaling to 100% or 125% to ensure proper functionality.", "Warning", MB_OK | MB_ICONINFORMATION)