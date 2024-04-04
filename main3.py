from HorizontalContainer import HorizontalContainer
from VerticalContainer import VerticalContainer
import pygame

(WIDTH, HEIGHT) = (1200, 800)

cnt = HorizontalContainer((0, 0), (WIDTH, HEIGHT), None, (255, 0, 0))

main_window = HorizontalContainer((0, 0), (WIDTH - 400, HEIGHT), None, (0, 0, 255))
main_window.push(VerticalContainer((0, 0), (300, 600), None, (255, 0, 255)))
main_window.push(VerticalContainer((0, 0), (300, 600), None, (255, 120, 255)))

side_menu = VerticalContainer((0, 0), (400, HEIGHT), None, (0, 255, 0))


side_menu.push(VerticalContainer((0, 0), (300, 300), None, (255, 0, 255)))
side_menu.push(VerticalContainer((0, 0), (200, 100), None, (100, 100, 255)))

side_menu.children[0].push(VerticalContainer((0, 0), (100, 100), None, (255, 255, 0)))
side_menu.children[0].push(VerticalContainer((0, 0), (100, 100), None, (255, 255, 100)))

cnt.push(main_window)
cnt.push(side_menu)

print(side_menu.pos)

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
