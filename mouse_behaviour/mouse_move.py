import pyautogui
import time
import random


def mouse_click():
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    pyautogui.click(x, y)

    localtime = time.localtime()
    timestamp = time.strftime("%I:%M:%S %p", localtime)
    print(
        f' mouse click at Zeit/Koordinaten: {str(timestamp)} / ({str(x)},{str(y)}) ')


def right_mouse_click():
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    pyautogui.click(x, y, button='right')
    pyautogui.keyDown('esc')

    localtime = time.localtime()
    timestamp = time.strftime("%I:%M:%S %p", localtime)
    print(
        f' right mouse click at Zeit/Koordinaten: {str(timestamp)} / ({str(x)},{str(y)}) ')


def mouse_move():
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    pyautogui.moveTo(x, y)

    localtime = time.localtime()
    timestamp = time.strftime("%I:%M:%S %p", localtime)
    print(f'Zeit/Koordinaten: {str(timestamp)} / ({str(x)},{str(y)}) ')


def infinite_mouse_move():
    while True:
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        pyautogui.moveTo(x, y)

        localtime = time.localtime()
        timestamp = time.strftime("%I:%M:%S %p", localtime)

        print(f'Zeit/Koordinaten: {str(timestamp)} / ({str(x)},{str(y)}) ')
        time.sleep(2)
