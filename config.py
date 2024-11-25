from enum import Enum

class Scenes(Enum):
    MENU = 1
    BFS = 2
    DFS = 3
    A_STAR = 4

BLACK = (30, 28, 28)
WHITE = (235, 235, 235)

GRID_SIZE_SMALL = 40
CELL_SIZE_SMALL = 20

GRID_SIZE_MEDIUM = 25
CELL_SIZE_MEDIUM = 32
GRID_SIZE_LARGE = 26

WIDTH = 800
HEIGHT = 900

class State(Enum):
    EMPTY = 1
    WALL = 2
    VISITED = 3
    VISITING = 4
    START = 5
    FINISH = 6
    PATH = 7
    ERROR = 8
    
class Colors(Enum):
    BORDER = (60, 58, 59)
    WALL = (60, 58, 59)
    EMPTY = (30, 28, 28)
    START = (40,131,213)
    PATH = (40,131, 213)
    FINISH = (65,201,76)
    VISITED = (25, 63, 28)
    VISITING = (65,201,76)
    ERROR = (236, 86, 87)
    