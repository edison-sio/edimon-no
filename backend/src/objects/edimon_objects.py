'''
This file designed and implement all objects in the edimon world.
'''
# from abc import ABC, abstractmethod

from world.geology import EPosition, EDirection, get_next_position

class EObject:
    '''
    The base abstract class inherited by every objects in the edimon world.
    '''
    def location(self) -> EPosition:
        pass


class EStableObject(EObject):
    '''
    A class inherited by every stable objects in the edimon world.
    '''

class EAbstractObject(EObject):
    '''
    An abstract class inherited by objects that is not physically exists on the map.
    e.g. Eddex.
    '''

class EMovableObject(EObject):
    '''
    An abstract class inherited by every movable objects in the edimon world.
    '''
    def __init__(self, pos: EPosition):
        self.pos = pos
    
    def change_map(self, map):
        self.pos = map[0]
        self.map = map
    
    def move(self, dir: EDirection):
        next_pos = get_next_position(self.pos, dir)
        if (next_pos.layer - self.pos.layer) <= 0.5:
            self.pos.move(dir)
