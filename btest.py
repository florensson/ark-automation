import pydirectinput
import time
import correct_view

time.sleep(2)

correct_view.adjust_view()
time.sleep(0.25)
#pydirectinput.press("e")
time.sleep(0.25)


pydirectinput.moveRel(0,-200)
time.sleep(0.25)
# pydirectinput.press("e")
time.sleep(0.25)


pydirectinput.moveRel(0,500)
time.sleep(0.25)
pydirectinput.press("e")
time.sleep(0.25)