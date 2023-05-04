import os
import pyautogui
import keyboard
import time

def open_program(program_path):
    os.startfile(program_path)

def close_program(window_title):
    pyautogui.getWindowsWithTitle(window_title)[0].close()

# Key bindings and program configurations
config = {
    "open_notepad": {
        "key": "ctrl+alt+n",
        "program_path": "notepad.exe",
    },
    "close_notepad": {
        "key": "ctrl+alt+shift+n",
        "window_title": "Untitled - Notepad",
    },
    # Add more programs and key bindings here
}

while True:
    for action, settings in config.items():
        if keyboard.is_pressed(settings["key"]):
            if "program_path" in settings:
                open_program(settings["program_path"])
            elif "window_title" in settings:
                close_program(settings["window_title"])
            time.sleep(1)  # Prevent multiple triggers
