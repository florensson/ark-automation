import pydirectinput
import time
import view_tp # Import our function that makes sure we are looking at the tp
import safe
import tp_helpers
import re
import state
import correct_view
import pyautogui
from screen_verify import PixelVerifier
from meny_handler import MenuNoDelay
menu = MenuNoDelay()
import meny_handler
import screen_verify

def teleport_to(target_name: str):
    start = time.time()
    correct_view.adjust_view()
    view_tp.tp_view()

    # Two move dow to be more offencive in the look down, error handel here can take alot of time
    time.sleep(0.025)
    pydirectinput.moveRel(0, 460)
    time.sleep(0.025)


    pydirectinput.press('e')
    time.sleep(0.1)

    start_check = time.time()
    if not PixelVerifier.wait_for_pixel(787, 181, (193, 245, 255), tolerance=10, max_checks=200):
        print("🔄 TP-menyn hittades inte – justerar vy")
        view_tp.tp_view()
        pydirectinput.moveRel(0, 500, duration=0.5)
        time.sleep(0.1)
        pydirectinput.press('e')
        time.sleep(0.2)

        if not PixelVerifier.wait_for_pixel(787, 181, (193, 245, 255), tolerance=5, max_checks=60):
            print("⚠️ Fortfarande ingen TP-meny – kollar sängmeny")
            if safe.is_in_bed_menu("beds"):
                print("🛏️ I sängmenyn – lämnar den")
                pydirectinput.press('esc')
                time.sleep(0.2)
                correct_view.adjust_view()
                time.sleep(0.2)
                pydirectinput.moveRel(0, 500, duration=0.5)
                time.sleep(0.2)
                pydirectinput.press('e')
                time.sleep(0.2)

                if not PixelVerifier.wait_for_pixel(787, 181, (193, 245, 255), tolerance=5, max_checks=50):
                    print("❌ Misslyckades att öppna TP-menyn efter att ha lämnat sängmenyn.")
                    return
            else:
                print("❌ Varken TP-meny eller sängmeny hittades. Avbryter.")
                return

    print("✅ TP-meny öppen")
    # print("⏱ Tid att öppna TP-meny:", time.time() - start_check)

    # Uses the no delay class to click search bar
    time.sleep(0.2)
    menu.click_search_bar_tp()

    # Write the destination
    time.sleep(0.2)
    menu.write(target_name)
    time.sleep(0.2)

    start3 = time.time()
    PixelVerifier.click_until_color_matches (1154, 272, (61, 27, 0), tolerance=10, max_attempts=70)
    end3 = time.time()
    # print("Click the disire tp in: ", (end3 - start3))
    #tp_helpers.click_top_tp_in_menu()  # Click on the target that we want (tagit bort tiden för lab)

    # Click on the teleport button 
    menu.click_teleport_button()

    start4 = time.time()
    time.sleep(0.1)
    safe.confirm_tp_with_tribelog()

    if safe.is_console_open():
        print("⌨️ Konsolen är öppen – stänger med Enter")
        pydirectinput.press('enter')
        time.sleep(0.1)

    end4 = time.time()

    # print("Open tribe log in: ", (end4 - start4))
    pydirectinput.moveRel(0, -458, duration=0.1)
    time.sleep(0.05)
    correct_view.adjust_view()
    time.sleep(0.05)

    #pydirectinput.moveRel(400,400)
    end = time.time()
    total_time = end - start
    print(f"Teleportation to {target_name}, time: {total_time}")


def fast_teleport_r():
    start = time.time()
    correct_view.adjust_view()
    time.sleep(0.1)

    pydirectinput.press('r')
    time.sleep(0.1)
    safe.confirm_tp_with_tribelog()
    time.sleep(0.1)
    end = time.time()
    print(f"Time for fast teleport: ", (end - start))
