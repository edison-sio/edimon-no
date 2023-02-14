from backend.src.objects.player import EPlayer
from backend.src.world.places import EPlace

class EdimonGame:
    def __init__(self, player: EPlayer):
        self.player = player
