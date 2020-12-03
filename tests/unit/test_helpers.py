import numpy as np
from gradientascent.ascender import Ascender, Coordinate


def create_ascender(array):
    return Ascender(array, Coordinate(0,0))
