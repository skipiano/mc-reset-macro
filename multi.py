import pyautogui
import time
import os
import shutil
import keyboard
from datetime import datetime, timedelta
from PIL import Image, ImageGrab
from pynput import mouse, keyboard
saves = "/Users/hi/Library/Application Support/minecraft/saves/"
saves0 = "/Users/hi/Desktop/MultiInstance/Minecraft0/saves/"
saves1 = "/Users/hi/Desktop/MultiInstance/Minecraft1/saves/"
saves2 = "/Users/hi/Desktop/MultiInstance/Minecraft2/saves/"
saves3 = "/Users/hi/Desktop/MultiInstance/Minecraft3/saves/"

delay = 0.1 
control = Controller()
timeCreated = []
worldCount = 0

def createWorld():
    for folder in os.listdir(saves0):
        if folder[0] != '_':
            shutil.move(saves0+folder, saves+"_oldWorlds/"+str(datetime.now()))
    for folder in os.listdir(saves1):
        if folder[0] != '_':
            shutil.move(saves1+folder, saves+"_oldWorlds/"+str(datetime.now()))
    for folder in os.listdir(saves2):
        if folder[0] != '_':
            shutil.move(saves2+folder, saves+"_oldWorlds/"+str(datetime.now()))
    for folder in os.listdir(saves3):
        if folder[0] != '_':
            shutil.move(saves3+folder, saves+"_oldWorlds/"+str(datetime.now()))
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

def exitWorld(paused):
    if not paused:
        control.tap('esc')
    control.press('shift')
    control.tap('tab')
    control.release('shift')
    control.tap('enter')


def resetting(paused):
    global timeCreated
    global worldCount
    exitWorld(paused)
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
    control.release('cmd')
    if len(timeCreated) < 4:
        timeCreated.append(datetime.now())
    elif datetime.now - timeCreated[worldCount % 4] > datetime.timedelta(minutes = 4):
        timeCreated[worldCount % 4] = datetime.now()
        timeCreated[(worldCount + 3) % 4] = datetime.now()
        worldCount += 1
        resetting(True)
    else:
        timeCreated[(worldCount + 3) % 4] = datetime.now()
        worldCount += 1




if __name__ == "__main__":
    print("running auto resetter...")
    print("start up a new world manually and start resetting")
    keyboard.add_hotkey('space+u', resetting(False))