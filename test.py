import pyautogui
import sys
import os
import time
import random


pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

try:

  while True:
    sleep = random.randrange(60, 120)
    time.sleep(sleep)
    step = random.randrange(2)
    #if sleep % 2 == 0:
      #pyautogui.moveTo(100,100,duration=0.25)
    #pyautogui.moveTo(200,100,duration=step)
    click = random.randrange(100, 200)
    pyautogui.click(500,click)
except KeyboardInterrupt:
    print('\nDone')

