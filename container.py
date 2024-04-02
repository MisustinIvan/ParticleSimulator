from pygame import Vector2
from pygame.event import Event
from widget import Widget
import pygame
from abc import abstractmethod


class Container(Widget):
    def __init__(
        self,
        pos: Vector2,
        dimensions: Vector2,
        parent: Widget | None,
        children: list[Widget],
    ) -> None:
        super().__init__(pos, dimensions, parent, [])

        for child in children:
            self.push(child)

    def handle_event(self, event: Event) -> None:
        for child in self.children:
            child.handle_event(event)

    def is_mouse_over(self) -> bool:
        pos = pygame.mouse.get_pos()
        return (
            self.pos.x < pos.x
            and self.pos.x < self.pos.x + self.dimensions.x
            and self.pos.y < pos.y
            and self.pos.y < self.pos.y + self.dimensions.y
        )

    def draw(self, surface: pygame.Surface) -> None:
        self.surface.fill((255, 255, 255))
        surface.blit(self.surface, self.pos)

        for child in self.children:
            child.draw(surface)

    @abstractmethod
    def push(self, widget: Widget) -> None:
        print("[ERROR] push method not implemented")

    @abstractmethod
    def pop(self) -> None:
        print("[ERROR] pop method not implemented")


class VerticalContainer(Container):
    def __init__(
        self,
        pos: Vector2,
        dimensions: Vector2,
        parent: Widget | None,
        children: list[Widget],
    ) -> None:
        super().__init__(pos, dimensions, parent, children)

    def push(self, widget: Widget) -> None:
        widget.parent = self

        if self.children == []:
            widget.pos += self.pos + pygame.Vector2(0, 50)
            self.children.append(widget)

        else:
            widget.pos += (
                self.children[-1].pos
                + pygame.Vector2(0, self.children[-1].dimensions.y)
                + pygame.Vector2(0, 50)
            )
            self.children.append(widget)

    def pop(self) -> None:
        self.children = self.children[:-1]


cnt = VerticalContainer(
    pygame.Vector2(0, 0),
    pygame.Vector2(200, 100),
    None,
    [
        VerticalContainer(pygame.Vector2(0, 0), pygame.Vector2(50, 500), None, []),
        VerticalContainer(pygame.Vector2(0, 0), pygame.Vector2(50, 500), None, []),
    ],
)

print(cnt)

pygame.init()

screen = pygame.display.set_mode((800, 800))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 255))

    cnt.draw(screen)

    pygame.display.flip()
