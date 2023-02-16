from .eid import ELocationID, EdimonID, _ECounter

class EIDGenerator:
    @staticmethod
    def location() -> ELocationID:
        counter = _ECounter.LOCATION
        _ECounter.LOCATION += 1
        return ELocationID(counter)
    
    @staticmethod
    def edimon():
        counter = _ECounter.EDIMON
        _ECounter.EDIMON += 1
        return EdimonID(counter)

    # TODO: More ID can be added.