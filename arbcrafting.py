import time
import pydirectinput
import meny_handler
import safe
import correct_view
import ocr_utils
from screen_verify import ImageVerifier as IV
from teleport_2 import teleport_to
from teleport_2 import fast_teleport_r
import correct_view2



def clean_invetory():
    meny_handler.open_player_inventory()
    meny_handler.drop_all_player()
    meny_handler.close_meny()

def dedi_drop_3x1():
    time.sleep(0.5)
    correct_view.adjust_view()
    time.sleep(0.25)
    pydirectinput.press("e")
    time.sleep(0.25)

    pydirectinput.moveRel(0,-200)
    time.sleep(0.25)
    pydirectinput.press("e")
    time.sleep(0.25)

    pydirectinput.moveRel(0,500)
    time.sleep(0.25)
    pydirectinput.press("e")
    time.sleep(0.25)

    correct_view.adjust_view()

############ spark ###########

def arb_sling():
    fast_teleport_r()
    time.sleep(0.5)

    correct_view2.adjust_view()
    meny_handler.open_meny_f()
    time.sleep(0.5)
    meny_handler.search_in_dino_inventory("spark")
    pydirectinput.click(2100,376)
    for n in range(1,11):
        time.sleep(0.1)
        pydirectinput.press("a")

    # take all spark
    meny_handler.transfer_all_dino()
    meny_handler.close_meny()

    # drop of the spark in dedi
    time.sleep(0.5)
    fast_teleport_r()
    time.sleep(0.5)

    correct_view2.adjust_view() # look to the dedi

    dedi_drop_3x1()

    clean_invetory()


############ gunpowder ###########

    # Gunpowder part STATION 1

    fast_teleport_r()
    time.sleep(0.5)

    correct_view2.adjust_view()
    time.sleep(0.5)
    meny_handler.open_meny_f()
    time.sleep(0.5)
    meny_handler.search_in_dino_inventory("gun")
    pydirectinput.click(2100,376)
    for n in range(1,11):
        time.sleep(0.1)
        pydirectinput.press("a")

    # take all gun
    meny_handler.transfer_all_dino()
    meny_handler.close_meny()
    time.sleep(0.5)

    # drop of the gun in dedi

    correct_view2.adjust_view() # look to the dedi

    # Gunpowder part STATION 2

    fast_teleport_r()
    time.sleep(0.5)

    correct_view2.adjust_view()
    time.sleep(0.5)
    meny_handler.open_meny_f()
    time.sleep(0.5)
    meny_handler.search_in_dino_inventory("gun")
    pydirectinput.click(2100,376)
    for n in range(1,11):
        time.sleep(0.1)
        pydirectinput.press("a")

    # take all gun
    meny_handler.transfer_all_dino()
    meny_handler.close_meny()
    time.sleep(0.5)

    # drop of the gun in dedi
    fast_teleport_r()
    time.sleep(0.5)

    correct_view2.adjust_view() # look to the dedi

    dedi_drop_3x1()

    clean_invetory()




    ############ REPLICATOR ###########

    fast_teleport_r()
    time.sleep(0.5)

    correct_view2.adjust_view()

    meny_handler.open_meny_f()
    time.sleep(0.5)
    meny_handler.search_in_dino_inventory("advance rifle")
    pydirectinput.click(2100,376)
    for n in range(1,11):
        time.sleep(0.1)
        pydirectinput.press("a")

    # take all arb
    meny_handler.transfer_all_dino()
    meny_handler.close_meny()
    time.sleep(0.5)

    fast_teleport_r()
    time.sleep(0.5)

    correct_view2.adjust_view() # look to the dedi

    time.sleep(1)
    pydirectinput.press("e")
    time.sleep(1)

    clean_invetory()


