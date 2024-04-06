from Clickable import Clickable
from pygame import Vector2
import pygame
from typing import Tuple, Callable
from Widget import Widget
from Style import Style


class Button(Clickable):
    style: Style
    label: str
    drawn: bool
    hover: bool

    def __init__(
        self,
        pos: Vector2 | Tuple[int, int],
        dimensions: Vector2 | Tuple[int, int],
        parent: Widget | None,
        on_click: Callable[[Clickable], None],
        label: str,
        style: Style,
    ) -> None:
        super().__init__(pos, dimensions, parent, on_click)

        self.drawn = False
        self.style = style
        self.label = label
        self.hover = False
        self.font = pygame.font.Font(None, self.style.text_size)

    def draw(self, surface: pygame.Surface) -> None:
        if not self.drawn or self.is_mouse_over() != self.hover:
            self.hover = self.is_mouse_over()

            self.surface.fill((0, 0, 0, 0))
            if self.is_mouse_over():
                pygame.draw.rect(
                    self.surface,
                    self.style.background_secondary_color,
                    (0, 0, self.dimensions.x, self.dimensions.y),
                    0,
                    self.style.border_radius,
                )
            else:
                pygame.draw.rect(
                    self.surface,
                    self.style.background_color,
                    (0, 0, self.dimensions.x, self.dimensions.y),
                    0,
                    self.style.border_radius,
                )

            text = self.font.render(self.label, True, self.style.text_color)
            text_rect = text.get_rect(center=self.surface.get_rect().center)
            self.surface.blit(text, text_rect)

            pygame.draw.rect(
                self.surface,
                self.style.border_color,
                (0, 0, self.dimensions.x, self.dimensions.y),
                self.style.border_width,
                self.style.border_radius,
            )

            self.drawn = True

        surface.blit(self.surface, self.pos)

    def handle_event(self, event) -> None:
        if event.type == pygame.MOUSEMOTION and self.is_mouse_over():
            self.drawn = False
        super().handle_event(event)

    def is_mouse_over(self) -> bool:
        mouse_pos = Vector2(pygame.mouse.get_pos())
        return (
            self.pos.x < mouse_pos.x < self.pos.x + self.dimensions.x
            and self.pos.y < mouse_pos.y < self.pos.y + self.dimensions.y
        )
