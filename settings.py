# settings for the bot

# BasE value for delay
BASE_DELAY = 0.5

# Derived delays
CLICK_DELAY = BASE_DELAY * 0.2          # 0.1s
TELEPORT_DELAY = BASE_DELAY * 5         # 2.5s
TP_COnFIRM_DELAY = BASE_DELAY * 10      # 5s
VIEW_ADJUST_DELAY = BASE_DELAY * 0.3    # 0.15s

# Tolerance
CCC_AREA_MARGIN = 40000                 # Covers  whale cave boundary
TARGET_XYZ = [198380, 350550, -41483]   # Center of allowed cave zone
TOLERANCE_BED = 20                      # Margin when standing at pod

# Station names
STATIONS = {
    "drop": "gachadrop",
    "grind": "gachagrind",
    "berry": "gachaberry",
    "iguanodon": "gachaig",
    "start_bed": "gachaend",
}

# Stationn list
GACHA_LIST = [f"gacha {i:02}" for i in range(1, 47)]    # Station 01-46
PEGGO_LIST = [f"pego {i:02}" for i in range(1, 20)]     # Station 01-19