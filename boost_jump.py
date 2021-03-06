'''
Author = xShikari - Ivan Tagle
'''

import pyautogui
import time
from datetime import datetime, timedelta

def jump():
    end_time = datetime.now() + timedelta(seconds=3)

    while datetime.now() < end_time:
        pyautogui.press('shift')
        pyautogui.press('space')


print('starting in 10 secs, switch to Valheim')
time.sleep(5)
print('Started')
pyautogui.keyDown('w')
try:
    while True:
        jump()
        time.sleep(3)
except KeyboardInterrupt:          
    print('Enjoy the boost')
