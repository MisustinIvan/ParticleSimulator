from Clickable import Clickable
from pygame import Vector2
import pygame
from typing import Tuple, Callable
from Widget import Widget


class Button(Clickable):
    def __init__(
        self,
        pos: Vector2 | Tuple[int, int],
        dimensions: Vector2 | Tuple[int, int],
        parent: Widget | None,
        on_click: Callable[[Clickable], None]
    ) -> None:
        super().__init__(pos, dimensions, parent, on_click)


    def draw(self, surface : pygame.Surface) -> None:
        pass

    def is_mouse_over(self) -> bool:
        return True


b = Button((0,0), (0,0), None, lambda b : print(b.pos))
b.on_click(b)