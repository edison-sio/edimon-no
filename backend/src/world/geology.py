'''
This file design abstract geology objects in the Edimon world.
'''
from enum import Enum

class EDirection(Enum):
    '''
    An enum represents direction in Edimon world.
    '''
    FRONT = 1
    BACK = 2
    LEFT = 3
    RIGHT = 4

class EPosition:
    '''
    This represents positions in Edimon world.
    '''
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def move(self, dir: EDirection):
        if dir == EDirection.FRONT:
            self.y -= 1
        elif dir == EDirection.BACK:
            self.y += 1
        elif dir == EDirection.LEFT:
            self.x -= 1
        elif dir == EDirection.RIGHT:
            self.x += 1
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class ELocationID:
    ID = -1
    def __init__(self):
        self.ID += 1

class ELocation:
    '''
    This class represents location in Edimon world.
    '''
    def __init__(self, name: str, xs: int, ys: int) -> None:
        self.poss: list[EPosition] = []
        for y in ys:
            for x in xs:
                self.poss.append(EPosition(x, y))
        
    

    

def get_next_location(loc: ELocation, dir: EDirection) -> ELocation:
    x = loc.x
    y = loc.y
    if dir == EDirection.FRONT:
        y -= 1
    elif dir == EDirection.BACK:
        y += 1
    elif dir == EDirection.LEFT:
        x -= 1
    elif dir == EDirection.RIGHT:
        x += 1
    return ELocation(x, y)