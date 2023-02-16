'''
This file design and implements Edimon class.
'''
from enum import Enum
from .edimon_objects import EMovableObject
from game.eid_generator import EIDGenerator
from world.geology import EPosition

class EdimonStats:
    '''
    EdimonStat represents edimon stat.
    '''
    def __init__(self, hp: int,
                       attack: float,
                       defense: float,
                       speed: float):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
    
    def to_object(self):
        return {
            'hp': self.hp,
            'attack': self.attack,
            'defense': self.defense,
            'speed': self.speed,
        }

class EdimonType(Enum):
    '''
    Edimon types.
    '''
    FIRE = 'fire'
    WATER = 'water'
    GRASS = 'grass'
    NORMAL = 'normal'

class Edimon:
    '''
    Edimon class.
    '''
    def __init__(self, name: str, 
                       stats: EdimonStats, 
                       type_: EdimonType):
        self.id = EIDGenerator.edimon()
        self.name = name
        self.stats = stats
        self.type = type_
    
    def get_stats(self) -> dict:
        return self.stats.to_object()

class EdimonObject(EMovableObject):
    '''
    Edimon copy object.
    '''
    def __init__(self, edimon: Edimon, pos: EPosition):
        super(EdimonObject, self).__init__(pos)
        self.edimon = edimon
    
    def get_stats(self) -> dict:
        return self.edimon.stats()
    