#!/usr/bin/env python3

import pygame as pg

pg.mixer.init()
pg.init()

m_1 = pg.mixer.Sound("tracks/1.wav")
m_2 = pg.mixer.Sound("tracks/2.wav")
m_3 = pg.mixer.Sound("tracks/3.wav")
m_4 = pg.mixer.Sound("tracks/4.wav")
m_5 = pg.mixer.Sound("tracks/5.wav")
m_6 = pg.mixer.Sound("tracks/6.wav")
m_7 = pg.mixer.Sound("tracks/7.wav")
m_8 = pg.mixer.Sound("tracks/8.wav")

print(m_1)
print(m_2)
print(m_3)
print(m_4)
print(m_5)
print(m_6)
print(m_7)
print(m_8)

pg.mixer.set_num_channels(10)

m_1.play()
m_2.play()
m_3.play()
m_4.play()
m_5.play()
m_6.play()
m_7.play()
m_8.play()

while(True):
    pass