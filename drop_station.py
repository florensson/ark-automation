import pydirectinput
import time
import meny_handler
import teleport
import movement
import correct_view
from screenshot_utils import third_person_scr

def gacha_drop():
    arr_tokeep1 = ["fabricated","pump","assault","riot"]
    arr_tokeep2 = ["fabricated","pump","assault","riot"]
    time.sleep(1)

    ##### öppna kristaller och göra alla drops
    meny_handler.open_hotbar()

    correct_view.adjust_view()

    time.sleep(0.2)

    #### Lämnar av allt i dedi
    movement.dedi_3x3_dump()

    time.sleep(0.2)

    # back to standard looking
    correct_view.adjust_view()

    time.sleep(0.2)

    ### Vänder sig mot vault och släpper all rito gear i vaut 1

    pydirectinput.moveRel(-500, 0)

    #open inventory vault
    meny_handler.open_meny_f()


    meny_handler.vault_drop(arr_tokeep1) # Drop ["fabricated","pump","assault","riot"] in vault


    # Vänder sig mot vault och släpper all rito gear i vaut 2

    ### Vänder sig mot vault och släpper all rito gear i vaut 1
    time.sleep(0.6)
    pydirectinput.moveRel(1000, 0)

    #open inventory vault
    meny_handler.open_meny_f()

    meny_handler.vault_drop(arr_tokeep2) # ["cliff","tree","behe"]

    # back to standard looking6
    correct_view.adjust_view()

    third_person_scr(folder_name="drop",prefix="Drop")

    teleport.fast_teleport_r()

    """ %%%%%%%%%%%%%%%%% Extra part %%%%%%%%%%%%%%%%%%%%% """

    time.sleep(0.2)

    correct_view.adjust_view()

    #### Lämnar av allt i dedi
    movement.dedi_3x3_dump()

    time.sleep(0.2)

    # back to standard looking
    correct_view.adjust_view()

    third_person_scr(folder_name="drop",prefix="Extra")

    ########## drop wood ############# new 2025-08-31

    teleport.fast_teleport_r()

    correct_view.adjust_view()
    movement.dedi_drop_3x1()
    correct_view.adjust_view()

