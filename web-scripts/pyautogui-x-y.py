import time
import pyautogui


def monitor_mouse_position():
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Posição atual do mouse: x = {x}, y = {y}")
            time.sleep(0.3)
    except KeyboardInterrupt:
        print("Loop interrompido pelo usuário.")


monitor_mouse_position()
