from DynamicLabel import DynamicLabel
from HorizontalContainer import HorizontalContainer
from Label import Label
from VerticalContainer import VerticalContainer
import pygame
from Button import Button
from Style import Style
from electron import electron
from simulation import Simulation, SimulationWidget

pygame.init()


sim = Simulation()
sim.particles = [
    electron(pygame.Vector2(100, 100), pygame.Vector2(0, 0), pygame.Vector2(0, 0)),
    electron(pygame.Vector2(200, 200), pygame.Vector2(0, 0), pygame.Vector2(0, 0)),
    electron(pygame.Vector2(300, 300), pygame.Vector2(0, 0), pygame.Vector2(0, 0)),
]

default_style = Style(
    text_size=36,
    text_color=(255, 255, 255),
    background_color=(80, 80, 120),
    background_secondary_color=(120, 120, 180),
    border_color=(255, 255, 255),
    border_width=5,
    border_radius=10,
)


(WIDTH, HEIGHT) = (1200, 800)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

cnt = HorizontalContainer((0, 0), (WIDTH, HEIGHT), None, (255, 0, 0))

main_window = SimulationWidget((0, 0), (WIDTH - 400, HEIGHT), None, sim.get_particles)

side_menu = VerticalContainer((0, 0), (400, HEIGHT), None, (0, 255, 0))
side_menu.push(
    Label(
        pos=(0, 0),
        dimensions=(400, 50),
        parent=None,
        label="add a particle to the simulation:",
        align="left",
        style=default_style,
    )
)

side_menu.push(
    Button(
        pos=(0, 0),
        dimensions=(300, 100),
        parent=None,
        on_click=lambda self: sim.particles.append(
            electron(
                pygame.Vector2(400, 400), pygame.Vector2(0, 0), pygame.Vector2(0, 0)
            )
        ),
        label="Add Particle",
        style=default_style,
    )
)

side_menu.push(
    DynamicLabel(
        pos=(0, 0),
        dimensions=(400, 50),
        parent=None,
        get_label=lambda: f"Particles: {len(sim.particles)}",
        align="left",
        style=default_style,
    )
)

side_menu.push(
    DynamicLabel(
        pos=(0, 0),
        dimensions=(400, 50),
        parent=None,
        get_label=lambda: f"FPS: {int(clock.get_fps())}",
        align="left",
        style=default_style,
    )
)


def exit():
    pygame.quit()
    exit(0)


side_menu.push(
    Button(
        pos=(0, 0),
        dimensions=(100, 40),
        parent=None,
        on_click=lambda self: exit(),
        label="Exit",
        style=default_style,
    )
)

cnt.push(main_window)
cnt.push(side_menu)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                exit()

        cnt.handle_event(event)

    sim.update()
    screen.fill((0, 0, 0))

    cnt.draw(screen)
    print(clock.get_fps())

    pygame.display.flip()
    clock.tick(60)
