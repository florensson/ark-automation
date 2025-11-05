from teleport import teleport_to
import pydirectinput
import gacha
import correct_view
import movement
import in_pod
import time
import meny_handler



### Station tester, calibrate, tp to station, access both gacha ###
# station = "013" godkänd
# station = "014" godkänd
# station = "015" godkänd
# station = "16"  godkänd
# station = "17"  godkänd
# station = "18"  godkänd

def test_run_gacha():
    start = time.time()
    movement.out_of_pod()                   # out of pod
    correct_view.adjust_view()
    time.sleep(1)              # adjust the camera
    teleport_to(station)

    correct_view.adjust_view()
    time.sleep(1)
    pydirectinput.moveRel(200, 0)               # Move cam 200 pix to rigth
    time.sleep(1)
    meny_handler.open_meny_f()
    meny_handler.close_meny()

    correct_view.adjust_view()
    time.sleep(1)
    pydirectinput.moveRel(-200, 0)               # Move cam 200 pix to rigth
    time.sleep(1)
    meny_handler.open_meny_f()
    meny_handler.close_meny()

    teleport_to("gachaend")

    correct_view.adjust_view()
    in_pod.safe_press_e_only_if_correct()
    end = time.time()
    diff = end - start
    print(f"Time: {diff:.1f}")


time.sleep(3)
test_run_gacha()