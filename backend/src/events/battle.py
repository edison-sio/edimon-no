'''
This file implement class EdBattle to represent battle between two Edimon.
'''
from abc import ABC, abstractmethod

class EdEvent(ABC):
    '''
    EdEvent represents all events occured in Edimon world.
    '''
    def title(self):
        '''
        Event title.
        '''

class EdBattle(EdEvent):
    '''
    EdBattle represents a fight battle between two edimons.
    '''
    