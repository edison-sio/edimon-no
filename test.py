class ECounter:
    LOCATION = 0
    EDIMON = 0

class ELocationID:
    def __init__(self, count: int):
        self._count = count
    
    def __str__(self):
        return f'LOC{self._count:04}'

class EdimonID:
    def __init__(self, count: int):
        self._count = count
    
    def __str__(self):
        return f'EDM{self._count:04}'

class EIDGenerator:
    @staticmethod
    def location() -> ELocationID:
        counter = ECounter.LOCATION
        ECounter.LOCATION += 1
        return ELocationID(counter)
    
    @staticmethod
    def edimon():
        counter = ECounter.EDIMON
        ECounter.EDIMON += 1
        return EdimonID(counter)

print(EIDGenerator.location())
print(EIDGenerator.location())
print(EIDGenerator.location())
print(EIDGenerator.location())
print(EIDGenerator.edimon())
print(EIDGenerator.location())
