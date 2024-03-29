from typing import Callable
import pygame
from style import Style
from widget import Widget


class Button(Widget):

    on_click: Callable[[], None]
    label: str
    style: Style

    def __init__(
        self,
        pos: pygame.Vector2,
        dimensions: pygame.Vector2,
        parent: "Widget | None",
        on_click: Callable[[], None],
        label: str,
        style: Style,
    ) -> None:
        super().__init__(pos, dimensions, parent, None)
        self.on_click = on_click
        self.label = label
        self.style = style

    def draw(self, surface: pygame.Surface) -> None:
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
        pygame.draw.rect(
            self.surface,
            self.style.border_color,
            (0, 0, self.dimensions.x, self.dimensions.y),
            self.style.border_width,
            self.style.border_radius,
        )

        font = pygame.font.Font(None, self.style.font_size)
        text = font.render(self.label, True, self.style.text_color, None)
        text_rect = text.get_rect()
        text_rect.center = (int(self.dimensions.x / 2), int(self.dimensions.y / 2))
        self.surface.blit(text, text_rect)

        surface.blit(self.surface, self.pos)

    def append(self, widget: "Widget") -> None:
        pass

    def remove(self, widget: "Widget") -> None:
        pass

    def update(self) -> None:
        pass

    def handle_event(self, event: pygame.event.Event) -> None:
        if self.is_mouse_over() and event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
            self.on_click()
