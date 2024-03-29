from typing import Literal
from widget import Widget
import pygame


class Root(Widget):
    direction: Literal["vertical", "horizontal"]

    def __init__(
        self,
        pos: pygame.Vector2,
        dimensions: pygame.Vector2,
        parent: "Widget | None",
        children: list["Widget"] | None,
        direction: Literal["vertical", "horizontal"],
    ) -> None:
        super().__init__(pos, dimensions, parent, children)
        self.direction = direction

    def draw(self, surface: pygame.Surface) -> None:
        self.surface.fill((0, 0, 0))
        pygame.draw.rect(
            self.surface,
            (255, 255, 255),
            (0, 0, self.dimensions.x, self.dimensions.y),
            2,
        )
        surface.blit(self.surface, self.pos)

        if self.children is not None:
            for child in self.children:
                child.draw(surface)

    def append(self, widget: "Widget") -> None:
        if self.children is None:
            widget.pos = self.pos + widget.pos
            self.children = [widget]
        else:
            match self.direction:
                case "vertical":
                    widget.pos = (
                        pygame.Vector2(0, self.children[-1].pos.y)
                        + pygame.Vector2(0, self.children[-1].dimensions.y)
                        + widget.pos
                    )
                    self.children.append(widget)
                case "horizontal":
                    widget.pos = (
                        pygame.Vector2(self.children[-1].pos.x, self.pos.y)
                        + pygame.Vector2(self.children[-1].dimensions.x, 0)
                        + widget.pos
                    )
                    self.children.append(widget)

    def remove(self, widget: "Widget") -> None:
        pass

    def update(self) -> None:
        pass

    def handle_event(self, event: pygame.event.Event) -> None:
        if self.children is not None:
            for child in self.children:
                child.handle_event(event)
