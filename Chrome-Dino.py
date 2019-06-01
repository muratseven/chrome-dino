import time

from PIL import ImageGrab,ImageOps
import pyautogui
from numpy import *

class Cordinates():
    replayBtn = (340,390)
    dinazor= (266,426)


def Restart():
    pyautogui.click(Cordinates.replayBtn)
    pyautogui.keyDown('down')


def pressSpace(): # zıplama ve eğilme
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.19)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')


def imageGrab(): # dino'nun boyu tları
    box = (Cordinates.dinazor[0]+60,Cordinates.dinazor[1],
           Cordinates.dinazor[0]+140,Cordinates.dinazor[1]+5)
    image = ImageGrab.grab(box)
    grayImage= ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()

def main():

    while True:

        if(imageGrab()!= 647):
            pressSpace()
            Restart()


main()






