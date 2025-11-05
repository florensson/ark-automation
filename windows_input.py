# windows_input.py
import ctypes
from ctypes import wintypes

# Fönster: Fullskärm eller borderless
hwnd = ctypes.windll.user32.FindWindowW(None, "ArkAscended")

# Konstanter
INPUT_MOUSE = 0
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_MOVE_NOCOALESCE = 0x2000

# Musrörelse-struktur
class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ("dx", wintypes.LONG),
        ("dy", wintypes.LONG),
        ("mouseData", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", wintypes.ULONG),
    ]

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = [("mi", MOUSEINPUT)]

    _anonymous_ = ("_input",)
    _fields_ = [
        ("type", wintypes.DWORD),
        ("_input", _INPUT),
    ]

# Justera efter din muskänslighet och FOV (hårdkodat först)
PIXELS_PER_DEGREE = 1.43  # Justerat för 90 FOV och sens 1.0

def turn(x: int, y: int):
    dx = int(x * PIXELS_PER_DEGREE)
    dy = int(y * PIXELS_PER_DEGREE)

    input_event = INPUT(type=INPUT_MOUSE)
    input_event.mi = MOUSEINPUT(
        dx=dx,
        dy=dy,
        mouseData=0,
        dwFlags=MOUSEEVENTF_MOVE | MOUSEEVENTF_MOVE_NOCOALESCE,
        time=0,
        dwExtraInfo=0,
    )

    ctypes.windll.user32.SendInput(1, ctypes.byref(input_event), ctypes.sizeof(INPUT))
