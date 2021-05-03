"""
This is the secondary clipboard. It basically allows you to copy two things at once and also paste them.
"""

import os
import pyperclip
import time
import keyboard

__author__ = "Pranav Sandeep"


class Secondary_Clipboard:
    def __init__(self):
        self.SecondaryClipBoardContent = ""


SClipBoard = Secondary_Clipboard()


def CopyToSecondaryClipBoard(exe=".\Dependencies\Copy.exe"):
    OriginalContent = pyperclip.paste()
    time.sleep(0.1)
    os.system(exe)
    time.sleep(0.1)
    SecondaryClipboardContent = pyperclip.paste()
    print(SecondaryClipboardContent)

    pyperclip.copy(str(OriginalContent))

    return SecondaryClipboardContent


def Copy():
    while True:
        time.sleep(0.1)
        keyboard.wait("ctrl + ]")
        SClipBoard.SecondaryClipBoardContent = CopyToSecondaryClipBoard()
        print(SClipBoard.SecondaryClipBoardContent)


def Paste():
    while True:
        time.sleep(0.1)
        keyboard.wait("ctrl + [")
        keyboard.write(str(SClipBoard.SecondaryClipBoardContent))
