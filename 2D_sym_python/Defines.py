from enum import Enum

class WorldState(Enum):
    FIRST_SET=0
    START=1
    END=2

class MovementSide(Enum):
    LEFT=0
    RIGHT=1
    UP=2
    DOWN=3
    NONE=4

class whoMoves(Enum):
    HUMAN_MOVE=0
    WORLD_MOVE=1

class reportType(Enum):
    KILL=0
    CONSUMPTION=1
    SPAWN=2
    MOVED=3
    STRENGTH_INC=4
    ATTACK_REFLECTED=5
    HUMAN_GOT_AB=6
    ROUND_OG_AB=7
    CANT_USE_AB=8
    FILE_SAVED=9
    FILE_OPENED=10
    ANIMAL_OR_PLANT=11
    PRINT=12
    CLEAR=13
    ORGANISM_ADDED=14

class sideMove(Enum):
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3

HORIZ_SIZE = 10
VERTIC_SIZE = 10
DEF_MATRIX_SIZE = 10

DOT = '.'
ONE_STEP = 1
TWO_STEPS = 2
LETTER_RANGE_ANIMAL_A = 64
LETTER_RANGE_ANIMAL_Z = 91

FIGHT_LIST = 0
NEW_ORGANISM = 1