#Python Keylogger

Author: Jershon Paul Isaac R
Internship Task: Task – SkillCraft Technology Internship (Cybersecurity)

##Overview

This Python project is a lightweight Keylogger that records keystrokes into a log file for monitoring and research purposes. It demonstrates how keystroke capture works using the pynput library. Special keys like space and enter are handled properly, while modifier keys (Shift, Ctrl) are ignored for clean output.

It is designed purely for educational and cybersecurity research to understand keystroke logging mechanisms.

##Features

Keystroke Logging: Captures all typed characters.

Special Key Handling: Converts space → " ", enter → new line.

Modifier Key Filtering: Ignores Shift, Ctrl (and can be extended for Alt, Tab, etc.).

Automatic Log File: Saves keystrokes in log.txt.

Lightweight & Simple: Uses only pynput.

##Installation

Clone the repository:
```
git clone https://github.com/jershonpaulisaac/python-keylogger.git
cd python-keylogger
```

Install dependency:
```
pip install pynput
```
Usage

Run the keylogger with:
```
python keylogger.py

```
Keystrokes will be stored in log.txt.

Example

Typing the following:
```
Hello World
This is a test123
```

Will produce in log.txt:
```
Hello World
This is a test123
```
##How It Works

Keyboard Listener: Uses pynput.Listener to capture keypress events.

Key Conversion: Converts Key.space → " ", Key.enter → "\n".

Filtering: Skips Shift and Ctrl keys to avoid clutter.

Logging: Appends captured keystrokes into log.txt.

##License

© 2025 Jershon Paul Isaac R. All rights reserved.

This software and its source code are protected. You may view and use the code for personal or educational purposes only.
Modification, distribution, or commercial use of this code is strictly prohibited without prior written permission from the author.
