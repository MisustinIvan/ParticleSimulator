from typing import Callable, Literal, Tuple
from pygame import Vector2
import pygame
from pygame.event import Event
from Widget import Widget
from Style import Style


class DynamicLabel(Widget):
    style: Style
    align: Literal["left", "center", "right"]

    def __init__(
        self,
        pos: Vector2 | Tuple[int, int],
        dimensions: Vector2 | Tuple[int, int],
        parent: Widget | None,
        get_label: Callable[[], str],
        align: Literal["left", "center", "right"],
        style: Style,
    ) -> None:
        super().__init__(pos, dimensions, parent)

        self.align = align
        self.style = style
        self.get_label = get_label

    def draw(self, surface: pygame.Surface) -> None:
        self.surface.fill((0, 0, 0, 0))

        font = pygame.font.Font(None, self.style.text_size)
        text = font.render(self.get_label(), True, self.style.text_color)
        text_rect = text.get_rect()

        match self.align:
            case "left":
                text_rect.left = 0
                text_rect.centery = self.surface.get_rect().centery
            case "center":
                text_rect.center = self.surface.get_rect().center
            case "right":
                text_rect.right = self.surface.get_rect().right
                text_rect.centery = self.surface.get_rect().centery

        self.surface.blit(text, text_rect)

        surface.blit(self.surface, self.pos)

    def handle_event(self, event: Event) -> None:
        pass

    def is_mouse_over(self) -> bool:
        mouse_pos = Vector2(pygame.mouse.get_pos())
        return (
            self.pos.x < mouse_pos[0] < self.pos.x + self.dimensions.x
            and self.pos.y < mouse_pos[1] < self.pos.y + self.dimensions.y
        )
