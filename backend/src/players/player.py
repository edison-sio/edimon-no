'''
This file implement class Player play about 
'''
from objects.edimon import Edimon
from objects.edimon_objects import EMovableObject
from world.geology import EDirection, EPosition

class EPlayerBag:
    '''
    Player Bag which can store his/her Edimon, money, etc.
    '''
    def __init__(self):
        self.gold = 0.0
        self.capacity = 6
        self.edimons: list[Edimon] = []
    
    def earn_gold(self, earn: float) -> float:
        self.gold += earn
        return self.gold
    
    def add_edimon(self, edimon: Edimon) -> bool:
        if len(self.edimons) >= self.capacity:
            return False
        self.edimons.append(edimon)
        return True

    def remove_edimon(self, index: int) -> bool:
        if index < 0 or index >= self.capacity:
            raise IndexError
        edimon = self.edimons[index]
        self.edimons.remove(edimon)
        

class EPlayerProfile:
    '''
    Player profile to store player details.
    '''
    def __init__(self, name: str, gender: str):
        self.name = name
        self.gender = gender
    

class EPlayer(EMovableObject):
    '''
    The player class.
    '''
    def __init__(self, name: str, gender: str, pos: EPosition):
        super(EPlayer, self).__init__(pos)
        self.profile = EPlayerProfile(name, gender)
        self.bag = EPlayerBag()
