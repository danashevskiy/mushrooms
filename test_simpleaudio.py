

import simpleaudio as sa

def main():
    a = sa.WaveObject.from_wave_file("./tracks/1.wav")
    mushroom_2 = sa.WaveObject.from_wave_file("./tracks/2.wav")
    mushroom_3 = sa.WaveObject.from_wave_file("./tracks/3.wav")
    mushroom_4 = sa.WaveObject.from_wave_file("./tracks/4.wav")
    mushroom_5 = sa.WaveObject.from_wave_file("./tracks/5.wav")
    mushroom_6 = sa.WaveObject.from_wave_file("./tracks/6.wav")
    mushroom_7 = sa.WaveObject.from_wave_file("./tracks/7.wav")
    mushroom_8 = sa.WaveObject.from_wave_file("./tracks/8.wav")
    a.play()
    mushroom_2.play()
    mushroom_3.play()
    mushroom_4.play()
    mushroom_5.play()
    mushroom_6.play()
    mushroom_7.play()
    mushroom_8.play()

    while(True):
        pass

main()