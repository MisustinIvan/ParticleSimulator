from typing import Union
from pygame import Vector2
from pygame.event import Event
from style import Tuple
from widget import Widget
from abc import abstractmethod
import pygame


class Container(Widget):

    background_debug_color: Tuple[int, int, int]

    def __init__(
        self,
        pos: Union[Vector2, Tuple[int, int]],
        dimensions: Union[Vector2, Tuple[int, int]],
        parent: Widget | None,
        children: list[Widget],
        background_debug_color: Tuple[int, int, int],
    ) -> None:
        super().__init__(pos, dimensions, parent, [])

        self.background_debug_color = background_debug_color

        for child in children:
            self.push(child)

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

        for child in self.children:
            child.draw(self.surface)

        surface.blit(self.surface, self.pos)

    @abstractmethod
    def push(self, widget: Widget) -> None:
        print("[ERROR] push method not implemented")

    @abstractmethod
    def pop(self) -> None:
        print("[ERROR] pop method not implemented")


class VerticalSplit(Container):

    ratio: float

    def __init__(
        self,
        pos: Union[Vector2, Tuple[int, int]],
        dimensions: Union[Vector2, Tuple[int, int]],
        parent: Widget | None,
        children: Tuple[Widget, Widget],
        background_debug_color: Tuple[int, int, int],
        ratio: float,
    ) -> None:
        self.ratio = ratio
        super().__init__(
            pos, dimensions, parent, list(children), background_debug_color
        )

    def push(self, widget: Widget) -> None:
        widget.parent = self

        if self.children == []:
            widget.pos += self.pos
            widget.dimensions = Vector2(
                self.dimensions.x * 0.5,
                self.dimensions.y,
            )

            widget.surface = pygame.Surface(widget.dimensions)

            self.children.append(widget)

        else:
            widget.pos += self.children[-1].pos + Vector2(
                self.children[-1].dimensions.y, 0
            )
            widget.dimensions = Vector2(self.dimensions.x * 0.5, self.dimensions.y)
            widget.surface = pygame.Surface(widget.dimensions)
            self.children.append(widget)

    def pop(self) -> None:
        self.children = self.children[:-1]


class VerticalContainer(Container):
    def __init__(
        self,
        pos: Union[Vector2, Tuple[int, int]],
        dimensions: Union[Vector2, Tuple[int, int]],
        parent: Widget | None,
        children: list[Widget],
        background_debug_color: Tuple[int, int, int],
    ) -> None:
        super().__init__(pos, dimensions, parent, children, background_debug_color)

    def push(self, widget: Widget) -> None:
        widget.parent = self

        if self.children == []:
            widget.pos += self.pos
            self.children.append(widget)

        else:
            widget.pos += self.children[-1].pos + Vector2(
                0, self.children[-1].dimensions.y
            )
            self.children.append(widget)

    def pop(self) -> None:
        self.children = self.children[:-1]


class HorizontalContainer(Container):
    def __init__(
        self,
        pos: Union[Vector2, Tuple[int, int]],
        dimensions: Union[Vector2, Tuple[int, int]],
        parent: Widget | None,
        children: list[Widget],
        background_debug_color: Tuple[int, int, int],
    ) -> None:
        super().__init__(pos, dimensions, parent, children, background_debug_color)

    def push(self, widget: Widget) -> None:
        widget.parent = self

        if self.children == []:
            widget.pos += self.pos
            self.children.append(widget)
        else:
            widget.pos += self.children[-1].pos + Vector2(
                self.children[-1].dimensions.x, 0
            )
            self.children.append(widget)

    def pop(self) -> None:
        self.children = self.children[:-1]


cnt = VerticalSplit(
    (0, 0),
    (400, 400),
    None,
    (
        VerticalContainer(
            (0, 0),
            (50, 500),
            None,
            [],
            (255, 0, 0),
        ),
        VerticalContainer(
            (0, 0),
            (50, 500),
            None,
            [],
            (0, 255, 0),
        ),
    ),
    (255, 255, 255),
    ratio=0.5,
)

print(cnt.children[0].pos)
print(cnt.children[1].pos)

pygame.init()

screen = pygame.display.set_mode((800, 800))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                exit()

    screen.fill((0, 0, 255))

    cnt.draw(screen)

    pygame.display.flip()
