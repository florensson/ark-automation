import time
import pydirectinput
import meny_handler
import safe
import correct_view
import ocr_utils
from screenshot_utils import take_screenshot

"""
look at pego, open inventory, take all crystals, close inventory
"""

region_weight = (1765, 835, 59, 250)
region_peggo_name = (1596, 252, 92, 25)


def log_peggo_ocr():
    name = ocr_utils.read_text_from_region(region_peggo_name)
    value = ocr_utils.read_text_from_region(region_weight)
    
    if value is None:
        print("⚠️ Could not read weight")
    elif name is None:
        print(f"⚠️ Could not read Peggo name, weight: {value}")
    else:
        print(f"[WEIGHT] {name}: {value}")

def log_weight():
    value = ocr_utils.read_text_from_region(region_weight)
    if value is None:
        print("⚠️ Could not read value for peggo")
    else:
        print(f"Peggo weight is ({value})")




def empty_pego():
    start_timer = time.time()       # time test start

    pydirectinput.moveRel(0,-100)   # peggos are a bit up so need to look up to access the pego
    time.sleep(0.2)       
    meny_handler.open_meny_f()      # open pego inventory
    
    #start_timer2 = time.time()
    success = safe.is_it_ready_pic("inventory",confidence=0.70, retries=25, delay=0.03)
    #end_timer = time.time()

    #print(f"Peggo open inventroy time: {end_timer - start_timer:.2f} sec")

    if not success:  # if the invetory is not open, try once more
        correct_view.adjust_view()
        pydirectinput.moveRel(0,100)
        time.sleep(0.2)
        meny_handler.open_meny_f()
        log_peggo_ocr()
        take_screenshot(folder_name="pego",prefix="pego")
        meny_handler.transfer_all_dino()
        meny_handler.close_meny()
    if success:
        log_peggo_ocr()
        take_screenshot(folder_name="pego",prefix="pego")   
        meny_handler.transfer_all_dino()
        meny_handler.close_meny()
    else:
        print("❌ Inventory öppnades inte – pego misslyckades")
    
    time.sleep(0.2)


    end_timer = time.time()
    print(f"Peggo station time: {end_timer - start_timer:.2f} sec")




