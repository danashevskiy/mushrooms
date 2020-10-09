#!/usr/bin/env bash

DEVICE=sysdefault:CARD=Headphones
NONBLOCK=--nonblock

amixer -D 'hw:1' set Headphone 100%

aplay -D $DEVICE $NONBLOCK ./tracks/1.wav &
aplay -D $DEVICE $NONBLOCK ./tracks/2.wav &
aplay -D $DEVICE $NONBLOCK ./tracks/3.wav &
aplay -D $DEVICE $NONBLOCK ./tracks/4.wav &
aplay -D $DEVICE $NONBLOCK ./tracks/5.wav &
aplay -D $DEVICE $NONBLOCK ./tracks/6.wav &
aplay -D $DEVICE $NONBLOCK ./tracks/7.wav &
aplay -D $DEVICE $NONBLOCK ./tracks/8.wav &
bash