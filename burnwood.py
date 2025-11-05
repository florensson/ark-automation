import time
import pydirectinput
import meny_handler
import safe
import correct_view
import ocr_utils
from screen_verify import ImageVerifier as IV
from teleport_2 import teleport_to
from teleport_2 import fast_teleport_r




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

def char_from_indy():
    meny_handler.open_meny_f()
    meny_handler.search_in_dino_inventory("h")
    meny_handler.transfer_all_dino()
    meny_handler.close_meny()


def clean_invetory():
    meny_handler.open_player_inventory()
    meny_handler.drop_all_player()
    meny_handler.close_meny()

def wood_back_in_dedi():
    time.sleep(1)
    teleport_to("arbwood drop")
    time.sleep(1)
    pydirectinput.press('e')
    time.sleep(1)

def wood_for_dedi():
    meny_handler.open_meny_f()
    meny_handler.transfer_all_dino()
    meny_handler.close_meny()

skip_list = []
forge_list_full = [f"arbforge {i:02}" for i in range(1, 10) if i not in skip_list]
forge_list = [f"arbforge {i:02}" for i in range(1, 4) if i not in skip_list]
forge_list_4_6 = [f"arbforge {i:02}" for i in range(4, 7) if i not in skip_list]
forge_list_7_10 = [f"arbforge {i:02}" for i in range(7, 10) if i not in skip_list]

# Empty part
def wood_forge():
    
    for forge_name in forge_list_full:
        for n in range(1,3): # Two times per forge, cant take all in one go
            teleport_to(forge_name)

            # take char from industrialforges
            char_from_indy()

            fast_teleport_r()

            # Drop res in dedi
            dedi_drop_3x1()

    # clean the inventory before refill
    clean_invetory()

    ###### refill wood in forges 1-3 #####
    
    teleport_to("arbwood drop")
    
    wood_for_dedi()

    for forge_name in forge_list:
        teleport_to(forge_name)
        meny_handler.open_meny_f()
        meny_handler.transfer_all_player()
        meny_handler.close_meny()



    ###### refill wood in forges 4-6 #####
    time.sleep(1)

    # put wood left back in dedi
    wood_back_in_dedi()

    wood_for_dedi()

    for forge_name in forge_list_4_6:
        teleport_to(forge_name)
        meny_handler.open_meny_f()
        meny_handler.transfer_all_player()
        meny_handler.close_meny()

    # put wood left back in dedi
    wood_back_in_dedi()

    ###### refill wood in forges 7-9 #####
    
    wood_for_dedi()

    for forge_names in forge_list_7_10:
        teleport_to(forge_names)
        meny_handler.open_meny_f()
        meny_handler.transfer_all_player()
        meny_handler.close_meny()

    # put wood left back in dedi
    wood_back_in_dedi()

    #clean inventory before next task
    clean_invetory()





#teleport.teleport_to("ARBWOOD DROP")




