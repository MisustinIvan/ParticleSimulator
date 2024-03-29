import pygame
from abc import ABC, abstractmethod
from typing import Literal


class Widget(ABC):

    surface: pygame.Surface

    pos: pygame.Vector2
    dimensions: pygame.Vector2
    parent: "Widget | None"
    children: list["Widget"] | None

    focus: bool = False

    def __init__(
        self,
        pos: pygame.Vector2,
        dimensions: pygame.Vector2,
        parent: "Widget | None",
        children: list["Widget"] | None,
    ) -> None:
        self.pos = pos
        self.dimensions = dimensions
        self.surface = pygame.Surface((self.dimensions.x, self.dimensions.y))
        self.parent = parent
        self.children = children

    def is_mouse_over(self) -> bool:
        mouse_pos = pygame.mouse.get_pos()
        return (
            self.pos.x < mouse_pos[0] < self.pos.x + self.dimensions.x
            and self.pos.y < mouse_pos[1] < self.pos.y + self.dimensions.y
        )

    @abstractmethod
    def draw(self, surface: pygame.Surface) -> None:
        print("[ERROR] draw method not implemented")

    @abstractmethod
    def append(self, widget: "Widget") -> None:
        print("[ERROR] append method not implemented")

    @abstractmethod
    def remove(self, widget: "Widget") -> None:
        print("[ERROR] remove method not implemented")

    @abstractmethod
    def update(self) -> None:
        print("[ERROR] update method not implemented")

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> None:
        print("[ERROR] handle_event method not implemented")
