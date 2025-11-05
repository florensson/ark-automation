import time
import pydirectinput

class MenuNoDelay:
    def __init__(self):
        self.click_delay = 0.01
        self.fast_write_delay = 0.00

    def click(self, x, y):
        pydirectinput.moveTo(x, y)
        time.sleep(self.click_delay)
        pydirectinput.click()

    def write(self, text):
        pydirectinput.PAUSE = 0
        pydirectinput.write(text, interval=self.fast_write_delay)
        pydirectinput.PAUSE = 0.1

    def sort_in_dino_invetory(self, text):
        self.click(2171, 270)
        self.write(text)

    def sort_in_player_inventory(self, text):
        self.click(802, 262)
        self.write(text)

    def click_search_bar_tp(self):
        time.sleep(0.05)
        self.click(950, 1290)
        time.sleep(0.05)

    def click_teleport_button(self):
        time.sleep(0.05)
        self.click(2625, 1300)
        time.sleep(0.05)

    def transfer_all_dino(self):
        self.click(2357, 267)    #transfer all from dino

    ### Transfer all from player to dino, accept needed
    def transfer_all_player(self):
        self.click(992, 266)      # transfer from player to dino button              
        click_accept()

    def click_accept(self):
        self.click(1588, 976)     # Accept knappen
    
    def close_meny(self):
        pydirectinput.moveTo(2840, 90)  # close menubutton
        pydirectinput.click()

    def drop_all_dino(self):
        self.click(2420, 266)             # Drop all invetory dino 
        self.click_accept()

    def drop_all_player(self):
        self.click(1057, 262)             # Drop all player
        self.click_accept()

    def open_meny_f_no_delay_before(self):
        pydirectinput.press('f')            # Open inventory for dino
        time.sleep(0.4)

    def drop_loop_player(self):
        self.click(735, 381)     # throw from topslot for player

        pydirectinput.keyDown('o')
        time.sleep(3)
        pydirectinput.keyUp('o')
        time.sleep(0.1)
        pydirectinput.keyUp('o')    # Extra up for sticky key            

    



def open_meny_f():
    time.sleep(0.4)
    pydirectinput.press('f')            # Open inventory for dino
    time.sleep(0.4)

### Close all meny
def close_meny():
    time.sleep(0.3)
    pydirectinput.moveTo(2840, 90)  # close menubutton
    time.sleep(0.3)
    pydirectinput.click()
    time.sleep(0.4)                 # close inventory

### Transfer all from dino to player, no accept needed
def transfer_all_dino():
    time.sleep(0.3)
    pydirectinput.moveTo(2357, 267)    #transfer all from dino
    time.sleep(0.32)
    pydirectinput.click()               # clicka på transfer
    time.sleep(0.3)

### Transfer all from player to dino, accept needed
def transfer_all_player():
    time.sleep(0.4)
    pydirectinput.moveTo(992, 266)      # transfer from player to dino button
    time.sleep(0.3)
    pydirectinput.click()               
    time.sleep(0.3)
    click_accept()
    time.sleep(0.4)                      # Accept function

### transfer from item from dino to player
def transfer_item_dino(item: str):
    time.sleep(0.4)
    pydirectinput.moveTo(2171, 270) # Click in the textbox of dino
    time.sleep(0.3)
    pydirectinput.click()
    search_in_dino_inventory(item)
    pydirectinput.moveTo(2358, 270)  # Transfer all button dion
    time.sleep(0.3)
    pydirectinput.click()
    time.sleep(0.4)

### denna ser inte klar ut
def drop_spec_player(item_to_drop):
    time.sleep(0.3)
    pydirectinput.press('i')            # open inventory
    time.sleep(0.3)
    pydirectinput.moveTo(833, 261)
    time.sleep(0.3)
    pydirectinput.click()
    time.sleep(0.3)

    pydirectinput.PAUSE = 0
    pydirectinput.write(item_to_drop)
    pydirectinput.PAUSE = 0.1
    time.sleep(0.5)
    click_accept()



#open all crystals from hotbar
def open_hotbar():
    pydirectinput.PAUSE = 0
    for i in range(53):
        for k in range(10):
            pydirectinput.press(str(k))
            time.sleep(0.025)
    pydirectinput.PAUSE = 0.1

def open_player_inventory():
    time.sleep(0.4) 
    pydirectinput.press('i')                    # open inventory
    time.sleep(0.2)

def drop_all_player():
    time.sleep(0.3)
    pydirectinput.moveTo(1057, 262)             # Drop all player
    time.sleep(0.3) 
    pydirectinput.click()
    click_accept()

def drop_all_dino():
    time.sleep(0.3)
    pydirectinput.moveTo(2420, 266)             # Drop all invetory dino
    time.sleep(0.3) 
    pydirectinput.click()
    click_accept()

def click_accept():
    time.sleep(0.3)
    pydirectinput.moveTo(1588, 976)     # Accept knappen
    time.sleep(0.3)
    pydirectinput.click()               # Click the accept button
    time.sleep(0.4)

### drop item from dino inventory on at the time, set amount
def drop_loop_dino(amount):
    time.sleep(0.3)
    pydirectinput.moveTo(2105, 376)     # throw from topslot för dino
    time.sleep(0.4)
    pydirectinput.click()
    time.sleep(0.4)

    for i in range(amount):             # tryck på o 15 gånger
        pydirectinput.press('o')
        time.sleep(0.3)                 # det går inte göra detta fortare pga av drop begränsningar
    time.sleep(0.4)

def transfer_item_loop_dino(amount):
    time.sleep(0.3)
    pydirectinput.moveTo(2105, 376)     # throw from topslot för dino
    time.sleep(0.4)
    pydirectinput.click()
    time.sleep(0.4)

    for i in range(amount):             # tryck på o 15 gånger
        pydirectinput.press('t')
        time.sleep(0.3)                 # det går inte göra detta fortare pga av drop begränsningar
    time.sleep(0.4)


### Use the searchbar
def search_in_dino_inventory(item: str):
    pydirectinput.moveTo(2160, 263)     # Tryck i sökrutan för dino
    time.sleep(0.3)
    pydirectinput.click()               # Click so we can write
    time.sleep(0.3)
    pydirectinput.PAUSE = 0
    pydirectinput.write(item)           # Type in the item
    pydirectinput.PAUSE = 0.1
    time.sleep(0.4)



def search_in_player(item: str):
    pydirectinput.moveTo(802, 262)     # Tryck i sökrutan för player
    time.sleep(0.4)
    pydirectinput.click()               # Click so we can write
    time.sleep(0.4)
    pydirectinput.PAUSE = 0
    pydirectinput.write(item)           # Type in the item
    pydirectinput.PAUSE = 0.1
    time.sleep(0.4)

### Vault droping
def vault_drop(arr):
    for name in arr:
        time.sleep(0.2)
        pydirectinput.moveTo(802, 262)     #Tryck i sökrutan
        time.sleep(0.1)
        pydirectinput.click()
        time.sleep(0.1)
        pydirectinput.PAUSE = 0
        pydirectinput.write(name)
        pydirectinput.PAUSE = 0.1
        time.sleep(0.1)
        pydirectinput.moveTo(992, 266)     # Tryck på transfer all
        time.sleep(0.1)
        pydirectinput.click()
        pydirectinput.moveTo(1588, 976)     # accept knappen
        time.sleep(0.1)
        pydirectinput.click()

    time.sleep(0.2)
    close_meny()
    time.sleep(0.2)


