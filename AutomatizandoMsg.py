import pyautogui as py
import random
import time

time.sleep(5)

msgs = ["Ta doidao", "teste", "Tudo certo", "Coe", "Eita", "Tmj", "Eh nos", "Partiu"]

for i in range(50):
    msg = random.choice(msgs)
    py.write(msg)
    py.press("enter")
