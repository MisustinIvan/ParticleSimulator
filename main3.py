from HorizontalContainer import HorizontalContainer
from VerticalContainer import VerticalContainer
import pygame
from Widget import Widget

(WIDTH, HEIGHT) = (1200, 800)

cnt = VerticalContainer(
    pos=(0, 0),
    dimensions=(WIDTH, HEIGHT),
    parent=None,
    children=[
        HorizontalContainer(
            pos=(0, 0),
            dimensions=(WIDTH, int(HEIGHT * 0.8)),
            parent=None,
            children=[
                VerticalContainer(
                    pos=(0, 0),
                    dimensions=(WIDTH / 2, HEIGHT * 0.8),
                    parent=None,
                    children=[],
                    background_debug_color=(255, 255, 100),
                ),
                VerticalContainer(
                    pos=(0, 0),
                    dimensions=(WIDTH / 2, HEIGHT * 0.8),
                    parent=None,
                    children=[
                        VerticalContainer(
                            pos=(0, 0),
                            dimensions=(WIDTH / 2, HEIGHT * 0.4),
                            parent=None,
                            children=[],
                            background_debug_color=(100, 255, 100),
                        ),
                        #         # VerticalContainer(
                        #         #     pos=(0, 0),
                        #         #     dimensions=(WIDTH / 2, HEIGHT * 0.4),
                        #         #     parent=None,
                        #         #     children=[],
                        #         #     background_debug_color=(100, 200, 200),
                        #         # ),
                    ],
                    background_debug_color=(100, 100, 100),
                ),
            ],
            background_debug_color=(100, 100, 100),
        ),
        HorizontalContainer(
            pos=(0, 0),
            dimensions=(WIDTH, HEIGHT * 0.2),
            parent=None,
            children=[],
            background_debug_color=(100, 255, 100),
        ),
    ],
    background_debug_color=(255, 255, 255),
)


def update_children_pos(widget: Widget) -> None:
    for child in widget.children:
        child.pos += widget.pos
        update_children_pos(child)


update_children_pos(cnt)

print(cnt.children[0].children[1].children[0].pos)

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
