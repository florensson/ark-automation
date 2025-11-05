import screen_verify


# Check if we see death sceen, works 2025-06-16
template = "death_screen"
def is_dead_screen():
    try:
        value = screen_verify.ImageVerifier.locate_image_in_region(template, (2339, 1214, 700, 200), confidence=0.8)
        return value
    except:
        return False
    
"""INFO
Death screen: 
Top right coner: (655, 136)
distens to left bottom coner: (480, 116)

### Test part
time.sleep(3)
start = time.time()
print(is_dead_screen())
end = time.time()
print(end - start)
"""