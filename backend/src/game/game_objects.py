from .eid_generator import EIDGenerator

from objects.edimon import Edimon, EdimonStats, EdimonType
from players.player import EPlayer, EPlayerProfile, EPlayerBag

from world.places import ELocation
from world.geology import EDirection, EPosition

from game.config import load_config

class EGame:
    def __init__(self, config_filepath: str):
        self.config_file = config_filepath

        self.player: EPlayer = None
        self.edimons: list[Edimon] = []
        self.locations: list[ELocation] = []
        
    def add_player(self, name: str, gender: str):
        self.player = EPlayer(name, gender, EPosition(0, 0))
    
    def add_edimon(self, name: str, stats: EdimonStats, type_: EdimonType):
        new_edimon = Edimon(name, stats, type_)
        self.edimons.append(new_edimon)
    
    def add_location(self, name: str, positions: EPosition):
        new_location = ELocation(name, positions)
        self.locations.append(new_location)
    
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
            new_location = ELocation(name, positions)
            self.locations.append(new_location)

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

