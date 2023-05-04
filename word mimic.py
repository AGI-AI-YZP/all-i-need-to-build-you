from pynput.keyboard import Key, Listener, Controller
import time

keyboard = Controller()
logged_keys = []

def on_press(key):
    logged_keys.append(key)

def mimic_typing(logged_keys):
    time.sleep(2)  # Give yourself a couple of seconds to focus the text field
    for key in logged_keys:
        if key == Key.space:
            keyboard.type(' ')
        elif key == Key.enter:
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        else:
            keyboard.type(str(key).replace("'", ""))

with Listener(on_press=on_press) as listener:
    listener.join()

mimic_typing(logged_keys)