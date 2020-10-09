#!/usr/bin/env python3

from gpiozero import Button
from signal import pause
import pygame as pg
import os
import subprocess

TRACK_FOLDER = "./tracks/"

pins = ("GPIO5", "GPIO6", "GPIO13", "GPIO19", "GPIO26", "GPIO16", "GPIO20", "GPIO21")
tracks = os.listdir(TRACK_FOLDER)
buttons = [None] * 8
players = [None] * 8

def main():
    #set maxumum volume for jack output
    subprocess.run("amixer -D 'hw:1' set Headphone 100%", shell=True)
    pg.mixer.init()
    pg.init()
    for index, (pin, track) in enumerate(zip(pins, tracks)):
        players[index] = pg.mixer.Sound(TRACK_FOLDER + track)
        buttons[index] = Button(pin)
        buttons[index].when_pressed = players[index].play
    pg.mixer.set_num_channels(8)
    pause()

main()