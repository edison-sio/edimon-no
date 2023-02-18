from .eid_generator import EIDGenerator

from objects.edimon import Edimon, EdimonStats, EdimonType
from players.player import EPlayer, EPlayerProfile, EPlayerBag

from world.places import ELocation, EPlace
from world.geology import EDirection, EPosition, position_compare_key

from game.config import load_config

class EGame:
    def __init__(self, config_filepath: str):
        self.config_file = config_filepath

        self.player: EPlayer = None
        self.edimons: list[Edimon] = []
        self.locations: list[ELocation] = []
        self.places: list[EPlace] = []
        self.current_place_index = -1
        
    def add_player(self, name: str, gender: str):
        self.player = EPlayer(name, gender, EPosition(0, 0))
    
    def add_edimon(self, name: str, stats: EdimonStats, type_: EdimonType):
        new_edimon = Edimon(name, stats, type_)
        self.edimons.append(new_edimon)
    
    def add_location(self, name: str, positions: EPosition):
        new_location = ELocation(name, positions)
        self.locations.append(new_location)
    
    def add_place(self, name: str, locs: list[ELocation], size: tuple[int, int]):
        new_place = EPlace(name, locs, size)
        self.places.append(new_place)

    def setup(self):
        config_data = load_config(self.config_file)
        
        # Player Setup
        player_data = config_data['player']
        self.add_player(player_data['name'], player_data['gender'])
        
        # Edimons Setup
        edimons_data = config_data['edimons']
        for edimon_data in edimons_data:
            stats_data = edimon_data['stats']
            edimon_stats = EdimonStats(stats_data['hp'], stats_data['attack'], stats_data['defense'], stats_data['speed'])
            self.add_edimon(edimon_data['name'], edimon_stats, EdimonType(edimon_data['type']))
        
        # Locations Setup
        locations_data = config_data['locations']
        for location_data in locations_data:
            name = location_data['name']
            positions_data = location_data['positions']
            positions = []
            for position_data in positions_data:
                position = EPosition(position_data['x'], position_data['y'], position_data['layer'])
                positions.append(position)
            # new_location = ELocation(name, positions)
            self.add_location(name, positions)
        

        places_data = config_data['places']        
        for place_data in places_data:
            name = place_data['name']
            xs = place_data['xs']
            ys = place_data['ys']
            size = (xs, ys)
            locs_name = place_data['locations']
            locs: list[ELocation] = []
            for loc in self.locations:
                if loc.name in locs_name:
                    locs.append(loc)
            self.add_place(name, locs, size)
        
        if len(self.places) > 0:
            self.current_place_index = 0

    def start(self):
        self.setup()
    
    def move_up(self):
        self.player.move(EDirection('up'))
    
    def move_down(self):
        self.player.move(EDirection('down'))
    
    def move_left(self):
        self.player.move(EDirection('left'))
    
    def move_right(self):
        self.player.move(EDirection('right'))
    
    def change_place(self, place_index: int): 
        # TODO: one more condition: the new place should be connected to the current place
        if place_index >= 0 or place_index < len(self.places):
            self.current_place_index = place_index

