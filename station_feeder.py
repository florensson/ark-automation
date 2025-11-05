### This is where we try shit out
import time
import meny_handler
import correct_view
import pydirectinput
from teleport import teleport_to

"""
This is only for feeding the owls when there is a slotcap of meat,
just lazzy
"""




time.sleep(3)

def feed_the_owls():

    NUM_STATIONS = 19

    gacha_list = [f"gacha {i:02}" for i in range(1, NUM_STATIONS + 1)]    # Add moe stations in for later


    for gacha_name in gacha_list:


        correct_view.adjust_view()                          # zero.zero the cam

        teleport_to(gacha_name)

        correct_view.adjust_view()
        pydirectinput.moveRel(-550, 220)
        meny_handler.open_meny_f()
        pydirectinput.moveTo(866, 376)

        pydirectinput.click()

        for _ in range(12):         # slotcap for 20 station
            pydirectinput.press('t')
            time.sleep(0.3)

        meny_handler.close_meny()
        correct_view.adjust_view()



feed_the_owls()

