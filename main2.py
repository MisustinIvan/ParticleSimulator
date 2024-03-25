from abc import abstractmethod
import pygame
from typing import Callable

pygame.init()


screen = pygame.display.set_mode((800, 600))


class Widget:

    pos: pygame.Vector2
    dimensions: pygame.Vector2
    surface: pygame.Surface

    def __init__(self, pos: pygame.Vector2, dimensions: pygame.Vector2) -> None:
        self.pos = pos
        self.dimensions = dimensions
        self.surface = pygame.Surface((self.dimensions.x, self.dimensions.y))

    @abstractmethod
    def draw(self, surface: pygame.surface.Surface) -> None:
        pass


class Button(Widget):

    on_click: Callable[[None], None] | None = None

    def __init__(
        self, pos: pygame.Vector2, dimensions: pygame.Vector2, on_click: Callable[[None], None]
    ) -> None:
        super().__init__(pos, dimensions)
        self.on_click = on_click

    def draw(self, surface: pygame.surface.Surface) -> None:
        if pygame.mouse.get_pressed(3)[0]:
            self.surface.fill((0, 255, 0))
        else:
            self.surface.fill((255,0,0))
        surface.blit(self.surface, self.pos)


class App:

    def __init__(self) -> None:
        pass


def main():
    button = Button(
        pos=pygame.Vector2(100, 100),
        dimensions=pygame.Vector2(100, 50),
        on_click=lambda: print("Hello"),
    )

    button.on_click()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            screen.fill((0, 0, 0))

            button.draw(screen)

            pygame.display.flip()


main()