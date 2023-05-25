import struct
import wave
import os

n = True
IF = 0

name = input("Введите название файла: ")+".wav"
dir = os.path.abspath(os.curdir)
for root, dirs, files in os.walk(dir):
    if name in files:
        while IF == 0:
            i_frame = input("Введите натуральное число i из диапазона от 2 до 5: ")
            if int(i_frame) == float(i_frame) and  1 < int(i_frame) < 6:
                IF += 1
         n = False

sound = wave.open(name, mode="rb")
fcount = sound.getnframes()
#print(fcount)

data = sound.readframes(fcount)
params = sound.getparams()
sound.close()

data = struct.unpack("<" + str(fcount * 2) + "h", data)
new_data = list(data)
del new_data[::int(i_frame)]
new_frame = struct.pack("<" + str(len(new_data)) + "h", *new_data)
snd = wave.open(name, mode="wb")
snd.setparams(params)
snd.writeframes(new_frame)
snd.close()