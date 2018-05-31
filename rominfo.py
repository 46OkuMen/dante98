"""
    Rom description of Dante98 II.
"""

FILES = ['RPG.EXE', 'EDCHIP.EXE', 'EDCONV.EXE', 'EDENEMY.EXE', 'EDMAGIC.EXE',
         'EDMAP.EXE', 'EDMENU.EXE', 'EDPACK.EXE', 'EDPLAYER.EXE', 'EDUSAGE.EXE',
         'EDWORD.EXE', 'GF.COM', 'MUSIC.COM', 'UNPACK.BIN', 'ENEMY.DAT',
         'ITEM.DAT', 'MAGIC.DAT', 'MAPNAME.DAT', 'PLAYER.DAT',  ]

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
        (0x14420, 0x148f4),
        (0x1496c, 0x14c40),
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
        (0x0, 0x792)
    ],
}
