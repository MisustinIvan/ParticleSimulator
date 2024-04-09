from Widget import Widget
from typing import Union, Tuple, Callable
from pygame import Vector2, Surface, event, mouse
import pygame

from style import Style


class TextInput(Widget):
    focus: bool
    style: Style
    content: str
    cursor: int
    set_content: Callable[[str], None]

    def __init__(
        self,
        pos: Union[Vector2, Tuple[int, int]],
        dimensions: Union[Vector2, Tuple[int, int]],
        parent: "Widget | None",
        style: Style,
        set_content: Callable[[str], None],
    ) -> None:
        super().__init__(pos, dimensions, parent)

        self.set_content = set_content
        self.style = style
        self.font = pygame.font.Font(None, style.text_size)
        self.focus = False
        self.content = ""
        self.cursor = 0

    def draw(self, surface: Surface) -> None:
        self.surface.fill((0, 0, 0, 0))
        if self.is_mouse_over() or self.focus:
            pygame.draw.rect(
                self.surface,
                self.style.background_color,
                (0, 0, *self.dimensions),
                0,
                self.style.border_radius,
            )
        else:
            pygame.draw.rect(
                self.surface,
                self.style.background_secondary_color,
                (0, 0, *self.dimensions),
                0,
                self.style.border_radius,
            )

        pygame.draw.rect(
            self.surface,
            self.style.border_color,
            (0, 0, *self.dimensions),
            self.style.border_width,
            self.style.border_radius,
        )

        if self.focus:
            text = self.font.render(
                self.content[: self.cursor] + "|" + self.content[self.cursor :],
                True,
                self.style.text_color,
            )
        else:
            text = self.font.render(self.content, True, self.style.text_color)
        text_rect = text.get_rect()
        text_rect.center = self.surface.get_rect().center
        self.surface.blit(text, text_rect)

        surface.blit(self.surface, self.pos)

    def handle_event(self, event: event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_mouse_over():
                self.focus = True

            else:
                self.focus = False

        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_BACKSPACE:
                    if self.focus:
                        self.content = (
                            self.content[: self.cursor - 1]
                            + self.content[self.cursor :]
                        )
                        self.cursor = max(0, self.cursor - 1)

                case pygame.K_LEFT:
                    if self.focus:
                        self.cursor = max(0, self.cursor - 1)

                case pygame.K_RIGHT:
                    if self.focus:
                        self.cursor = min(len(self.content), self.cursor + 1)

                case _:
                    if self.focus:
                        self.content = (
                            self.content[: self.cursor]
                            + event.unicode
                            + self.content[self.cursor :]
                        )
                        self.cursor += 1
            if self.focus and self.content != "":
                self.set_content(self.content)
            if self.content == "" and self.focus:
                self.set_content("0")

    def is_mouse_over(self) -> bool:
        mouse_pos = Vector2(mouse.get_pos())
        return (
            self.pos.x < mouse_pos[0] < self.pos.x + self.dimensions.x
            and self.pos.y < mouse_pos[1] < self.pos.y + self.dimensions.y
        )
