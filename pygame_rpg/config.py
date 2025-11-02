import os

FRAMES_PER_SECOND = 30 # fps


TILESIZE = 16



# DEBUG
DEBUG_IMG_ON = False
DEBUG_PLAYER = False
DEBUG_COORDS = True

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120

TILES_PATH = os.path.join("assets", "img", "tiles.png")
NUT_ASSETS = os.path.join("assets", "img", "nutv2.png")
NUT_STILL = os.path.join("assets", "img", "nutstill.png")

if DEBUG_IMG_ON:
    TILES_PATH = os.path.join("assets", "img", "debug", "tilesdebug.png")
    NUT_ASSETS = os.path.join("assets", "img", "debug", "nutboxguide.png")

if DEBUG_PLAYER:
    NUT_ASSETS = os.path.join("assets", "img", "debug", "nutboxguide.png")