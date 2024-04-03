from HorizontalContainer import HorizontalContainer
from VerticalContainer import VerticalContainer
from container import Container
import pygame


(WIDTH, HEIGHT) = (1200, 800)

cnt = VerticalContainer(
    pos=(0, 0),
    dimensions=(WIDTH, HEIGHT),
    parent=None,
    children=[
        HorizontalContainer(
            pos=(0, 0),
            dimensions=(WIDTH, HEIGHT * 0.8),
            parent=None,
            children=[
                VerticalContainer(
                    pos=(0, 0),
                    dimensions=(WIDTH / 2, HEIGHT * 0.8),
                    parent=None,
                    children=[],
                    background_debug_color=(200, 200, 100),
                ),
                VerticalContainer(
                    pos=(0, 0),
                    dimensions=(WIDTH / 2, HEIGHT * 0.8),
                    parent=None,
                    children=[],
                    background_debug_color=(100, 100, 200),
                ),
            ],
            background_debug_color=(200, 100, 100),
        ),
        HorizontalContainer(
            pos=(0, 0),
            dimensions=(WIDTH, HEIGHT * 0.2),
            parent=None,
            children=[],
            background_debug_color=(100, 200, 100),
        ),
    ],
    background_debug_color=(255, 255, 255),
)

print(isinstance(cnt, Container))

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                exit()

    screen.fill((0, 0, 0))

    cnt.draw(screen)

    pygame.display.flip()
