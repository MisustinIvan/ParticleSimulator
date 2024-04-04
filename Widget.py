from typing import Union
from pygame import Vector2, Surface, event
from abc import ABC, abstractmethod

from style import Tuple


class Widget(ABC):
    surface: Surface
    pos: Vector2
    dimensions: Vector2
    parent: "Widget | None"
    children: list["Widget"]

    def __init__(
        self,
        pos: Union[Vector2, Tuple[int, int]],
        dimensions: Union[Vector2, Tuple[int, int]],
        parent: "Widget | None",
        children: list["Widget"],
    ) -> None:
        self.pos = Vector2(pos)
        self.parent = parent
        self.children = children
        self.dimensions = Vector2(dimensions)
        self.surface = Surface((self.dimensions.x, self.dimensions.y))

    @abstractmethod
    def handle_event(self, event: event.Event) -> None:
        print("[ERROR] handle_event method not implemented")

    @abstractmethod
    def is_mouse_over(self) -> bool:
        print("[ERROR] is_mouse_over method not implemented")

    @abstractmethod
    def draw(self, surface: Surface) -> None:
        print("[ERROR] draw method not implemented")