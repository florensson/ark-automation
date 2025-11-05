import pydirectinput
import time




# rör spelaren lite bakåt, till för när man inte kan nå meny för tp
def step_back(duration=0.05):
    pydirectinput.keyDown('s')
    time.sleep(duration)
    pydirectinput.keyUp('s')
    time.sleep(0.2)  # liten paus så karaktären hinner stanna/stabiliseras

def dedi_drop_3x1():
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


def dedi_3x3_dump():
    import safe
    time.sleep(0.25)
    pydirectinput.moveRel(-100,-100)    # Look at dedi 1x1
    time.sleep(0.25)
    pydirectinput.press('e')
    time.sleep(0.25)
    pydirectinput.moveRel(200, 0)       # Look at dedi 1x2
    time.sleep(0.25)
    pydirectinput.press('e')
    time.sleep(0.25)
    pydirectinput.moveRel(0, 200)       # Look at dedi 2x1
    time.sleep(0.25)
    pydirectinput.press('e')
    time.sleep(0.25)
    pydirectinput.moveRel(-200, 0)      # Look at dedi 2x2
    time.sleep(0.25)
    pydirectinput.press('e')
    time.sleep(0.25)
    pydirectinput.press('c')            # Look at dedi 3x1. c movment have a longer animation
    time.sleep(0.5)
    pydirectinput.press('e')
    time.sleep(0.25)
    pydirectinput.moveRel(200 , 0)      # Look at dedi 3x2
    time.sleep(0.25)
    pydirectinput.press('e')
    time.sleep(0.25)
    pydirectinput.press('c')
    time.sleep(0.5)
    safe.are_we_crouching_hq() # check so we are standing up, if not we stand up (This have happend a few times and if we not standing we cant tp))

### Get in the pod
def get_in_pod():
    time.sleep(0.5)
    pydirectinput.keyDown('e')
    time.sleep(0.5)
    pydirectinput.moveRel(200, -200, duration=0.5)
    time.sleep(0.5)
    pydirectinput.keyUp('e')
    time.sleep(0.5)

### Get out of the tek pod
def out_of_pod():
    print("Bot is exiting the pod")
    time.sleep(1)
    pydirectinput.press('e')
    time.sleep(4)              # It sometimes lag and there is a long animation, replace with cc for faster turn
    print("out of pod done")
    #pydirectinput.moveRel(-805, 0,duration=1)
    #time.sleep(1)

### look up and rigth (Grinder)
def look_up_and_right():
    time.sleep(0.5)  # Ge dig tid att klicka in i ARK-fönstret
    pydirectinput.moveRel(0, -500)
    time.sleep(0.5)  # Flytta musen upp 500 pixlar (Denna verkar ställa till det i singel player)
    pydirectinput.moveRel(500, 0)
