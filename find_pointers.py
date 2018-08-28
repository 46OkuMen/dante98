import re
import os
import openpyxl
from collections import OrderedDict
from romtools.dump import BorlandPointer, PointerExcel
from romtools.disk import Gamefile

from rominfo import POINTER_CONSTANT, POINTER_TABLE_SEPARATOR, FILE_BLOCKS

FILES_WITH_POINTERS = POINTER_CONSTANT

# POINTER_CONSTANT is the line where "Borland Compiler" appears, rounded down to the nearest 0x10.

# Removing the 9a at the end of this one. Didn't show up in some pointers.
pointer_regex = r'\\x1e\\x68\\x([0-f][0-f])\\x([0-f][0-f])'
pointer_table_regex_base = r'\\x([0-f][0-f])\\x([0-f][0-f])sep'

def capture_pointers_from_function(hx, regex): 
    return re.compile(regex).finditer(hx)

def location_from_pointer(pointer, constant):
    return '0x' + str(format((unpack(pointer[0], pointer[1]) + constant), '05x'))

def unpack(s, t=None):
    if t is None:
        t = str(s)[2:]
        s = str(s)[0:2]
    s = int(s, 16)
    t = int(t, 16)
    value = (t * 0x100) + s
    return value

pointer_count = 0

try:
    os.remove('dante98-II_pointer_dump.xlsx')
except FileNotFoundError:
    pass

PtrXl = PointerExcel('dante98-II_pointer_dump.xlsx')

for gamefile in FILES_WITH_POINTERS:
    print(gamefile)
    pointer_locations = OrderedDict()
    gamefile_path = os.path.join('original', 'DANTE2', gamefile)
    GF = Gamefile(gamefile_path, pointer_constant=POINTER_CONSTANT[gamefile])
    with open(gamefile_path, 'rb') as f:
        bs = f.read()
        target_areas = FILE_BLOCKS[gamefile]
        # target_area = (GF.pointer_constant, len(bs))
        #print(hex(target_area[0]), hex(target_area[1]))

        only_hex = u""
        for c in bs:
            only_hex += u'\\x%02x' % c

        #print(only_hex)

        try:
            pointer_table_regex = pointer_table_regex_base.replace('sep', POINTER_TABLE_SEPARATOR[gamefile])
        except TypeError:
            # When POINTER_TABLE_SEPARATOR[gamefile] is None, no pointer
            # tables. skip that regex
            pointer_table_regex = None

        for regex in (pointer_regex, pointer_table_regex):
            if regex is None:
                continue
            #print(regex)
            pointers = capture_pointers_from_function(only_hex, regex)

            for p in pointers:
                #print(p)
                # Hard-coded pointers are 1e 68 XX YY...
                if regex == pointer_regex:
                    pointer_location = p.start()//4 + 2
                # Table pointers are at that same location.
                elif regex == pointer_table_regex:
                    pointer_location = p.start()//4



                pointer_location = '0x%05x' % pointer_location
                text_location = int(location_from_pointer((p.group(1), p.group(2)), GF.pointer_constant), 16)

                #print("Text:", hex(text_location), "Pointer:", pointer_location)

                if all([not t[0] <= text_location<= t[1] for t in target_areas]):
                    #print("Skipping")
                    continue

                all_locations = [int(pointer_location, 16),]

                #print(pointer_locations)

                if (GF, text_location) in pointer_locations.keys():
                    all_locations = pointer_locations[(GF, text_location)]
                    all_locations.append(int(pointer_location, 16))

                pointer_locations[(GF, text_location)] = all_locations
                print(pointer_locations[(GF, text_location)])


    # Setup the worksheet for this file
    worksheet = PtrXl.add_worksheet(GF.filename)

    row = 1

    for (gamefile, text_location), pointer_locations in sorted((pointer_locations).items()):
        obj = BorlandPointer(gamefile, pointer_locations, text_location)
        #print(text_location)
        #print(pointer_locations)
        for pointer_loc in pointer_locations:
            worksheet.write(row, 0, hex(text_location))
            worksheet.write(row, 1, hex(pointer_loc))
            try:
                worksheet.write(row, 2, obj.text())
            except:
                worksheet.write(row, 2, u'')
            row += 1

PtrXl.close()