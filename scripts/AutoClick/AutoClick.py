import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# Cấu hình
delay = 0.03  # Khoảng thời gian giữa các lần click (giây)
button = Button.left  # Loại click (trái chuột)
start_stop_key = KeyCode(char='s')  # Nhấn phím 's' để bắt đầu/dừng
exit_key = KeyCode(char='e')  # Nhấn phím 'e' để thoát

class AutoClicker:
    def __init__(self, delay, button):
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        print("Bắt đầu click")
        self.running = True

    def stop_clicking(self):
        print("Dừng click")
        self.running = False

    def exit(self):
        print("Thoát")
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

# Lắng nghe sự kiện bàn phím
with Listener(on_press=on_press) as listener:
    clicker.run()
    listener.join()
