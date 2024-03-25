from typing import Tuple
from particle import particle
from pygame import Vector2

class positron(particle):

    mass : float = 9.109e-31

    electric_elementary_charge : float = 1
    electric_charge : float = 1.602e-19
    spin : float = 0.5

    draw_color : Tuple[int, int, int] = (130, 34, 240)
    draw_radius : int = 5

    def __init__(self, p: Vector2, v: Vector2, a: Vector2) -> None:
        super().__init__(p, v, a)

        self.mass : float = 9.109e-31

        self.electric_elementary_charge : float = 1
        self.electric_charge : float = 1.602e-19
        self.spin : float = 0.5
