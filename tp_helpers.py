import pydirectinput
import time
from settings import CLICK_DELAY

def safe_click(x, y, delay=CLICK_DELAY):
    pydirectinput.moveTo(x,y)
    time.sleep(delay)
    pydirectinput.click()

def search_bar_tp_menu(): # Click the search bar
    safe_click(950, 1290)

def search_bar_bed_menu(): # Click the search bar in TP wiew
    safe_click(703, 1286)

def click_top_tp_in_menu(): # Click the top tp in meny
    safe_click(800, 300)

def click_tp_button():      # Click to do the teleportation
    safe_click(2625, 1300)
