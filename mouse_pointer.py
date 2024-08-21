import pyautogui
from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    if button.name == 'left' and pressed:
        print(f"Pointer position: X = {x}, Y = {y}")

# Set up the listener to monitor mouse clicks
with Listener(on_click=on_click) as listener:
    listener.join()
