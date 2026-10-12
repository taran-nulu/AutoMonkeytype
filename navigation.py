import pyautogui as pg
import custom_hotkey as ch

def nav_to_app(app):
    ch.custom_hotkey('command','space')
    pg.write(app)
    pg.press("enter")