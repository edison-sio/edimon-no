'''
This file implements classes represent or related to places in Edimon.
'''
from objects.edimon_objects import EStableObject, EAbstractObject, EObject
from world.geology import EDirection, EPosition


class ELocation:
    '''
    This class represents location in Edimon world.
    '''
    def __init__(self, name: str, positions: EPosition) -> None:
        # self.poss: list[EPosition] = []
        # for y in ys:
        #     for x in xs:
        #         self.poss.append(EPosition(x, y))
        self.name = name
        self.positions = positions
        
class EMap(EAbstractObject):
    '''
    Representation of map includes all available places in Edimon world.
    '''
    def __init__(self):
        self.places: list[ELocation] = []
    
    def add_location(self, place: ELocation):
        self.places.append(place)
    
    def remove_location(self, place_id: int):
        place = self.places[place_id]
        self.places.remove(place)