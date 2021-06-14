import pyautogui
import time
import os
import shutil
import keyboard
from datetime import datetime
from PIL import Image, ImageGrab

saves = "/Users/hi/Library/Application Support/minecraft/saves/"
delay = 0.1 
pyautogui.PAUSE = 0

def createWorld():
    for folder in os.listdir(saves):
        if folder[0] != '_':
            shutil.move(saves+folder, saves+"_oldWorlds/"+str(datetime.now()))
    pyautogui.press('\t')
    pyautogui.press('enter')
    time.sleep(delay)
    pyautogui.press('\t')
    pyautogui.press('\t')
    pyautogui.press('\t')
    pyautogui.press('enter')
    time.sleep(delay)
    pyautogui.press('\t')
    pyautogui.press('\t')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('\t')
    pyautogui.press('\t')
    pyautogui.press('\t')
    pyautogui.press('\t')
    pyautogui.press('\t')
    time.sleep(delay)
    pyautogui.press('enter')

def exitWorld():
    pyautogui.press('esc')
    pyautogui.keyDown('shift')
    pyautogui.press('tab')
    pyautogui.keyUp('shift')
    pyautogui.press('enter')


if __name__ == "__main__":
    print("running auto resetter...")
    print("start up a new world manually and start resetting")
    while True:
        keyboard.wait('shift+u')
        exitWorld()
        while True:
            im = ImageGrab.grab(bbox = None)
            if (im.getpixel((1334, 897)) != (113, 113, 113, 255)):
                time.sleep(delay)
            else:
                break
        createWorld()
