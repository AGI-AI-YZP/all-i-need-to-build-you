import pyautogui
import time
from pynput import keyboard, mouse
from threading import Thread

# Record events
def record_events(duration):
    events = []

    def on_click(x, y, button, pressed):
        if pressed:
            timestamp = time.time() - start_time
            events.append(("mouse", x, y, button, timestamp))

    def on_key(key, action):
        try:
            timestamp = time.time() - start_time
            events.append(("keyboard", key, action, timestamp))
        except AttributeError:
            pass

    start_time = time.time()
    with mouse.Listener(on_click=on_click) as mouse_listener, keyboard.Listener(on_press=on_key, on_release=on_key) as keyboard_listener:
        while time.time() - start_time < duration:
            time.sleep(0.001)

    return events

# Replay events
def replay_events(events):
    start_time = time.time()

    for event in events:
        time_to_wait = event[-1] - (time.time() - start_time)
        if time_to_wait > 0:
            time.sleep(time_to_wait)

        if event[0] == "mouse":
            x, y, button, _ = event[1:]
            pyautogui.click(x, y, button=button.name.lower())
        elif event[0] == "keyboard":
            key, action, _ = event[1:]
            if action == "press":
                pyautogui.press(str(key))
            elif action == "release":
                pyautogui.release(str(key))

# Main
duration = 10  # Record events for 10 seconds
print(f"Recording events for {duration} seconds...")
events = record_events(duration)
print(f"Recorded {len(events)} events. Replaying...")
replay_events(events)
print("Replay finished.")