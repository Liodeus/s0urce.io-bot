import pyautogui
import pyscreenshot as ImageGrab
import time
import os
from PIL import ImageOps
from numpy import *
import words

# Globals
# --------------------

x_pad = 531
y_pad = 666


def screenGrab():
    box = (x_pad, y_pad,  x_pad + 234, y_pad + 19)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    return a



def get_cords():
    x, y = pyautogui.position()
    x = x - x_pad
    y = y - y_pad
    print(x, y)


def mousePos(cord):
    pyautogui.moveTo(x_pad + cord[0], y_pad + cord[1])


def test(value):
    mousePos((159, 42))
    leftClick()
    pyautogui.typewrite(words.words[value])
    pyautogui.press("enter")
    time.sleep(.4)


def writeWord(word):
    mousePos((159, 42))
    leftClick()
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(.4)


def leftClick():
    pyautogui.click()
    print("Click")


def message():
    mousePos(Pos.hackingSuccessfullWrite)
    leftClick()
    pyautogui.typewrite("Hacked by Liodeus's bot :)")
    mousePos(Pos.sendButton)
    leftClick()


class Pos:
    cmdWrite = (159, 42)
    sendButton = (160, -107)
    hackingSuccessfullWrite = (156, -154)


if __name__ == "__main__":
    Flag = True

    while Flag:
        s = screenGrab()

        while s == 20445:
            writeWord("ghostfilesystem")
            writeWord("createnewpackage")
            s = screenGrab()

        while s == 20524:
            writeWord("systemgridtype")
            writeWord("fileexpresslog")
            s = screenGrab()

        while s == 19040:
            writeWord("datatype")
            writeWord("download")
            s = screenGrab()

        if s in words.words:
            test(s)
        else:
            Flag = False
