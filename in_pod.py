import pydirectinput
import pyperclip
import time
import movement

# Allowed posistion to try to use the e wheel meny to get in bed
ALLOWED_POSITION = [189076, 350501, -45267]     # Pushout value
ALLOWED_YAW = -141.00                           # Pushout angel lookin at bed
ALLOWED_PITCH = 0.00
TOLERANCE = 20  # defoult tolerance

### Get all the ccc values in x, y, z, yaw, pitch
def get_ccc_values():
    pydirectinput.press('f1')
    time.sleep(0.2)
    pydirectinput.write('ccc')
    pydirectinput.press('enter')

    raw = pyperclip.paste().strip()
    parts = raw.split()
    try:
        x = int(float(parts[0]))
        y = int(float(parts[1]))
        z = int(float(parts[2]))
        yaw = float(parts[3])
        pitch = float(parts[4])
        return [x, y, z, yaw, pitch]
    except Exception as e:
        print("Kunde inte läsa clipboard:", e)
        print("Innehåll:", raw)
        return None

### Tolerance checker
def is_within_tolerance(value1, value2, tolerance):
    return abs(value1 - value2) <= tolerance        # if diff smaller then tolerance

def safe_press_e_only_if_correct():
    vals = get_ccc_values()
    if vals is None:
        print("Kunde inte hämta ccc-värden.")
        return

    x, y, z, yaw, pitch = vals
    pos_ok = (
    is_within_tolerance(x, ALLOWED_POSITION[0], 150) and    # Error in x
    is_within_tolerance(y, ALLOWED_POSITION[1], 100) and    # Error in y
    is_within_tolerance(z, ALLOWED_POSITION[2], 20))        # Error in z

    yaw_ok = is_within_tolerance(yaw, ALLOWED_YAW, TOLERANCE)
    pitch_ok = is_within_tolerance(pitch, ALLOWED_PITCH, TOLERANCE)

    if pos_ok and yaw_ok and pitch_ok:
        print(f"Position & riktning okej: ({x}, {y}, {z}) / yaw={yaw}, pitch={pitch}")
        movement.get_in_pod()                # us the meny to lay in bed
    else:
        print(f"Felaktig plats/riktning → Avbryter E-interaktion")
        print(f"Nuvarande: ({x}, {y}, {z}) / yaw={yaw}, pitch={pitch}")




