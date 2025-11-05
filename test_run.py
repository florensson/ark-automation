import subprocess
import time
from teleport import teleport_to
import keyboard
import movement
import correct_view
from peggo import empty_pego
from berrystation import get_berry
import gacha
import station_grinder
import iguanodon
import pydirectinput
import drop_station
import in_pod
import logsetup
import threading
import sys
import safe
import meny_handler

target_xyz = [198380, 350550, -41483] # gacha hq pos
time.sleep(4)


def show_log():
        time.sleep(1)
        pydirectinput.press('l')
        time.sleep(2)
        meny_handler.close_meny()
        time.sleep(1)


def run_main():
    pydirectinput.keyUp('e')  # Släpp ifall e tryckts ned av något

    print("✅ Startar main.py")
    time.sleep(3)

def run(script):
    print(f"▶️ Kör {script}")
    subprocess.run(["python", script])
    time.sleep(1)


    # ### pego, drop and grind station
    # pego_list = [f"pego {i:02}" for i in range(1, 12)]

movement.out_of_pod()
correct_view.adjust_view()
"""
    movement.step_back()
    movement.step_back()


    for pego_name in pego_list:
 Testa att flyta ut ur blocket för att öka farten
        movement.out_of_pod()
        correct_view.adjust_view()
        movement.step_back()
        movement.step_back()



        teleport_to(pego_name)
        safe.is_within_bounds(target_xyz)
        correct_view.adjust_view()
        #show_log()
        pydirectinput.moveRel(0,-100)   # peggos are a bit up so need to look up to access the pego
        time.sleep(0.2)       
        meny_handler.open_meny_f()      # open pego inventory
        
        success = safe.is_it_ready_pic("inventory",confidence=0.70, retries=15, delay=0.03)
        end_timer = time.time()
        print(f"{pego_name} open inventroy")
        meny_handler.close_meny()
        correct_view.adjust_view()

    teleport_to("gachaend")
    correct_view.adjust_view()
    safe.is_within_bounds(target_xyz)
    in_pod.safe_press_e_only_if_correct() # Check cords and press e to get in pod if allowed

    time.sleep(1)
    pydirectinput.press('l')
    time.sleep(30)
    meny_handler.close_meny()
    time.sleep(1)

    ### get the berrys
    movement.out_of_pod()

"""    

gacha_list = [f"gacha {i:02}" for i in range(21, 45)]

for gacha_name in gacha_list:

    correct_view.adjust_view()

    teleport_to(gacha_name)
    correct_view.adjust_view()
    safe.is_within_bounds(target_xyz)
    time.sleep(0.2)

    pydirectinput.moveRel(-200, 0)               # Move cam 200 pix to rigth
    time.sleep(0.2)
    meny_handler.open_meny_f # open inventory
    time.sleep(0.2)
    meny_handler.close_meny()

    correct_view.adjust_view()

    pydirectinput.moveRel(200, 0)               # Move cam 200 pix to rigth
    time.sleep(0.2)
    meny_handler.open_meny_f # open inventory
    time.sleep(0.2)
    meny_handler.close_meny()


teleport_to("gachaend")
correct_view.adjust_view()
safe.is_within_bounds(target_xyz)
in_pod.safe_press_e_only_if_correct() # Check cords and press e to get in pod if allowed

time.sleep(1)
pydirectinput.press('l')
time.sleep(30)
meny_handler.close_meny()
time.sleep(1)