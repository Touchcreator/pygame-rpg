# simple utils for the game

import colorsys

def hsv_to_rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))