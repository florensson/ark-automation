import pyautogui
import keyboard
import findMousePos
import time
from windows_input import turn

"""
This code is only use in the setup stage, have no bot function
"""

def mouse_pos_when_push():
    print("System is waiting for user to press F to give mouse position")
    pos = pyautogui.position()
    print(f"The mosue pos is: {pos}")

mouse_pos_when_push()


def look_down_90_degrees():
    print("⏳ Tittar ner 90 grader om 3 sek...")
    time.sleep(3)
    turn(0, 90)  # 0 x-led, 90 y-led = nedåt


f2_was_pressed = True  # Starta med att låtsas att F2 är nedtryckt

print("Väntar på att F2 släpps innan start...")

# Vänta tills F2 släpps (om den är nedtryckt från början)
while keyboard.is_pressed("F2"):
    time.sleep(0.05)

f2_was_pressed = False  # Nu är vi redo

while True:
    if keyboard.is_pressed("F2") and not f2_was_pressed:
        findMousePos.mouse_pos_when_push()
        f2_was_pressed = True  # Undvik upprepning
    if not keyboard.is_pressed("F2") and f2_was_pressed:
        f2_was_pressed = False  # Släpp blockering när knappen släpps
    

    # break the loop
    if keyboard.is_pressed("F4"):
        print("Mousepos stopped by user")
        break
