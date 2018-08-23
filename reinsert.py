"""
    Dante98-II reinserter.
    Based on the CRW reinserter base.
"""

import os

from rominfo import FILES, FILE_BLOCKS, ORIGINAL_ROM_PATH, TARGET_ROM_PATH
from romtools.disk import Disk, Gamefile, Block
from romtools.dump import DumpExcel

DUMP_XLS_PATH = 'dante98-II_dump.xlsx'

Dump = DumpExcel(DUMP_XLS_PATH)
OriginalDante = Disk(ORIGINAL_ROM_PATH, dump_excel=Dump)
TargetDante = Disk(TARGET_ROM_PATH)

FILES_TO_REINSERT = ['ENEMY.DAT',]

for filename in FILES_TO_REINSERT:
    if filename.endswith('.DAT'):
        path_in_disk = "DANTE2\\DAT_RPG"
        gamefile_path = os.path.join('original', 'DANTE2', 'DAT_RPG', filename)
    else:
        path_in_disk = "DANTE2\\"
        gamefile_path = os.path.join('original', 'DANTE2', filename)

    gamefile = Gamefile(gamefile_path, disk=OriginalDante, dest_disk=TargetDante)

    for block in FILE_BLOCKS[filename]:
        block = Block(gamefile, block)
        previous_text_offset = block.start
        diff = 0
        for t in Dump.get_translations(block):
            print(t.english)
            loc_in_block = t.location - block.start + diff

            this_diff = len(t.en_bytestring) - len(t.jp_bytestring)
            if filename.endswith('.DAT'):
                print(t.en_bytestring)
                print(t.jp_bytestring)
                print("Diff is ", this_diff)
                # Need to pad with 00's
                while this_diff < 0:
                    t.en_bytestring += b'\x00'
                    this_diff += 1
                while this_diff > 0:
                    t.jp_bytestring += b'\x00'
                    this_diff -= 1

                assert len(t.en_bytestring) - len(t.jp_bytestring) == 0


            #print(t.jp_bytestring)
            try:
                i = block.blockstring.index(t.jp_bytestring)
            except ValueError:
                print(t, "wasn't found in the string. Skipping for now")
                continue
            j = block.blockstring.count(t.jp_bytestring)

            index = 0
            while index < len(block.blockstring):
                index = block.blockstring.find(t.jp_bytestring, index)
                if index == -1:
                    break
                index += len(t.jp_bytestring) # +2 because len('ll') == 2

            assert loc_in_block == i, (hex(loc_in_block), hex(i))

            block.blockstring = block.blockstring.replace(t.jp_bytestring, t.en_bytestring, 1)

            #gamefile.edit_pointers_in_range((previous_text_offset, t.location), diff)
            previous_text_offset = t.location

            diff += this_diff

    block_diff = len(block.blockstring) - len(block.original_blockstring)
    if block_diff < 0:
        block.blockstring += (-1)*block_diff*b'\x00'
    block_diff = len(block.blockstring) - len(block.original_blockstring)
    assert block_diff == 0, block_diff

    block.incorporate()

    # TODO: Don't encode it if the file is in UNCOMPRESSED_FILES
    gamefile.write(skip_disk=True)
    #decompressed_path = 'patched/%s' % gamefile.filename
    #print(decompressed_path)
    #encode(decompressed_path)
    encoded_path = 'patched/' + filename
    TargetDante.insert(encoded_path, path_in_disk=path_in_disk)
