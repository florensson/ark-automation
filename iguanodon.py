import time
import pydirectinput
import meny_handler
import safe
import correct_view
import ocr_utils
from screen_verify import ImageVerifier as IV
fastmenu = meny_handler.MenuNoDelay()
import berrystation
from screenshot_utils import take_screenshot

"""
This part is considered done, its not crazy fast but it has stability. The only thing we migth do if there is a need is to make a crazy fast
version that i sub 2 sec then have the big on as a fall back. time now is 7.5 sec
"""

inventory = "inventory"
ig_hud = "ig_female_infohud"
template_seed = "tinto_seed"
template_tinto = "tinto_berry"
region_weight = (1764, 835, 55, 250)

def refill_if_needed():
    meny_handler.close_meny()

    from teleport import teleport_to    #  Lokal import för att undvika cykler
    teleport_to("gachaberry")
    correct_view.adjust_view()

    meny_handler.open_meny_f()
    meny_handler.transfer_item_loop_dino(43)    #  18 stacks beroende på vikt kanske?
    meny_handler.close_meny()

    teleport_to("gachaig")
    correct_view.adjust_view()

def big_refill():
    meny_handler.close_meny()
    from teleport import teleport_to    #  Lokal import för att undvika cykler
    teleport_to("gachaberry")
    correct_view.adjust_view()

    berrystation.get_berry()

    teleport_to("gachaig")
    correct_view.adjust_view()


def not_defualt_iguanodons():
    def transfer_seeds_from_dino():
        time.sleep(0.1)
        fastmenu.sort_in_dino_invetory("seed")
        time.sleep(0.1)
        fastmenu.transfer_all_dino()
        time.sleep(0.1)
        fastmenu.close_meny()

    def transfer_back_and_forward():
        time.sleep(0.1)
        fastmenu.transfer_all_dino()
        time.sleep(0.1)
        fastmenu.transfer_all_player()
        time.sleep(0.1)
        fastmenu.close_meny()
        time.sleep(0.1)

    def try_get_seeds():
        meny_handler.open_meny_f()
        if IV.wait_until_pic_shows(inventory, confidence=0.8, retries=20, delay=0.1):
            transfer_seeds_from_dino()
            return True
        else:
            print("Kunde inte få upp inventory vid seedhämtning.")
            return False

    start = time.time()

    correct_view.adjust_view()
    time.sleep(0.2)
    meny_handler.open_meny_f()
    time.sleep(0.1)

    if IV.wait_until_pic_shows(inventory, confidence=0.8, retries=20, delay=0.1):
        transfer_back_and_forward()
    else:
        print("Kunde inte öppna inventory – försöker ändå.")
        correct_view.adjust_view()
        meny_handler.open_meny_f()
        transfer_back_and_forward()

    # Vänta på att HUD kommer tillbaka = vi är ute ur meny
    IV.wait_until_pic_shows(ig_hud, confidence=0.8, retries=20, delay=0.1)

    pydirectinput.press('e')  # skapa seeds

    # Försök att hämta seeds
    if not try_get_seeds():
        print("Försök med justerad vy...")
        correct_view.adjust_view()
        time.sleep(0.3)
        try_get_seeds()

    print(f"iguanodon time: {time.time() - start:.2f} sek")


def fail(msg):
    print("❌", msg)
    fastmenu.close_meny()
    return False


def iguanodons():
    """
    Kör iguanodon-seed-cykeln:
    - Öppnar meny
    - Tömmer och fyller om inventory
    - Trycker E för att konvertera bär till frön
    - Hämtar fröna
    - Om seeds saknas → backup-strategi
    """
    start = time.time()

    # 1. Open meny
    correct_view.adjust_view()  # adjust view
    meny_handler.open_meny_f()  # open meny

    # 2. Om meny inte öppnas – försök återställa vyn och öppna igen
    if not IV.wait_until_pic_shows("inventory", confidence=0.8, retries=10):
        print("Inventory öppnades inte – försöker titta upp och försöka igen.")
        pydirectinput.moveRel(0, -150, duration=0.2)  # Titta upp lite
        time.sleep(0.2)
        correct_view.adjust_view()
        meny_handler.open_meny_f()
        if not IV.wait_until_pic_shows("inventory", confidence=0.8, retries=10):
            return fail("Inventory öppnades inte efter fallback-försök")
    
    # 1.1 Check so we have the correct ammount of berrys
    value = ocr_utils.read_text_from_region(region_weight)
    if value is None:
        print("Kunde inte läsa av vikten – hoppar över påfyllning.")
    elif 900 < value < 1021:
        refill_if_needed()
        correct_view.adjust_view()  # adjust view
        meny_handler.open_meny_f()  # open meny
    elif value == 20.0:
        print("There is 0 berrys, need to get alot more.")
        big_refill()
        correct_view.adjust_view()  # adjust view
        meny_handler.open_meny_f()  # open meny
    else:
        print(f"Tillräcklig vikt ({value}) – ingen påfyllning.")
    
    # 2. Take all berry from dion
    time.sleep(0.1)
    fastmenu.transfer_all_dino()
    time.sleep(0.1)

    # 3. Put all back to the dino
    time.sleep(0.1)
    fastmenu.transfer_all_player()
    time.sleep(0.1)

    fastmenu.close_meny()

    # 3.1 Check so meny is close
    IV.wait_until_pic_shows(ig_hud, confidence=0.8, retries=30, delay=0.1)     # looks for the icon on iguanodon

    # 4. Press E to make seeds
    time.sleep(0.2)  # Liten buffert extra innan E
    pydirectinput.press('e')
    time.sleep(0.4)

    # 5. Open meny once more
    #meny_handler.open_meny_f()
    #if not IV.wait_until_pic_shows("inventory", confidence=0.8, retries=10):
    #    return fail("Kunde inte öppna inventory efter seed")
    for attempt in range(3):
        meny_handler.open_meny_f()
        if IV.wait_until_pic_shows("inventory", confidence=0.8, retries=10):
            break
        print(f"Försök {attempt+1} att öppna meny misslyckades – provar igen")
        time.sleep(0.5)
    else:
        return fail("Kunde inte öppna inventory efter seed")
        
    # 6. Pick out the seeds
    fastmenu.transfer_all_player()
    time.sleep(0.1)
    fastmenu.transfer_all_dino()
    time.sleep(0.1)
    fastmenu.transfer_all_player()
    time.sleep(0.1)
    fastmenu.sort_in_dino_invetory("seed")
    time.sleep(0.1)
    fastmenu.transfer_all_dino()

    fastmenu.close_meny()

    IV.wait_until_pic_shows(ig_hud, confidence=0.8, retries=30, delay=0.1)     # looks for the icon on iguanodon

    time.sleep(0.2)  #  Liten buffert extra innan E
    pydirectinput.press('e')
    time.sleep(0.4)

    for attempt in range(3):
        meny_handler.open_meny_f()
        if IV.wait_until_pic_shows("inventory", confidence=0.8, retries=10):
            break
        print(f"⚠️ Försök {attempt+1} att öppna meny misslyckades – provar igen")
        time.sleep(0.5)
    else:
        return fail("Kunde inte öppna inventory efter seed")

    fastmenu.transfer_all_player()
    time.sleep(0.1)

    fastmenu.sort_in_dino_invetory("seed")
    time.sleep(0.1)
    fastmenu.transfer_all_dino()
    time.sleep(0.1)
    fastmenu.sort_in_dino_invetory("seed")
    time.sleep(0.1)
    fastmenu.drop_all_dino()
    time.sleep(0.1)

    # 7. Check - are the seeds there?
    if IV.wait_until_pic_shows_in_region(template_seed, (789, 302, 150, 150), retries=10):
        time.sleep(0.05)

        # Printscreen to check for errors
        take_screenshot(folder_name="screens/iguanodon", prefix="seed_and_berry")

        fastmenu.close_meny()
        print(f"Seeds tagna korrekt. Tid: {time.time() - start:.2f}s")

    else:
        print("Seeds saknas – kör backup")
        # Is the berry in the inventory of the player? if so transfer them to dino
        if IV.wait_until_pic_shows_in_region(template_tinto, (789, 302, 150, 150), retries=5):
            time.sleep(0.05)

            # Printscreen to check for errors
            take_screenshot(folder_name="screens/iguanodon", prefix="seed_and_berry")

        # Close the meny to be safe
        fastmenu.close_meny()
        # Backup protocol
        not_defualt_iguanodons()



