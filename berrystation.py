import pydirectinput
import time
import meny_handler

### Tested and working

### Get berry from feeding troughs to player inventory
def get_berry():
    meny_handler.open_meny_f()          # Open the container with f

    meny_handler.transfer_all_dino()    # Oransfer the berry to player
    time.sleep(2)

    meny_handler.close_meny()
    time.sleep(2)


