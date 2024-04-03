from typing import Callable
from style import Style
from Widget import Widget
import pygame


class NumberInput(Widget):
    content: str = ""
    style: Style
    on_submit: Callable[[], None]
    get_state: Callable[[], str]
    set_state: Callable[[str], None]
    cursor_pos: int = 0

    def __init__(
        self,
        pos: pygame.Vector2,
        dimensions: pygame.Vector2,
        parent: "Widget | None",
        children: list["Widget"] | None,
        style: Style,
        on_submit: Callable[[], None],
        get_content: Callable[[], str],
        set_content: Callable[[str], None],
    ) -> None:
        super().__init__(pos, dimensions, parent, [])
        self.style = style
        self.on_submit = on_submit
        self.get_content = get_content
        self.set_content = set_content
        self.content = get_content()
        self.cursor_pos = len(self.content)

    def draw(self, surface: pygame.Surface) -> None:
        if self.focus:
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
        if self.focus:
            text = font.render(
                self.content[: self.cursor_pos] + "|" + self.content[self.cursor_pos :],
                True,
                self.style.text_color,
                None,
            )
        else:
            text = font.render(
                self.content,
                True,
                self.style.text_color,
                None,
            )
        text_rect = text.get_rect()
        text_rect.center = (int(self.dimensions.x / 2), int(self.dimensions.y / 2))

        self.surface.blit(text, text_rect)

        surface.blit(self.surface, self.pos)

    def handle_event(self, event: pygame.event.Event) -> None:
        match event.type:
            case pygame.MOUSEBUTTONDOWN:
                match self.is_mouse_over():
                    case True:
                        self.focus = True

                    case False:
                        self.focus = False

            case pygame.KEYDOWN:
                if self.focus:
                    match event.key:
                        case pygame.K_BACKSPACE:
                            if not len(self.content) == 0:
                                self.content = (
                                    self.content[: self.cursor_pos - 1]
                                    + self.content[self.cursor_pos :]
                                )
                                self.cursor_pos -= 1

                        case pygame.K_RETURN:
                            self.on_submit()
                            self.focus = False

                        case pygame.K_LEFT:
                            if not self.cursor_pos == 0:
                                self.cursor_pos -= 1

                        case pygame.K_RIGHT:
                            if not self.cursor_pos == len(self.content):
                                self.cursor_pos += 1

                        case _:
                            if event.unicode in "0123456789":
                                self.content = (
                                    self.content[: self.cursor_pos]
                                    + event.unicode
                                    + self.content[self.cursor_pos :]
                                )
                                self.cursor_pos += 1

                    self.set_content(self.content)

    def append(self, widget: "Widget") -> None:
        pass

    def update(self) -> None:
        pass

    def remove(self, widget: "Widget") -> None:
        pass
