import pydirectinput
import pyautogui
import time
import meny_handler
import pyperclip
from screen_verify import PixelVerifier
#import main
from screen_verify import ImageVerifier as IV



### Delay the click until the bot see the pic and can then use it
def is_it_ready_pic(template, confidence=0.8, retries=20, delay=0.1):
    template_path = fr"pic\{template}.png"  # f + r = funkar! formatsträng and råsträng
    for attempt in range(retries):
        time.sleep(delay)
        print(f"check for {template}:", attempt + 1)
        try:
            location = pyautogui.locateOnScreen(template_path, confidence=confidence)
            return location is not None
        except pyautogui.ImageNotFoundException:
            pass
    return False
        
### Delay the click until the bot see the pic and can then use it
def is_tp_menu_open(template_path=r"pic\tp.png", confidence=0.9, retries = 10, delay = 0.1):

    for attempt in range(retries):
        time.sleep(delay)
        print("check for menu for tp: ", attempt + 1)
        try:
            location = pyautogui.locateOnScreen(template_path, confidence=confidence)
            return location is not None
        except pyautogui.ImageNotFoundException:
            pass
    return False


def fail_safe_restart():
    print("💀 Initierar självmord och återställning...")

    meny_handler.open_player_inventory()
    time.sleep(1)
    pydirectinput.moveTo(735, 381)
    time.sleep(1)
    pydirectinput.click()
    time.sleep(7)
    pydirectinput.press('e')
    time.sleep(10)


target_xyz = [-67210, 201799, -14311]
def is_within_bounds(target_xyz, margin=40000):

    current_data = get_ccc()
    try:
        current_xyz = [float(current_data[i]) for i in range(3)]
        print(current_xyz)
    except Exception as e:
        print("❌ Kunde inte tolka koordinater:", e)
        fail_safe_restart()
        return False

    for i in range(3):
        if abs(current_xyz[i] - target_xyz[i]) > margin:
            print(f"🛑 Utanför gräns på axel {i}: {current_xyz[i]} vs {target_xyz[i]}")
            fail_safe_restart()
            return False
    print("in safe zone")
    return True


def get_ccc():
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
    print(parts)
    return parts

def are_we_crouching_hq():
    xyz = get_ccc()
    z = abs(float(xyz[2]))
    print(z)
    if z > 42900:
        time.sleep(0.2)
        pydirectinput.press('c')
        time.sleep(0.5)
    else:
        print("Standing tall")



def confirm_tp_with_tribelog(pixel_x=1325, pixel_y=403, expected_color=(0, 255, 152), tolerance=15):
    tribelog_slash = "tribelog_slash"
    count= 0

    while IV.wait_until_pic_shows_in_region(tribelog_slash, (1260, 366, 150, 150), retries=1) == False and count < 24:
        pydirectinput.press('l')
        print("Press l for tribelog")
        time.sleep(0.5)
        count += 1
    
    print("Tribelog found")
    meny_handler.close_meny()
    time.sleep(0.2)

def is_in_bed_menu(template):
    try:
        start = time.time()
        region = (676, 143, 500, 120)  # cords and how big area to look in
        template_path = fr"pic\{template}.png"
        result = pyautogui.locateOnScreen(template_path, region=region, confidence=0.8)
        end = time.time()
        print("With cords, smaller area to look in: ", result, (end - start))
        return result is not None
    except pyautogui.ImageNotFoundException:
        print("❌ locateOnScreen kastade ImageNotFoundException i sängmeny-checken")
        return False

def is_console_open():
    region = (0, 1421, 19, 19)  # justera efter var din >-prompt brukar synas
    return IV.locate_image_in_region("console_prompt", region, confidence=0.7)