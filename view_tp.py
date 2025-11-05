# correct_view.py
# Används för att automatiskt justera riktning efter teleportering enligt tidigare kalibrering

# correct_view.py
# Används för att automatiskt justera riktning efter teleportering enligt tidigare kalibrering

import json
import pyperclip
import pydirectinput
import time
import os
import correct_view
import re

SETTINGS_FILE = "rotation_settings.json"

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        print("❌ rotation_settings.json saknas. Kör calibrate_rotation.py först.")
        exit(1)
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)

def get_yaw_pitch_from_ccc():
    pydirectinput.press('f1')
    time.sleep(0.025)
    pydirectinput.PAUSE = 0
    pydirectinput.write('ccc')
    pydirectinput.PAUSE = 0.1
    time.sleep(0.025)
    pydirectinput.press('enter')
    time.sleep(0.025)

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


def tp_view(max_attempts=5, tolerance_yaw=5.0, tolerance_pitch=2.5):
    settings = load_settings()

    print("♻️ Nollställer vy till standard (0,0)")
    # correct_view.adjust_view()
    # time.sleep(0.1)

    pixels_per_yaw = settings["pixels_per_yaw"]
    pixels_per_pitch = settings["pixels_per_pitch"]
    tp_yaw = settings["tp_yaw"]
    tp_pitch = settings["tp_pitch"]

    for attempt in range(max_attempts):
        print(f"👁️ Försök {attempt + 1} att rikta kameran mot teleportern...")

        current_yaw, current_pitch = get_yaw_pitch_from_ccc()
        if current_yaw is None or current_pitch is None:
            print("❌ Avbryter – kunde inte läsa yaw/pitch.")
            return False

        # ✅ Tidig exit om riktning redan är inom tolerans
        yaw_diff = abs((current_yaw - tp_yaw + 180) % 360 - 180)
        pitch_diff = abs(current_pitch - tp_pitch)

        if yaw_diff <= tolerance_yaw and pitch_diff <= tolerance_pitch:
            print("✅ Riktning redan korrekt – ingen justering behövs.")
            return True

        # Räkna skillnader
        delta_yaw = tp_yaw - current_yaw
        delta_yaw = (delta_yaw + 180) % 360 - 180  # Wrap runt 360
        delta_pitch = tp_pitch - current_pitch

        # Om pitch är för nära men låg – tvinga nersvaj
        y_pixels = int(delta_pitch * pixels_per_pitch)
        if abs(y_pixels) < 10 and delta_pitch < -2:
            y_pixels = -50

        x_pixels = int(delta_yaw * pixels_per_yaw)

        print(f"↪️ Flyttar mus x={x_pixels}, y={y_pixels}")
        pydirectinput.moveRel(x_pixels, y_pixels, duration=0.1)
        pydirectinput.moveRel(0, 1)  # liten musrörelse för att trigga update
        time.sleep(0.1)

        # Verifiera om justering lyckades
        new_yaw, new_pitch = get_yaw_pitch_from_ccc()
        if new_yaw is None or new_pitch is None:
            continue

        yaw_diff = abs((new_yaw - tp_yaw + 180) % 360 - 180)
        pitch_diff = abs(new_pitch - tp_pitch)

        print(f"🔍 Efter justering: yaw_diff={yaw_diff:.2f}, pitch_diff={pitch_diff:.2f}")

        if yaw_diff <= tolerance_yaw and pitch_diff <= tolerance_pitch:
            print("✅ Riktning mot TP korrekt.")
            return True

    print("🛑 Misslyckades rikta kameran korrekt efter flera försök.")

    # 🔧 Sista nödförsök att trycka ner kameran till rätt pitch
    if tp_pitch <= -80:
        print("⚠️ Tvingar pitch nedåt sista försök...")

        for _ in range(6):
            pydirectinput.moveRel(0, 25)
            time.sleep(0.05)
            _, forced_pitch = get_yaw_pitch_from_ccc()
            if forced_pitch is None:
                continue
            pitch_diff = abs(forced_pitch - tp_pitch)
            if pitch_diff <= tolerance_pitch:
                print("✅ Fick till rätt pitch efter tvång!")
                return True

    return False














"""
    for attempt in range(max_attempts):
        print(f"👁️ Försök {attempt + 1} att rikta kameran mot teleportern...")

        current_yaw, current_pitch = get_yaw_pitch_from_ccc()
        if current_yaw is None or current_pitch is None:
            print("❌ Avbryter – kunde inte läsa yaw/pitch.")
            return False

        # Räkna skillnad i yaw
        delta_yaw = tp_yaw - current_yaw
        delta_yaw = (delta_yaw + 180) % 360 - 180  # Wrap runt 360

        # Räkna skillnad i pitch
        delta_pitch = tp_pitch - current_pitch

        # Om vi är nära men pitch saknas: tvinga kraftig nedjustering
        y_pixels = int(delta_pitch * pixels_per_pitch)
        if abs(y_pixels) < 10 and delta_pitch < -2:
            y_pixels = -50  # Tvinga nersvaj

        x_pixels = int(delta_yaw * pixels_per_yaw)

        print(f"↪️ Flyttar mus x={x_pixels}, y={y_pixels}")
        pydirectinput.moveRel(x_pixels, y_pixels, duration=0.1)
        pydirectinput.moveRel(0,1)   # justerar med 0.04
        time.sleep(0.1)

        # Verifiera om justering lyckades
        new_yaw, new_pitch = get_yaw_pitch_from_ccc()
        if new_yaw is None or new_pitch is None:
            continue

        yaw_diff = abs((new_yaw - tp_yaw + 180) % 360 - 180)
        pitch_diff = abs(new_pitch - tp_pitch)

        print(f"🔍 Efter justering: yaw_diff={yaw_diff:.2f}, pitch_diff={pitch_diff:.2f}")

        if yaw_diff <= tolerance_yaw and pitch_diff <= tolerance_pitch:
            print("✅ Riktning mot TP korrekt.")
            return True

    print("🛑 Misslyckades rikta kameran korrekt efter flera försök.")

    # 🔧 Sista nödförsök att trycka ner kameran till rätt pitch
    if tp_pitch <= -80:
        print("⚠️ Tvingar pitch nedåt sista försök...")

        for _ in range(6):
            pydirectinput.moveRel(0, 25)  # kraftig nersvaj
            time.sleep(0.05)
            _, forced_pitch = get_yaw_pitch_from_ccc()
            if forced_pitch is None:
                continue
            pitch_diff = abs(forced_pitch - tp_pitch)
            if pitch_diff <= tolerance_pitch:
                print("✅ Fick till rätt pitch efter tvång!")
                return True

    return False
  
"""


"""
def tp_view(max_attempts=5, tolerance_yaw=5.0, tolerance_pitch=2.5):
    settings = load_settings()

    print("♻️ Nollställer vy till 0,0")
    correct_view.adjust_view()
    time.sleep(0.3)

    pixels_per_yaw = settings["pixels_per_yaw"]
    pixels_per_pitch = settings["pixels_per_pitch"]
    tp_yaw = settings["tp_yaw"]
    tp_pitch = settings["tp_pitch"]

    for attempt in range(max_attempts):

        time.sleep(0.5)
        print(f"👁️ Försök {attempt + 1} att rikta kameran mot teleportern...")

        current_yaw, current_pitch = get_yaw_pitch_from_ccc()
        if current_yaw is None or current_pitch is None:
            print("❌ Avbryter – kunde inte läsa yaw/pitch.")
            return False

        delta_yaw = tp_yaw - current_yaw
        if delta_yaw > 180:
            delta_yaw -= 360
        elif delta_yaw < -180:
            delta_yaw += 360

        delta_pitch = tp_pitch - current_pitch

        x_pixels = int(delta_yaw * pixels_per_yaw)
        y_pixels = int(delta_pitch * pixels_per_pitch)

        print(f"↪️ Flyttar mus x={x_pixels}, y={y_pixels}")
        pydirectinput.moveRel(x_pixels, y_pixels, duration=0.3)
        time.sleep(0.1)

        # Kontrollera efter justering
        new_yaw, new_pitch = get_yaw_pitch_from_ccc()
        if new_yaw is None or new_pitch is None:
            continue

        yaw_diff = abs((new_yaw - tp_yaw + 180) % 360 - 180)
        pitch_diff = abs(new_pitch - tp_pitch)

        if yaw_diff <= tolerance_yaw and pitch_diff <= tolerance_pitch:
            print("✅ Riktning mot TP korrekt.")
            return True
        else:
            print(f"❌ Fortfarande fel vinkel (yaw_diff={yaw_diff:.2f}, pitch_diff={pitch_diff:.2f})")

    print("🛑 Misslyckades rikta kameran korrekt efter flera försök.")
    return False

"""