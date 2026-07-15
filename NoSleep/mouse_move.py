import random
import pyautogui
import time

msg:str = "Ich codeiere"

while True:
    x = random.randrange(2000)
    y = random.randrange(1000)
    pyautogui.moveTo(x,y)
    print(msg)
    print(pyautogui.position())
    time.sleep(5)