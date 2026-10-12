import pyautogui as pg
import navigation as nav
import time
import pytesseract
from pathlib import Path

SCREENSHOT_DIR = Path(__file__).resolve().parent / "screenshots"

# VALUES MAY NEED TO BE REALIGNED
def monkey_type(iterations: int = 1, remove_uppercase: bool = False, debug_output: bool = False):
    left = 108
    top = 520
    width = 1600
    height = 160
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    for i in range(iterations):
        if i >= 1: # Adjust the capture window height
            top = 575
            height = 100
        im = pg.screenshot(region=(left, top, width, height))
        im.save(SCREENSHOT_DIR / f"text{i}.png")
        extracted_text = pytesseract.image_to_string(im)
        clean_text = extracted_text.replace('\n', ' ')
        if remove_uppercase:
            clean_text = clean_text.lower()
        if debug_output:
            print(clean_text)
        pg.write(clean_text, interval=0.0057)


nav.nav_to_app("Chrome")
time.sleep(0.25)
monkey_type(2, remove_uppercase=True, debug_output=True)
# Iterations: 
# 1 for 25 words or less
# 2 for 50 words
# 3 for 100 words
# Unknown for time based