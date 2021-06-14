import pyautogui
import time
import os
import shutil
import keyboard
from datetime import datetime
from PIL import Image, ImageGrab
from pynput import mouse, keyboard
saves = "/Users/hi/Library/Application Support/minecraft/saves/"
saves0 = "/Users/hi/Desktop/MultiInstance/Minecraft0/saves/"
saves1 = "/Users/hi/Desktop/MultiInstance/Minecraft1/saves/"
saves2 = "/Users/hi/Desktop/MultiInstance/Minecraft2/saves/"
saves3 = "/Users/hi/Desktop/MultiInstance/Minecraft3/saves/"

delay = 0.1 
pyautogui.PAUSE = 0
control = Controller()

def createWorld():
    for folder in os.listdir(saves):
        if folder[0] != '_':
            shutil.move(saves+folder, saves+"_oldWorlds/"+str(datetime.now()))
    control.tap('tab')
    control.tap('enter')
    time.sleep(delay)
    control.tap('tab')
    control.tap('tab')
    control.tap('tab')
    control.tap('enter')
    time.sleep(delay)
    control.tap('tab')
    control.tap('tab')
    control.tap('enter')
    control.tap('enter')
    control.tap('enter')
    control.tap('tab')
    control.tap('tab')
    control.tap('tab')
    control.tap('tab')
    control.tap('tab')
    time.sleep(delay)
    control.tap('enter')

def exitWorld():
    control.tap('esc')
    control.press('shift')
    control.tap('tab')
    control.release('shift')
    control.tap('enter')


def resetting():
    exitWorld()
    while True:
        im = ImageGrab.grab(bbox = None)
        if (im.getpixel((1334, 897)) != (113, 113, 113, 255)):
            time.sleep(delay)
        else:
            break
    createWorld()
    control.press('cmd')
    control.tap('tab')
    control.tap('tab')
    control.tap('tab')


if __name__ == "__main__":
    print("running auto resetter...")
    print("start up a new world manually and start resetting")
    keyboard.add_hotkey('space+u', resetting())