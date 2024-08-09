import pyautogui
import time
import subprocess
import keyboard
from PIL import ImageGrab


# Função para verificar se a tecla ESC foi pressionada e encerrar o script
def check_cancel():
    if keyboard.is_pressed('esc'):
        print("Script cancelado pelo usuário.")
        exit()


# Função para verificar a cor de um pixel na tela
def check_pixel_color(x, y, rgb_color):
    # Captura uma pequena região ao redor do pixel
    screenshot = ImageGrab.grab(bbox=(x - 1, y - 1, x + 1, y + 1))
    pixel_color = screenshot.getpixel((1, 1))
    return pixel_color == rgb_color


# Abrir o Google Chrome
subprocess.Popen("C:/Program Files/Google/Chrome/Application/chrome.exe")
time.sleep(0.7)
check_cancel()  # Verifica se o usuário pressionou ESC

# Colocar o Chrome em tela cheia clicando no botão de maximizar
pyautogui.moveTo(1513, 53)  # Coordenadas para o botão de maximizar
pyautogui.click()
time.sleep(0.7)
check_cancel()

# Acessar o perfil 'Vinícius Andrade'
pyautogui.moveTo(1185, 669)  # Coordenadas para o ícone do perfil
pyautogui.click()
time.sleep(0.7)  # Reduzi o tempo de espera após clicar no perfil
check_cancel()

# Acessar os favoritos
pyautogui.hotkey('ctrl', 'shift', 'o')
time.sleep(0.7)  # Reduzi o tempo de espera após acessar os favoritos
check_cancel()

# Coordenadas para a área onde verificar a cor
x, y = 1677, 283  # Alterar para a coordenada relevante

while True:
    check_cancel()

    # Clicar nos três pontinhos do item
    pyautogui.moveTo(x, y)  # Coordenadas para os três pontinhos
    if check_pixel_color(x, y, (32, 33, 36)):
        print("Todos os favoritos foram eliminados.")
        exit()
    pyautogui.click()
    time.sleep(0.2)  # Ajuste de tempo para garantir a execução correta

    # Clicar em 'Eliminar'
    pyautogui.moveTo(x, y + 60)  # Coordenadas para o botão 'Eliminar'
    pyautogui.click()
    time.sleep(0.2)  # Ajuste de tempo para garantir a execução correta
