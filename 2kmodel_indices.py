import os
import struct
import sys
from pathlib import Path as plib

plib.home().joinpath('indicesUpdater_tool', '2k19convert.model')

f = open('2k19convert.model', 'rb+')
sect_start = 0x16274
sect_end = 0x26f23
sect = range(sect_start, sect_end)

f.seek(sect_start)

print ('Writing vertices...')
indices = []
for entry in sect:
    v1 = struct.unpack('<H', f.read(2))
    v2 = struct.unpack('<H', f.read(2))
    v3 = struct.unpack('<H', f.read(2))

    # Comment this and uncomment the line below if you want to just rewrite original file
    # opposite if you want to add the 112

    # entry_tuple = tuple(map(sum, zip(v1 + v2 + v3, (112, 112, 112))))
    entry_tuple = tuple(v1 + v2 + v3)

    indices.append(entry_tuple)


f.seek(sect_start)
over_the_max_num = 0
for index in indices:
    maxval = 32767 * 2 + 1
    over_the_max = False

    for e in index:

        if e > maxval:
            print("OVER THE MAX: " + str(e))
            over_the_max = True
            f.write(struct.pack('<H', int(e - maxval)))
        else:
            f.write(struct.pack('<H', int(e)))
    if over_the_max:
        over_the_max_num += 1

print('Over the max: ' + str(over_the_max_num))
print ('Done.')
