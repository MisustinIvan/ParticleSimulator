from pygame import Vector2
from Widget import Widget
from typing import Callable, Tuple
from abc import abstractmethod
import pygame


class Clickable(Widget):
    on_click: "Callable[[Clickable], None]"

    def __init__(
        self,
        pos: Vector2 | Tuple[int, int],
        dimensions: Vector2 | Tuple[int, int],
        parent: Widget | None,
        on_click: "Callable[[Clickable], None]",
    ) -> None:
        super().__init__(pos, dimensions, parent)
        self.on_click = on_click

    def handle_event(self, event) -> None:
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and self.is_mouse_over()
            and pygame.mouse.get_pressed(3)[0]
        ):
            self.on_click(self)

    @abstractmethod
    def is_mouse_over(self) -> bool:
        pass

    @abstractmethod
    def draw(self, surface: pygame.Surface) -> None:
        pass
