import pygame
from abc import ABC, abstractmethod


class Widget(ABC):
    surface: pygame.Surface
    pos: pygame.Vector2
    dimensions: pygame.Vector2
    parent: "Widget | None"
    children: list["Widget"]

    def __init__(
        self,
        pos: pygame.Vector2,
        dimensions: pygame.Vector2,
        parent: "Widget | None",
        children: list["Widget"],
    ) -> None:
        self.pos = pos
        self.parent = parent
        self.children = children
        self.dimensions = dimensions
        self.surface = pygame.Surface((self.dimensions.x, self.dimensions.y))

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> None:
        print("[ERROR] handle_event method not implemented")

    @abstractmethod
    def is_mouse_over(self) -> bool:
        print("[ERROR] is_mouse_over method not implemented")

    @abstractmethod
    def draw(self, surface: pygame.Surface) -> None:
        print("[ERROR] draw method not implemented")
