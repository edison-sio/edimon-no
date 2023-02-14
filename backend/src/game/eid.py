from abc import ABC, abstractmethod

class _ECounter:
    LOCATION = 0
    EDIMON = 0

class EID(ABC):
    pass

class ELocationID(EID):
    def __init__(self, count: int):
        self._count = count
    
    def __str__(self):
        return f'LOC{self._count:04}'

class EdimonID(EID):
    def __init__(self, count: int):
        self._count = count
    
    def __str__(self):
        return f'EDM{self._count:04}'
