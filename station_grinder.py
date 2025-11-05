import pydirectinput
import time
import meny_handler
import teleport
import movement
import correct_view
# import view_grind


def gacha_grind():
    #### Turn to the grinder -50
    #view_grind.grind_view()
    correct_view.adjust_view()
    time.sleep(0.5)
    pydirectinput.moveRel(500, 0)

    ### open the grinder 
    meny_handler.open_meny_f()

    #transfer all to grinder
    meny_handler.transfer_all_player()

    # grind all
    pydirectinput.moveTo(1714, 1109)    # Grind button
    time.sleep(0.6)
    pydirectinput.click()
    time.sleep(0.6)

    #transfer all from grinder
    meny_handler.transfer_all_dino()

    meny_handler.close_meny()

    # Turn to deadi for grind mats (Works)
    time.sleep(0.4)

    correct_view.adjust_view()

    ### lägg in allt som är grind i dedis

    #### Lämnar av allt i dedi
    movement.dedi_3x3_dump()
    pydirectinput.keyUp('e')

    #standard views
    correct_view.adjust_view()

    #open inventory
    meny_handler.open_player_inventory()

    # dumpa allt skit så boten är ren
    meny_handler.drop_all_player()

    #stäng meny
    meny_handler.close_meny()

