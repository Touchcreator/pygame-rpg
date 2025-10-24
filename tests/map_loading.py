import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from pygame_rpg.map_loader import MapLoader

loader = MapLoader()

loader.load("assets/maps/map1.txt")