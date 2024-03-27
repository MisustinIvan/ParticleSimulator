import pygame
from abc import ABC, abstractmethod
from typing import Literal


class Widget(ABC):

    pos: pygame.Vector2
    dimensions: pygame.Vector2
    surface: pygame.Surface

    def __init__(self, pos: pygame.Vector2, dimensions: pygame.Vector2) -> None:
        self.pos = pos
        self.dimensions = dimensions
        self.surface = pygame.Surface((self.dimensions.x, self.dimensions.y))

    @abstractmethod
    def draw(self, surface: pygame.surface.Surface) -> None:
        print("[ERROR]: draw is not implemented")

    def is_mouse_hover(self) -> bool:
        mouse_pos = pygame.mouse.get_pos()

        return (
            self.pos.x <= mouse_pos[0] <= self.pos.x + self.dimensions.x
            and self.pos.y <= mouse_pos[1] <= self.pos.y + self.dimensions.y
        )

    def is_clicked(self, mouse_button: Literal[0, 1, 2]) -> bool:
        return (
            self.is_mouse_hover()
            and pygame.mouse.get_pressed(3)[mouse_button]
            and self.is_mouse_hover()
        )

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> None:
        print("[ERROR]: handle_event is not implemented")
