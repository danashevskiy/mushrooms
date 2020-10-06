#!/usr/bin/env python3

from gpiozero import Button
from signal import pause

MUSHROOM_1 = "GPIO5"
MUSHROOM_2 = "GPIO6"
MUSHROOM_3 = "GPIO13"
MUSHROOM_4 = "GPIO19"
MUSHROOM_5 = "GPIO26"
MUSHROOM_6 = "GPIO16"
MUSHROOM_7 = "GPIO20"
MUSHROOM_8 = "GPIO21"

def test():
    print("Hello!")

def main():
    button = Button(MUSHROOM_8)
    button.when_pressed = test
    pause()

main()