from particle import particle
from pygame import Vector2

class photon(particle):
    mass : float = 0
    electric_charge : float = 0
    electric_elementary_charge : float = 0
    spin : float = 1
    frequency : float

    def __init__(self, p: Vector2, v: Vector2, a: Vector2, f : float) -> None:
        super().__init__(p, v, a)
        self.frequency = f

    def scatter(self, p : 'photon') -> None:
        pass
