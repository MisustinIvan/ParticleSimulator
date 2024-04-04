from typing import Tuple, Union
from Widget import Widget
import pygame
from pygame import Vector2
from pygame.event import Event
from abc import abstractmethod


class Container(Widget):
    background_debug_color: Tuple[int, int, int]
    children: list[Widget]

    def __init__(
        self,
        pos: Union[Vector2, Tuple[int, int]],
        dimensions: Union[Vector2, Tuple[int, int]],
        parent: Widget | None,
        background_debug_color: Tuple[int, int, int],
    ) -> None:
        super().__init__(pos, dimensions, parent)
        self.children = []

        self.background_debug_color = background_debug_color

    def handle_event(self, event: Event) -> None:
        for child in self.children:
            child.handle_event(event)

    def is_mouse_over(self) -> bool:
        pos = Vector2(pygame.mouse.get_pos())
        return (
            self.pos.x < pos.x
            and self.pos.x < self.pos.x + self.dimensions.x
            and self.pos.y < pos.y
            and self.pos.y < self.pos.y + self.dimensions.y
        )

    def draw(self, surface: pygame.Surface) -> None:
        self.surface.fill(self.background_debug_color)
        surface.blit(self.surface, self.pos)
        if self.children == []:
            return
        for child in self.children:
            child.draw(surface)

    @abstractmethod
    def push(self, widget: Widget) -> None:
        print("[ERROR] push method not implemented")

    @abstractmethod
    def pop(self) -> None:
        print("[ERROR] pop method not implemented")

    @abstractmethod
    def recompute_layout(self) -> None:
        print("[ERROR] recompute_layout method not implemented")
