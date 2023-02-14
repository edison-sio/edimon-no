'''
This file implements classes represent or related to places in Edimon.
'''
from objects.edimon_objects import EStableObject, EAbstractObject, EObject
from world.geology import ELocation


class EPlace(EStableObject):
    '''
    Representation of places in Edimon world.
    '''
    def __init__(self, name: str, locs: list[ELocation], spawn: ELocation, objs: list[EObject]):
        self.name = name
        self.locs = locs
        self.spawn = spawn
        self.objs = objs

    def connect_places(self) -> list:
        pass

class EMap(EAbstractObject):
    '''
    Representation of map includes all available places in Edimon world.
    '''
    def __init__(self):
        self.places: list[EPlace] = []
    
    def add_place(self, place: EPlace):
        self.places.append(place)
    
    def remove_place(self, place_id: int):
        place = self.places[place_id]
        self.places.remove(place)
    