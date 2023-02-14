'''
This file designed and implement all objects in the edimon world.
'''
from abc import ABC, abstractmethod

from world.geology import ELocation, EDirection, get_next_location

class EObject:
    '''
    The base abstract class inherited by every objects in the edimon world.
    '''
    @abstractmethod
    def location(self) -> ELocation:
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
    def __init__(self, map: list[ELocation]):
        self.loc = map[0]
        self.map = map
    
    def change_map(self, map):
        self.loc = map[0]
        self.map = map
    
    def move(self, dir: EDirection):
        next_loc = get_next_location(self.loc, dir)
        if next_loc not in self.map:
            return
        self.loc.move(dir)
