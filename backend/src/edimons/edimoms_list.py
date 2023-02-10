'''
This file implements representation of edimons and functions to list 
specific edimons.
'''
from enum import Enum
from objects.edimon_objects import EdStableObject, EdMovableObject
from collections.abc import Callable

class EdimonID(Enum):
    '''
    A enum class represents id for all edimons
    '''
    EDICHU = 1,
    BAOZI = 2,
    JARVIE = 3,
    XIAOJIAOPI = 4,
    XIAOJITUI = 5,

class Edimon(EdMovableObject):
    '''
    An edimon.
    '''
    def __init__(self):
        pass


class EdimonDict(EdStableObject):
    pass

class Eddex(EdStableObject):
    '''
    An Eddex is a book to show details of the edimon.
    '''
    # def __init__(self, edimons: list[Edimon], )