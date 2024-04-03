from pygame import Vector2
from style import Tuple
from Widget import Widget
from typing import Callable
import pygame


class Clickable(Widget):
    def __init__(
        self,
        pos: Vector2 | Tuple[int, int],
        dimensions: Vector2 | Tuple[int, int],
        parent: Widget | None,
        children: list[Widget],
        on_click: Callable[[], None],
    ) -> None:
        super().__init__(pos, dimensions, parent, children)

        self.on_click = on_click

    def handle_event(self, event) -> None:
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and self.is_mouse_over()
            and pygame.mouse.get_pressed(3)[0]
        ):
            self.on_click()

        for child in self.children:
            child.handle_event(event)
