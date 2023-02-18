'''
This file design abstract geology objects in the Edimon world.
'''
from enum import Enum

class EDirection(Enum):
    '''
    An enum represents direction in Edimon world.
    '''
    FRONT = 'up'
    BACK = 'down'
    LEFT = 'left'
    RIGHT = 'right'

class EPositionValue(Enum):
    GRASS = 'grass'
    STONE = 'stone'
    WALL = 'wall'


class EPosition:
    '''
    This represents positions in Edimon world.
    '''
    def __init__(self, x: int, y: int, layer: int=0):
        self.x = x
        self.y = y
        self.layer = layer
    
    def move(self, dir: EDirection):
        if dir == EDirection.FRONT:
            self.y -= 1
        elif dir == EDirection.BACK:
            self.y += 1
        elif dir == EDirection.LEFT:
            self.x -= 1
        elif dir == EDirection.RIGHT:
            self.x += 1
        
    def set_layer(self, layer: int): 
        self.layer = layer
    
    def __str__(self):
        return f'({self.x}, {self.y}, {self.layer})'
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def get_next_position(loc: EPosition, dir: EDirection) -> EPosition:
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
    return EPosition(x, y)

def position_compare_key(pos: EPosition):
    return pos.x, pos.y, pos.layer