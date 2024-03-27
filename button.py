from typing import Callable
import pygame
from widget import Widget


class Button(Widget):

    on_click: Callable[[], None]
    content: str

    def __init__(
        self,
        pos: pygame.Vector2,
        dimensions: pygame.Vector2,
        on_click: Callable[[], None],
        content: str,
    ) -> None:
        super().__init__(pos, dimensions)
        self.on_click = on_click
        self.content = content

    def draw(self, surface: pygame.surface.Surface) -> None:
        if self.is_clicked(0):
            self.surface.fill((0, 0, 255))
        else:
            if self.is_mouse_hover():
                self.surface.fill((0, 255, 0))
            else:
                self.surface.fill((255, 0, 0))

        font = pygame.font.Font(None, 36)
        text = font.render(self.content, True, (255, 255, 255))
        text_rect = text.get_rect(
            center=(self.dimensions.x // 2, self.dimensions.y // 2)
        )
        self.surface.blit(text, text_rect)

        surface.blit(self.surface, self.pos)

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and self.is_clicked(0):
            self.on_click()
