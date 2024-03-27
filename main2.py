from abc import abstractmethod
import sys
import pygame
from typing import Callable, Literal, Optional

from button import Button

pygame.init()

screen = pygame.display.set_mode((800, 600))


class App:

    def __init__(self) -> None:
        pass


def main():
    button = Button(
        pos=pygame.Vector2(100, 100),
        dimensions=pygame.Vector2(120, 50),
        on_click=lambda: print("Hello"),
        content="Button 1",
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE | event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

            button.handle_event(event)

        screen.fill((0, 0, 0))

        button.draw(screen)

        pygame.display.flip()


main()

