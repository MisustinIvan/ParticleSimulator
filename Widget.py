from typing import Union, Tuple
from pygame import Vector2, Surface, event
from abc import ABC, abstractmethod


class Widget(ABC):
    surface: Surface
    pos: Vector2
    dimensions: Vector2
    parent: "Widget | None"
    accept_events: list[int]

    def __init__(
        self,
        pos: Union[Vector2, Tuple[int, int]],
        dimensions: Union[Vector2, Tuple[int, int]],
        parent: "Widget | None",
    ) -> None:
        self.pos = Vector2(pos)
        self.parent = parent
        self.dimensions = Vector2(dimensions)
        self.surface = Surface((self.dimensions.x, self.dimensions.y)).convert_alpha()

    @abstractmethod
    def handle_event(self, event: event.Event) -> None:
        print("[ERROR] handle_event method not implemented")

    @abstractmethod
    def is_mouse_over(self) -> bool:
        print("[ERROR] is_mouse_over method not implemented")

    @abstractmethod
    def draw(self, surface: Surface) -> None:
        print("[ERROR] draw method not implemented")
