import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# Configuration
button = Button.left  # Click type (left mouse button)
start_stop_key = KeyCode(char='s')  # Press 's' to start/stop
exit_key = KeyCode(char='e')  # Press 'e' to exit

class AutoHold:
    def __init__(self, button):
        self.button = button
        self.running = False
        self.program_running = True

    def start_holding(self):
        print("Start holding mouse")
        self.running = True

    def stop_holding(self):
        print("Stop holding mouse")
        self.running = False

    def exit(self):
        print("Exit")
        self.stop_holding()
        self.program_running = False

    def run(self):
        mouse = Controller()
        while self.program_running:
            while self.running:
                mouse.press(self.button)
            if not self.running:
                mouse.release(self.button)
            time.sleep(0.1)

holder = AutoHold(button)

def on_press(key):
    if key == start_stop_key:
        if holder.running:
            holder.stop_holding()
        else:
            holder.start_holding()
    elif key == exit_key:
        holder.exit()
        return False

with Listener(on_press=on_press) as listener:
    holder.run()