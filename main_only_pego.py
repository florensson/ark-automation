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
time.sleep(5)


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
    pego_list = [f"pego {i:02}" for i in range(1, 5)]

    for pego_name in pego_list:
        movement.out_of_pod()
        correct_view.adjust_view()
        movement.step_back()
        movement.step_back()


        teleport_to(pego_name)
        safe.is_within_bounds(target_xyz)
        correct_view.adjust_view()
        #show_log()
        empty_pego()
        correct_view.adjust_view()
        safe.is_within_bounds(target_xyz)


        teleport_to("gachadrop")
        correct_view.adjust_view()
        #show_log()
        drop_station.gacha_drop()
        safe.is_within_bounds(target_xyz)


        teleport_to("gachagrind")
        #show_log()
        station_grinder.gacha_grind()
        safe.is_within_bounds(target_xyz)


        teleport_to("gachaend")
        correct_view.adjust_view()
        safe.is_within_bounds(target_xyz)
        in_pod.safe_press_e_only_if_correct() # Check cords and press e to get in pod if allowed
        time.sleep(1)

"""


gacha_list = [f"gacha {i:02}" for i in range(16, 21)]

for gacha_name in gacha_list:

    correct_view.adjust_view()

    teleport_to("gachaig")
    correct_view.adjust_view()
    safe.is_within_bounds(target_xyz)
    #show_log()
    iguanodon.iguanodons()
    correct_view.adjust_view()


    teleport_to(gacha_name)
    correct_view.adjust_view()
    safe.is_within_bounds(target_xyz)
    gacha.gacha_right()
    correct_view.adjust_view()


    teleport_to("gachaig")
    correct_view.adjust_view()
    safe.is_within_bounds(target_xyz)
    #show_log()
    iguanodon.iguanodons()
    correct_view.adjust_view()


    teleport_to(gacha_name)
    correct_view.adjust_view()
    safe.is_within_bounds(target_xyz)
    gacha.gacha_left()
    correct_view.adjust_view()


    teleport_to("gachaend")
    correct_view.adjust_view()
    safe.is_within_bounds(target_xyz)
    in_pod.safe_press_e_only_if_correct() # Check cords and press e to get in pod if allowed
    time.sleep(1)
    pydirectinput.press('l')
    time.sleep(10)
    meny_handler.close_meny()
    time.sleep(1)
    movement.out_of_pod()
"""


run_main()
















"""

time.sleep(3)
if __name__ == "__main__":
    run_main()
"""