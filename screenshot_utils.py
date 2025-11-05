import mss
import mss.tools
import time
import os
from datetime import datetime
import pyautogui
from settings import BASE_DELAY
import correct_view

def take_screenshot(folder_name="screens",prefix=""):
    """
    Take scr and save in the given subfolder with timestamp

    :param folder_name: Name on the folder where scr will be save
    :param prefix: Name of the station name/area or action
    :return: Full path to the save picture
    """

    # create folder if needed
    os.makedirs(folder_name, exist_ok=True)

    # Timestamp in format: 2025-06-28_14-37-22
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{prefix}_{timestamp}.png" if prefix else f"{timestamp}.png"
    filepath = os.path.join(folder_name,filename)


    with mss.mss() as sct:
        monitor = sct.monitors[1]  # hela primära skärmen
        screenshot = sct.grab(monitor)
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=filepath)

    print(f"Scr saved to: {filepath}")
    return filepath


def third_person_scr(folder_name="screens",prefix=""):
    time.sleep(BASE_DELAY*0.5)
    pyautogui.scroll(-1)
    time.sleep(BASE_DELAY*0.5)
    take_screenshot(folder_name=folder_name,prefix=prefix)
    time.sleep(BASE_DELAY*0.5)
    pyautogui.scroll(1)
    time.sleep(BASE_DELAY*0.5)
    pyautogui.scroll(1)
    time.sleep(BASE_DELAY*0.5)




