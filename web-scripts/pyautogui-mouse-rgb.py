import time
import pyautogui
from PIL import ImageGrab


def get_mouse_rgb():
    try:
        while True:
            x, y = pyautogui.position()
            screen = ImageGrab.grab(bbox=(x, y, x + 1, y + 1))
            color = screen.getpixel((0, 0))
            print(f"RGB na posição atual: {color}")
            time.sleep(0.3)
    except KeyboardInterrupt:
        print("Loop interrompido pelo usuário.")


get_mouse_rgb()
