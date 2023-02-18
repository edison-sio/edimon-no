'''
This file implements classes represent or related to places in Edimon.
'''
from objects.edimon_objects import EStableObject, EAbstractObject, EObject
from world.geology import EDirection, EPosition, position_compare_key


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
        
# class EMap(EAbstractObject):
#     '''
#     Representation of map includes all available places in Edimon world.
#     '''
#     def __init__(self):
#         self.places: list[ELocation] = []
    
#     def add_location(self, place: ELocation):
#         self.places.append(place)
    
#     def remove_location(self, place_id: int):
#         place = self.places[place_id]
#         self.places.remove(place)
class EPlace:
    def __init__(self, name: str, locs: list[ELocation], size: tuple[int, int]):
        self.name = name
        self.locations = locs
        self.xs = size[0]
        self.ys = size[1]

        self.positions: list[EPosition] = []
        known_positions: list[EPosition] = self.get_all_location_postitions()

        for y in range(self.ys):
            for x in range(self.xs):
                base_position = EPosition(x, y, 0)
                if base_position not in known_positions:
                    self.positions.append(base_position)
        self.positions += known_positions

        self.positions.sort(key=position_compare_key)

    def get_all_location_postitions(self) -> list[EPosition]:
        poss: list[EPosition] = []
        for loc in self.locations:
            poss += loc.positions
        return poss
    
    def add_location(self, loc: ELocation):
        loc_index = self.locations.index(loc)
        self.locations[loc_index] = loc
