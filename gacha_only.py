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
time.sleep(2)


def show_log():
        time.sleep(1)
        pydirectinput.press('l')
        time.sleep(2)
        meny_handler.close_meny()
        time.sleep(1)


def run_main():
    pydirectinput.keyUp('e')  # Släpp ifall e tryckts ned av något

    print("startar main.py")
    time.sleep(3)

    def run(script):
        print(f"Kör {script}")
        subprocess.run(["python", script])
        time.sleep(1)


    movement.out_of_pod()
    correct_view.adjust_view()

    ### get the berrys (The berrys get refille from det iguanadon script now)
    """
    correct_view.adjust_view()
    teleport_to("gachaberry")
    correct_view.adjust_view()
    get_berry()
    """


    skip_list = []
    gacha_list = [f"gacha {i:02}" for i in range(1, 47) if i not in skip_list]

    for gacha_name in gacha_list:
        start = time.time()

        #correct_view.adjust_view()

        teleport_to("gachaig")
        #correct_view.adjust_view()
        safe.is_within_bounds(target_xyz)
        iguanodon.iguanodons()
        #correct_view.adjust_view()


        teleport_to(gacha_name)
        #correct_view.adjust_view()
        safe.is_within_bounds(target_xyz)
        gacha.gacha_right()
        #correct_view.adjust_view()


        teleport_to("gachaig")
        #correct_view.adjust_view()
        safe.is_within_bounds(target_xyz)
        iguanodon.iguanodons()
        #correct_view.adjust_view()


        teleport_to(gacha_name)
        #correct_view.adjust_view()
        safe.is_within_bounds(target_xyz)
        gacha.gacha_left()

        """ Testa att lyfta ner, men då finns ingen calibrering, kanske lägg kalibering med rörelse på ig stationen
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
        print("Cycle done!")

        if gacha_name == "gacha 23":
            print("Extra moment för gacha 23")

            teleport_to("gachaend")
            correct_view.adjust_view()
            safe.is_within_bounds(target_xyz)
            in_pod.safe_press_e_only_if_correct() # Check cords and press e to get in pod if allowed

            time.sleep(1)
            pydirectinput.press('l')
            time.sleep(30)
            meny_handler.close_meny()
            time.sleep(1)
            movement.out_of_pod()





    teleport_to("gachaend")
    correct_view.adjust_view()
    safe.is_within_bounds(target_xyz)
    in_pod.safe_press_e_only_if_correct() # Check cords and press e to get in pod if allowed
    time.sleep(1)
    pydirectinput.press('l')
    time.sleep(30)
    meny_handler.close_meny()
    time.sleep(1)

    

if __name__ == "__main__":
    run_main()