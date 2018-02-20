# Name:

# See the README file for instructions.

from main import TurnOn
from main import TurnOff
from main import TurnLeft
from main import Move
from main import PickUp
from main import PutDown

from main import isAtPickUp
from main import isAtDeposit
from main import isAtEnd
from main import isClearAhead
from main import isClearLeft
from main import isClearRight
from main import hasPickUps
from main import hasError


from glob import UP
from glob import RIGHT
from glob import LEFT
from glob import DOWN

# This can be any value 0-7.  Chane it to test each function.
CURRENT_GAME = 7

# Set this to False to just test all your results without a GUI.  When set to True
# it will test one puzzle at a time.
SHOW_GUI = True

# The number of miliseconds between each step.  Raise it to slow things down.
# Lower it to speed it up.
STEP_TIME = 500



def solve0():
    TurnOn()
    TurnRight()
    Move()
    Move()
    TurnRight()
    Move()
    TurnOff()


def solve1():
    TurnOn()
    TurnRight()
    Move()
    PickUp()
    Move()
    PutDown()
    TurnRight()
    Move()
    TurnOff()

def solve2():
    TurnOn()
    MultiMove(2)
    TurnLeft()
    MultiMove(3)
    TurnRight()
    MultiMove(2)
    TurnRight()
    MultiMove(3)
    TurnOff()

def solve3():
    TurnOn()
    MultiMove(3)
    PickUp()
    TurnRight()
    for i in range(4):
        Move()
        PickUp()
    TurnRight()
    MultiMove(2)
    TurnRight()
    MultiMove(4)
    MultiPutDown(5)
    TurnAround()
    MultiMove(2)
    TurnOff()

def solve4():
    TurnOn()
    TurnRight()
    MultiMove(4)
    TurnRight()
    MultiMove(2)
    PickUp()
    Move()
    PickUp()
    MultiMove(2)
    PutDown()
    PutDown()
    TurnRight()
    MultiMove(3)
    TurnOff()

def solve5():
    TurnOn()
    TurnAround()
    MoveDownRightDiagonal()
    PickUp()
    MoveDownRightDiagonal()
    PutDown()
    MoveDownRightDiagonal()
    PickUp()
    MoveDownRightDiagonal()
    PickUp()
    MoveDownRightDiagonal()
    PutDown()
    PutDown()
    MoveDownRightDiagonal()
    TurnOff()

def solve6():
    TurnOn()
    MovePickUpSeq(3)
    TurnRight()
    MovePickUpSeq(2)
    MultiMove(2)
    MultiPutDown(5)
    TurnRight()
    MultiMove(2)
    PickUp()
    Move()
    PickUp()
    MultiMove(2)
    MultiPutDown(2)
    TurnRight()
    MultiMove(4)
    TurnRight()
    Move()
    PickUp()
    MultiMove(2)
    PutDown()
    TurnRight()
    MultiMove(2)
    TurnRight()
    Move()
    TurnOff()



def solve7():
    TurnOn()
    TurnRight()
    Move()
    PickUp()
    Move()
    PickUp()
    MultiMove(2)
    PickUp()
    Move()
    PickUp()
    TurnLeft()
    MultiMove(3)
    PickUp()
    TurnLeft()
    Move()
    PutDown()
    Move()
    PutDown()
    Move()
    PickUp()
    Move()
    PutDown()
    MultiMove(2)
    PutDown()
    TurnAround()
    MultiMove(4)
    TurnRight()
    MultiMove(5)
    TurnRight()
    Move()
    MultiPutDown(2)
    MultiMove(2)
    TurnOff()

# Turn to the right by making three left turns
def TurnRight():
    TurnLeft()
    TurnLeft()
    TurnLeft()

# Turn around by making two left turns
def TurnAround():
    TurnLeft()
    TurnLeft()

# Move forward n spaces
def MultiMove(n):
    for i in range(n):
        Move()

# Putdown n tokens
def MultiPutDown(n):
    for i in range(n):
        PutDown()

# Move to the downward right diagonal space
def MoveDownRightDiagonal():
    TurnLeft()
    Move()
    TurnRight()
    Move()

# Perform n move pickup sequences
def MovePickUpSeq(n):
    for i in range(n):
        MultiMove(2)
        PickUp()
