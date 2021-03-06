'''
Author = xShikari - Ivan Tagle
'''

import pyautogui
import time
import argparse
from datetime import datetime, timedelta

def jump():
    end_time = datetime.now() + timedelta(seconds=3)

    while datetime.now() < end_time:
        pyautogui.press('space')


def punch():
    end_time = datetime.now() + timedelta(seconds=12)

    while datetime.now() < end_time:
        pyautogui.click()  

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--punch', action='store_true', help='Boost Bare Hands')
    parser.add_argument('-j', '--jump', action='store_true', help='Boost Jump and Run')
    args = parser.parse_args()


    try:
        if args.jump:
            print('Boosting jump in 10 secs, switch to Valheim')
            time.sleep(5)
            print('Started')
            pyautogui.keyDown('w')

            while True:
                pyautogui.keyDown('shift')
                print('Jumping')
                jump()
                print('Chillaxing')
                pyautogui.keyUp('shift')
                time.sleep(3)

        elif args.punch:
            print('Boosting bare hands in 10 secs, switch to Valheim')
            time.sleep(5)
            print('Started')
            while True:
                print('Punching')
                punch()
                print('Chillaxing')
                time.sleep(5)
        else:
            parser.print_help()

    except KeyboardInterrupt:
        print('Enjoy the boost')
