import pyautogui
import time
import re
import os



### Check pixle color for a given pix and dose loops if it takes some time
class PixelVerifier:
    # Used for checking if a menu is open and so on by pixel color
    @staticmethod
    def wait_for_pixel(x, y, expected_color, tolerance=5, max_checks=1000):         
        for _ in range(max_checks): # will run 1000 times or until its true
            if PixelVerifier.check_pixel_color(x, y, expected_color, tolerance):
                return True
        return False
    
    # Check if pix is or the given color and returns a boolean value
    @staticmethod
    def check_pixel_color(x, y, expected_color, tolerance=5):
        r, g, b = pyautogui.pixel(x, y) # Get the color of given x, y
        er, eg, eb = expected_color
        return (
            abs(r - er) <= tolerance and
            abs(g - eg) <= tolerance and
            abs(b - eb) <= tolerance
        )
    
    # Repeatedly clicks and checks pixel color until it matches or max attempts is reached
    # This is uniq for the tp list and cant be used for anythig else
    @staticmethod
    def click_until_color_matches(x, y, expected_color, tolerance=5, max_attempts=70, target_name=None):
        from meny_handler import MenuNoDelay  # local import to avoid circular import issues

        for attempt in range(max_attempts):
            print(f"🔁 Klickförsök {attempt + 1}")
            MenuNoDelay().click(x, y)

            if PixelVerifier.check_pixel_color(x, y, expected_color, tolerance):
                print("✅ Markeringsfärg bekräftad")
                return True

        print("⚠️ Pixelmatch misslyckades")

        return False   
    
    

### Check pictures on the screen
class ImageVerifier:
    # Looks all over the screen for the picture, its the slower of all checks
    @staticmethod
    def locate_image(template, confidence=0.8):
        template_path = os.path.join("pic", f"{template}.png")
        return pyautogui.locateOnScreen(template_path, confidence=confidence)

    # Used for looking for a pic in a small area of the screen, take half the time of the locate_image
    @staticmethod
    def locate_image_in_region(template, region, confidence=0.8):
        template_path = os.path.join("pic", f"{template}.png")
        try:
            return pyautogui.locateOnScreen(template_path, region=region, confidence=confidence)
        except pyautogui.ImageNotFoundException:
            return None
        
    # Loops until it finds the picture then return a value, if loop runs out and the pic is not there will return false
    @staticmethod
    def wait_until_pic_shows(template, confidence=0.8, retries=20, delay=0.1):
        template_path = os.path.join("pic", f"{template}.png")
        for attempt in range(retries):
            # time.sleep(delay)
            try:
                location = pyautogui.locateOnScreen(template_path, confidence=confidence)
                return location is not None
            except pyautogui.ImageNotFoundException:
                pass
        return False
    
    @staticmethod
    def wait_until_pic_shows_in_region(template, region, confidence=0.8, retries=20, delay=0.1):
        template_path = os.path.join("pic", f"{template}.png")
        for attempt in range(retries):
            try:
                location = pyautogui.locateOnScreen(template_path, region=region, confidence=confidence)
                if location is not None:
                    return True
            except pyautogui.ImageNotFoundException:
                pass  # Bilden hittades inte, fortsätt försöka
            time.sleep(delay)
        return False
    

class TeleportVerifier:
    @staticmethod
    def verify_tp_image(target_name, prefix, confidence=0.8):
        template = prefix + re.sub(r"\s*\d+$", "", target_name).lower()
        return ImageVerifier.wait_until_pic_shows(template, confidence=confidence)

    @staticmethod
    def verify_tp_target_image(target_name):
        return TeleportVerifier.verify_tp_image(target_name, prefix="tp_")

    @staticmethod
    def verify_travel_button_image(target_name):
        return TeleportVerifier.verify_tp_image(target_name, prefix="travel_")