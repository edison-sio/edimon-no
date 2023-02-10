'''
This file design and implements Edimon class.
'''
from enum import Enum
from edimon_objects import EMovableObject

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

class EdimonType(Enum):
    '''
    Edimon types.
    '''
    FIRE = 1
    WATER = 2
    GRASS = 3

class Edimon:
    '''
    Edimon class.
    '''
    def __init__(self, name: str, 
                       stats: EdimonStats, 
                       type_: EdimonType):
        self.name = name
        self.hp = stats.hp
        self.attack = stats.attack
        self.defense = stats.defense
        self.speed = stats.speed
        self.type = type_
    