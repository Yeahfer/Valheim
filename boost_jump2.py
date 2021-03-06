'''
Author = xShikari - Ivan Tagle
'''

import pyautogui
import time
from datetime import datetime, timedelta

def jump():
    end_time = datetime.now() + timedelta(seconds=2)

    while datetime.now() < end_time:
        pyautogui.press('space')


print('starting in 10 secs, switch to Valheim')
time.sleep(5)
print('Started')
pyautogui.keyDown('w')

try:
    while True:
        pyautogui.keyDown('shift')
        jump()
        pyautogui.keyUp('shift')
        time.sleep(3)
except KeyboardInterrupt:
    print('Enjoy the boost')
