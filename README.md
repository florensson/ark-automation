# ARK automation

This project was built purely for fun and experimentation.  
**Use at your own risk.** The code is messy, unoptimized, and not actively maintained.
There is a mix of lang use in comments and documentation is minimal.
It mixes object-oriented (class-based) and procedural (function-based) structures in ways that are not best practice in production code.
The goal was to quickly test ideas and see what worked, rather than to maintain strict architecture.

## Project Status

- Built for **3440×1440** resolution (ultrawide).  
- If you use a different screen resolution, you will need to manually adjust coordinates and screen regions in the code.  
- The project is currently **on hold**. A settings file may be added in the future, but there are no current plans for updates.

## Disclaimer

This project is not guaranteed to work correctly or safely.  
It was created for personal experimentation and learning purposes.  
Using automation in games can violate their Terms of Service and may result in bans.  
**Do not use this online.** Use responsibly, preferably in single-player or sandbox environments.

## Requirements

- **Operating System:** Windows 10 or 11  
- **Python:** Version 3.10 or higher  

## Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# (Optional) Create and activate a virtual environment
python -m venv .venv
. .venv/Scripts/activate   # PowerShell: .\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the code (example)
python main.py
```

## Dependencies
Standard Libraries

These are included with Python:
import subprocess
import time
import threading
import sys

## Third-Party Libraries

Third-Party Libraries

Install these using pip:

import keyboard        # pip install keyboard
import pydirectinput   # pip install pydirectinput
import pyautogui       # pip install pyautogui

## Common Issues

Common Issues

- **Incorrect clicks:** The program is tuned for 3440×1440 resolution; coordinates must be changed for other screen sizes.

- **ImportError: **A local module may be missing or named incorrectly.

- **PermissionError:** Try running your terminal as administrator.

- **Unresponsive game:** Ensure ARK is running in windowed or borderless mode without overlays.

Testing: During testing, it achieved a success rate above 99% under controlled conditions
(single-player mode, 3440×1440 resolution, and matching in-game settings).
In most of the rare failures (roughly 9 out of 10), the issue occurred during the teleportation sequence.
When this happens, it automatically skips the affected station and continues its route to the next one.

## License: MIT
You may freely use, modify, and share this code with proper attribution.

## Disclaimer
This project is for educational and experimental purposes only.
It is not intended for use in online or competitive environments.
The author is not responsible for any misuse or violation of third-party terms of service.

## The Future
If I find the time in the future, I plan to clean up the code and possibly build a simple GUI for easier control and configuration.

