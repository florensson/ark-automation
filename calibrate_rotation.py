# calibrate_rotation.py
# Körs en gång efter uppvaknande för att mäta hur mycket musen måste röras för att nå ett visst yaw/pitch, och justerar sedan till exakt position.

import pyperclip
import pydirectinput
import time
import json

# Önskad riktning efter uppvaknande
TARGET_YAW = -140.86
TARGET_PITCH = 0.00

# Fil för att spara kalibreringsdata
OUTPUT_FILE = "rotation_settings.json"

def get_yaw_pitch_from_clipboard():
    time.sleep(0.3)
    raw = pyperclip.paste().strip()
    parts = raw.split()
    try:
        yaw = float(parts[3])
        pitch = float(parts[4])
        return yaw, pitch
    except Exception as e:
        print(" Kunde inte läsa yaw/pitch:", e)
        return None, None

def issue_ccc():
    pydirectinput.press('f1')
    time.sleep(0.2)
    pydirectinput.write('ccc')
    time.sleep(0.1)
    pydirectinput.press('enter')
    time.sleep(0.3)
    pydirectinput.press('tab')

def adjust_view(current_yaw, current_pitch, pixels_per_yaw, pixels_per_pitch):
    # Räkna skillnad
    delta_yaw = TARGET_YAW - current_yaw
    if delta_yaw > 180:
        delta_yaw -= 360
    elif delta_yaw < -180:
        delta_yaw += 360

    delta_pitch = TARGET_PITCH - current_pitch

    # Räkna pixlar
    x_pixels = int(delta_yaw * pixels_per_yaw)
    y_pixels = int(delta_pitch * pixels_per_pitch)

    print(f"🔄 Justerar view: x={x_pixels}, y={y_pixels}")
    pydirectinput.moveRel(x_pixels, y_pixels, duration=0.4)

print(" Startar kalibrering... Stå stilla i spelet och fokusera ARK-fönstret.")
time.sleep(3)

# Steg 1: Hämta ursprunglig yaw/pitch
issue_ccc()
start_yaw, start_pitch = get_yaw_pitch_from_clipboard()
print(f" Start: yaw={start_yaw}, pitch={start_pitch}")

# Steg 2: Flytta musen horisontellt (yaw)
pixels_yaw = 200
pydirectinput.moveRel(pixels_yaw, 0, duration=0.3)
time.sleep(0.5)
issue_ccc()
new_yaw, _ = get_yaw_pitch_from_clipboard()
print(f" Ny yaw: {new_yaw}")

yaw_change = new_yaw - start_yaw
pixels_per_yaw = pixels_yaw / yaw_change if yaw_change != 0 else 0
print(f" {pixels_per_yaw:.2f} pixlar per yaw-grad")

# Steg 3: Flytta musen vertikalt (pitch)
pixels_pitch = -200
pydirectinput.moveRel(0, pixels_pitch, duration=0.3)
time.sleep(0.5)
issue_ccc()
_, new_pitch = get_yaw_pitch_from_clipboard()
print(f" Ny pitch: {new_pitch}")

pitch_change = new_pitch - start_pitch
pixels_per_pitch = pixels_pitch / pitch_change if pitch_change != 0 else 0
print(f"  {pixels_per_pitch:.2f} pixlar per pitch-grad")

# Spara till fil
settings = {
    "pixels_per_yaw": pixels_per_yaw,
    "pixels_per_pitch": pixels_per_pitch,
    "target_yaw": TARGET_YAW,
    "target_pitch": TARGET_PITCH
}

with open(OUTPUT_FILE, "w") as f:
    json.dump(settings, f, indent=2)

print(f" Kalibrering klar och sparad i {OUTPUT_FILE}")

# Steg 4: Justera till målet
issue_ccc()
current_yaw, current_pitch = get_yaw_pitch_from_clipboard()
adjust_view(current_yaw, current_pitch, pixels_per_yaw, pixels_per_pitch)

# Verifiera
time.sleep(1)
issue_ccc()
final_yaw, final_pitch = get_yaw_pitch_from_clipboard()
print(f"🔍 Efter justering: yaw={final_yaw}, pitch={final_pitch}")
