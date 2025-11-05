import time
import pydirectinput
import meny_handler
import safe
import state
fastmenu = meny_handler.MenuNoDelay()
#500 är ungefär kvart varv

gacha_invetory = "inventory"

def gacha_right():
    start = time.time()
    time.sleep(0.2)
    pydirectinput.moveRel(200, 0)               # Move cam 200 pix to rigth
    time.sleep(0.2)

    fastmenu.open_meny_f_no_delay_before()                      # open inventory

    if safe.is_it_ready_pic(gacha_invetory):
        
        fastmenu.sort_in_dino_invetory("pe")        # Search for the item
        fastmenu.transfer_all_dino()
        fastmenu.sort_in_dino_invetory("pe")
        fastmenu.drop_all_dino()
        fastmenu.sort_in_dino_invetory("seed")
        fastmenu.transfer_all_dino()
        fastmenu.sort_in_dino_invetory("seed")
        fastmenu.drop_all_dino()
        #meny_handler.drop_loop_dino(15)            # Drop 15 pellets

        fastmenu.sort_in_player_inventory("seed")
        fastmenu.transfer_all_player()
        fastmenu.sort_in_player_inventory("pe")
        fastmenu.transfer_all_player()

        fastmenu.drop_all_player()                 # drop and clean out player inventory

        fastmenu.close_meny()
        time.sleep(0.3)
    else:
        print(f"Kunde inte bekräfta gacha-inventory {state.last_tp_used}")

    ### center the cam, raw
    pydirectinput.moveRel(-200, 0)
    end = time.time()
    diff = end - start
    print(f"Gacha took: {diff}")


def gacha_left():
    start = time.time()
    time.sleep(0.1)
    pydirectinput.moveRel(-200, 0)               # Move cam 200 pix to rigth
    time.sleep(0.1)

    fastmenu.open_meny_f_no_delay_before() # open inventory


    if safe.is_it_ready_pic(gacha_invetory):

        fastmenu.sort_in_dino_invetory("pe")        # Search for the item
        fastmenu.transfer_all_dino()
        fastmenu.sort_in_dino_invetory("pe")
        fastmenu.drop_all_dino()
        fastmenu.sort_in_dino_invetory("seed")
        fastmenu.transfer_all_dino()
        fastmenu.sort_in_dino_invetory("seed")
        fastmenu.drop_all_dino()
        #meny_handler.drop_loop_dino(15)            # Drop 15 pellets

        fastmenu.sort_in_player_inventory("seed")
        fastmenu.transfer_all_player()
        fastmenu.sort_in_player_inventory("pe")
        fastmenu.transfer_all_player()

        fastmenu.drop_all_player()

                  # drop and clean out player inventory

        fastmenu.close_meny()
        time.sleep(0.3)
    else:
        print(f"Kunde inte bekräfta gacha-inventory {state.last_tp_used}")

    ### center the cam, raw
    pydirectinput.moveRel(200, 0)
    end = time.time()
    diff = end - start
    print(f"Gacha took: {diff}")

