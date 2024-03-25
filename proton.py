from typing import Tuple
from particle import particle
from pygame import Vector2

class proton(particle):

    mass : float = 1.672e-27

    electric_elementary_charge : float = +1
    electric_charge : float = +1.602e-19
    spin : float = 0.5

    draw_color : Tuple[int, int, int] = (42, 162, 247)
    draw_radius : int = 15

    def __init__(self, p: Vector2, v: Vector2, a: Vector2) -> None:
        super().__init__(p, v, a)

        self.mass : float = 1.672e-27

        self.electric_elementary_charge : float = +1
        self.electric_charge : float = +1.602e-19
        self.spin : float = 0.5
