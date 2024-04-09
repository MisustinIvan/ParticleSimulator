from typing import List, Tuple
import pygame
from math import pi

from DynamicLabel import Literal

ELECTRIC_PERMITTIVITY: float = 8.854e-12
EPSILON: float = 1e-6
EPSILON_vec2: pygame.Vector2 = pygame.Vector2(EPSILON, EPSILON)


class particle:
    mass: float

    last_pos: pygame.Vector2
    pos: pygame.Vector2
    vel: pygame.Vector2
    acc: pygame.Vector2

    electric_elementary_charge: float
    electric_charge: float
    spin: float

    flags: List[Literal["static", "dynamic"]]

    draw_radius: int
    draw_color: Tuple[int, int, int]

    def __init__(
        self,
        p: pygame.Vector2,
        v: pygame.Vector2,
        a: pygame.Vector2,
        flags: List[Literal["static", "dynamic"]],
    ) -> None:
        self.pos = p
        self.vel = v
        self.acc = a
        self.last_pos = p
        self.flags = flags

    def electric_interaction(self, p: "particle") -> pygame.Vector2:
        r = self.pos.distance_squared_to(p.pos)
        if r == 0:
            return pygame.Vector2(0, 0)

        F = (self.electric_charge * p.electric_charge) / (
            4 * pi * ELECTRIC_PERMITTIVITY * r + EPSILON
        )
        uv: pygame.Vector2 = self.pos - p.pos
        uv.scale_to_length(F)
        return uv

    def calculate_forces(self, p: "particle") -> pygame.Vector2:
        return self.electric_interaction(p)
