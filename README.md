# Auto Click

**Auto Click** is a lightweight Python tool that automates mouse clicking. It is designed for repetitive clicking tasks in games, productivity tools, or testing environments.

## Features

- Automates continuous mouse clicks with customizable intervals.
- Configurable keyboard shortcuts:
  - Press `S` to start or stop the auto clicker.
  - Press `E` to exit the program.
- Minimal CPU usage with optimized loops.
- Easily customizable to change click buttons or key bindings.

---

## How It Works

This tool uses the Python library `pynput` to simulate mouse clicks and listen to keyboard input. By default, it performs **left mouse button clicks**, but it can be customized for other mouse buttons.

---

## Installation and Setup

### Prerequisites

Ensure that Python is installed on your system. You can download it [here](https://www.python.org/).

### Required Libraries

Install the required Python library using `pip`:

```bash
pip install pynput
```
##Running the Program
Clone this repository or download the autoclicker.py file.
Open a terminal in the project directory.
Run the program:
```bash
python autoclicker.py
```
##Usage Instructions

- Press S to start or stop the auto clicker.
- Press E to exit the program.
##Code Overview
The core functionality is implemented in the AutoClicker class, which uses the pynput.mouse.Controller for mouse actions and pynput.keyboard.Listener to capture keyboard input.

##Key Components
- Mouse Controller: Simulates mouse click actions.
- Keyboard Listener: Listens for specific keypress events (S and E) to control the flow of the program.
- Customizable Settings:
  - delay: Time interval between clicks.
  - button: Specifies the mouse button to be clicked.
  - start_stop_key: The key to toggle the auto clicker.
  - exit_key: The key to terminate the program.
##Customizations

Change the Mouse Button
To change the mouse button (e.g., right-click), modify this line in the code:

button = Button.left
Replace Button.left with:

Button.right for the right mouse button.
Button.middle for the middle mouse button.
Adjust the Click Speed
Modify the delay variable to change the time interval between clicks:

delay = 0.1  # Set to your preferred interval in seconds
Change the Shortcut Keys
Customize the keyboard shortcuts by modifying the KeyCode definitions. For example:

start_stop_key = KeyCode(char='s')  # Replace 's' with your preferred key
exit_key = KeyCode(char='e')       # Replace 'e' with your preferred key
Build as an Executable

To make the program easier to run without requiring Python, you can package it into an executable file.

Steps to Package
Install PyInstaller:
```bash
pip install pyinstaller
```
Create an executable:
```bash
pyinstaller --onefile --windowed --name "AutoClicker" autoclicker.py
```
The executable file will be generated in the dist folder.
Contributing

We welcome contributions to improve and expand this tool. Here’s how you can contribute:

Fork this repository.
Create a new branch:
```bash
git checkout -b feature/YourFeature
```
Commit your changes:
```bash
git commit -m "Add YourFeature"
```
Push to the branch:
```bash
git push origin feature/YourFeature
```
Open a pull request.

##License

This project is licensed under the MIT License. See the LICENSE file for details.
##Contact

For questions or support, please create an issue in the repository or reach out to [dogiaan91@gmail.com].
