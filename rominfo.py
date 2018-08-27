"""
    Rom description of Dante98 II.
"""

import os

ORIGINAL_ROM_DIR = 'original'
TARGET_ROM_DIR = 'patched'

ORIGINAL_ROM_PATH = os.path.join(ORIGINAL_ROM_DIR, 'dante98-II_w_character.hdi')
TARGET_ROM_PATH = os.path.join(TARGET_ROM_DIR, 'dante98-II_w_character.hdi')
DUMP_XLS_PATH = 'dante98-II_dump.xlsx'

FILES = ['RPG.EXE', 'EDCHIP.EXE', 'EDCONV.EXE', 'EDENEMY.EXE', 'EDITEM.EXE', 'EDMAGIC.EXE',
         'EDMAP.EXE', 'EDMENU.EXE', 'EDPACK.EXE', 'EDPLAYER.EXE', 'EDUSAGE.EXE',
         'EDWORD.EXE', 'GF.COM', 'MUSIC.COM', 'UNPACK.BIN', 'ENEMY.DAT',
         'ITEM.DAT', 'MAGIC.DAT', 'MAPNAME.DAT', 'PLAYER.DAT',  'WORD.DAT',
         'CEDIT/MAIN.EXE']

# LHA is a separate utility


FILE_BLOCKS = {
    #"""
    #    Text for the editor itself
    #"""
    "RPG.EXE": [
        (0x19e9e, 0x1a180),
        (0x1a1ae, 0x1a5ac),
        #(0x1a9e6, 0x1ac04),  # debug things and copyright
    ],

    'EDCHIP.EXE': [
        (0x98c1, 0x9c24),
        (0x9fe4, 0xa1bd),
    ],

    'EDCONV.EXE': [
        (0xcbde, 0xd127),
    ],

    'EDENEMY.EXE': [
        (0x14420, 0x146d0),
        (0x146d8, 0x148f4),
        (0x1496c, 0x14b05),
        (0x14b20, 0x14c40),
        (0x14ca2, 0x151bd),
    ],

    'EDITEM.EXE': [
        (0x9a3c, 0x9bbf),
        (0x9c84, 0xa177),
    ],

    'EDMAGIC.EXE': [
        (0x99c4, 0xa09f),
    ],

    'EDMAP.EXE': [
        (0x15cb0, 0x165f3),
        (0x16654, 0x16a24),
        (0x16da0, 0x17879),
        (0x17956, 0x1803e),
        (0x18162, 0x187ed),
    ],

    'EDMENU.EXE': [
        (0x3a1c, 0x3ae0),
    ],

    'EDPACK.EXE': [
        (0x3f18, 0x44ca),
    ],

    'EDPLAYER.EXE': [
        (0xd0d6, 0xd3ef),
        (0xd722, 0xddaf),
    ],

    'EDUSAGE.EXE': [
        (0xc6bd, 0xd590),
        (0xd892, 0xe071),
        (0xe1aa, 0xf73b),
    ],

    'EDWORD.EXE': [
        (0x898c, 0x8f8e),
    ],

    'GF.COM': [
        (0x3ed, 0x5e2),
    ],

    'MUSIC.COM': [
        (0x1ec6, 0x22f9),
    ],

    'UNPACK.BIN': [
        (0x2c44, 0x2fe4),
    ],

    #"""
    #    Text for sample game
    #"""
    'ENEMY.DAT': [
        (0x0, 0x1320),
    ],

    "ITEM.DAT": [
        (0x0, 0x1848),
    ],

    'MAGIC.DAT': [
        (0x0, 0x3c3c),
    ],

    'MAPNAME.DAT': [
        (0x0, 0xe0),
    ],

    'PLAYER.DAT': [
        (0x0, 0x200),
    ],

    'WORD.DAT': [
        (0x0, 0x791)
    ],

    #"""
    #     Text for character editor
    #"""

    'CEDIT/MAIN.EXE': [
        (0x1461f, 0x147a3),  # Needs to be broken up
        (0x148e7, 0x14940),
        (0x19050, 0x191f5),  # Needs to be broken up
        (0x1a6aa, 0x1a8cf),  # Same
        (0x1b9ea, 0x1babd),
        (0x1c068, 0x1c24d),
    ],
}

POINTER_CONSTANT = {
    'EDENEMY.EXE': 0x14390,
    'EDPLAYER.EXE': 0xd020,
    'EDWORD.EXE': 0x8900,
}

POINTER_TABLE_SEPARATOR = {
    'EDENEMY.EXE': '\\\\x79\\\\x12',
    'EDPLAYER.EXE': '\\\\xe2\\\\0b',
    'EDWORD.EXE': None,
}

# EDENEMY POINTER_CONSTANT = 14390, I'm guessing
# ESC string is iat 14525
# 14525 - 14390 = 195 = 95 01.
# 14544 - 14390 =       b4 01.


# 1e 68 95 01 9a 3e 04
# 1e 68 b4 01 9a 3e 04

# DANTE2/GF.COM is the same as CEDIT/GF.COM. Also RPGCONST/GF.COM.
# RPGCONST/MAIN.EXE is the same as CEDIT/MAIN.EXE.

assert len(FILE_BLOCKS) == len(FILES), "%s %s" % (len(FILE_BLOCKS), len(FILES))