from PIL import ImageGrab, ImageOps     #  requires Pillow, numpy, PyAutoGUI and windows OS for ImageGrab and ImageOps
from numpy import *                     #  run the game at http://www.trex-game.skipser.com/ for reference in the same window 
import pyautogui                        #  ie have this window on the right end and the game on the left end
import time


Dinosaur = (171, 394)
restart_button = (340, 390)


def restart():
    pyautogui.click(restart_button)


def jump():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')


def grab():
    global dist
    box = (187, 394, 214, 415)
    image = ImageGrab.grab(box)
    grayscale = ImageOps.grayscale(image)
    dist = array(grayscale.getcolors())
    


def main():
    while True:
        grab()
        if dist.sum() != 814:
            jump()


restart()
main()