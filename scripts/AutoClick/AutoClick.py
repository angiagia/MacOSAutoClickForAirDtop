import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# Configuration
delay = 0.03  # Delay between clicks (seconds)
button = Button.left  # Click type (left mouse button)
start_stop_key = KeyCode(char='s')  # Press 's' to start/stop
exit_key = KeyCode(char='e')  # Press 'e' to exit

class AutoClicker:
    def __init__(self, delay, button):
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        print("Start clicking")
        self.running = True

    def stop_clicking(self):
        print("Stop clicking")
        self.running = False

    def exit(self):
        print("Exit")
        self.stop_clicking()
        self.program_running = False

    def run(self):
        mouse = Controller()
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

clicker = AutoClicker(delay, button)

def on_press(key):
    if key == start_stop_key:
        if clicker.running:
            clicker.stop_clicking()
        else:
            clicker.start_clicking()
    elif key == exit_key:
        clicker.exit()
        return False

# Listen for keyboard events
with Listener(on_press=on_press) as listener:
    clicker.run()
    listener.join()
