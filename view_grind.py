# correct_view.py
# Används för att automatiskt justera riktning efter teleportering enligt tidigare kalibrering

import json
import pyperclip
import pydirectinput
import time
import os

SETTINGS_FILE = "rotation_settings.json"

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        print("❌ rotation_settings.json saknas. Kör calibrate_rotation.py först.")
        exit(1)
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)

def get_yaw_pitch_from_ccc():
    pydirectinput.press('f1')
    time.sleep(0.1)
    pydirectinput.PAUSE = 0
    pydirectinput.write('ccc')
    pydirectinput.PAUSE = 0.1
    time.sleep(0.1)
    pydirectinput.press('enter')
    time.sleep(0.1)

    raw = pyperclip.paste().strip()
    parts = raw.split()
    try:
        yaw = float(parts[3])
        pitch = float(parts[4])
        return yaw, pitch
    except Exception as e:
        print("❌ Fel att läsa clipboard:", e)
        print("📋 Clipboard innehåll:", raw)
        return None, None

def grind_view():
    settings = load_settings()

    pixels_per_yaw = settings["pixels_per_yaw"]
    pixels_per_pitch = settings["pixels_per_pitch"]
    tp_yaw = settings["grind_yaw"]
    tp_pitch = settings["grind_pitch"]

    print("🔍 Kollar kamerariktning...")
    current_yaw, current_pitch = get_yaw_pitch_from_ccc()
    if current_yaw is None or current_pitch is None:
        print("❌ Avbryter justering – kunde inte läsa yaw/pitch.")
        return

    # Beräkna skillnad
    delta_yaw = tp_yaw - current_yaw
    if delta_yaw > 180:
        delta_yaw -= 360
    elif delta_yaw < -180:
        delta_yaw += 360

    delta_pitch = tp_pitch - current_pitch

    x_pixels = int(delta_yaw * pixels_per_yaw)
    y_pixels = int(delta_pitch * pixels_per_pitch)

    if abs(x_pixels) < 2 and abs(y_pixels) < 2:
        print("✅ Riktning redan korrekt – ingen justering behövs.")
        return

    print(f"↪️ Flyttar mus x={x_pixels}, y={y_pixels}")
    pydirectinput.moveRel(x_pixels, y_pixels, duration=0.3)
    time.sleep(0.4)
