import cProfile
import pstats
import sys
from DynamicLabel import DynamicLabel
from HorizontalContainer import HorizontalContainer
from Label import Label
from TextInput import TextInput
from VerticalContainer import VerticalContainer
import pygame
from button import Button
from style import Style
from electron import electron
from simulation import Simulation, SimulationWidget

pygame.init()


default_style = Style(
    text_size=36,
    text_color=(255, 255, 255),
    background_color=(80, 80, 120),
    background_secondary_color=(120, 120, 180),
    border_color=(255, 255, 255),
    border_width=5,
    border_radius=10,
)


# (WIDTH, HEIGHT) = (2560, 1600)
(WIDTH, HEIGHT) = (2200, 1200)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

cnt = HorizontalContainer((0, 0), (WIDTH, HEIGHT), None, default_style.background_color)

sim = Simulation(pygame.Vector2(WIDTH - 400, HEIGHT))
sim.particles = [
    electron(pygame.Vector2(300, 300), pygame.Vector2(0, 0), pygame.Vector2(0, 0), []),
    electron(
        pygame.Vector2(100, 100), pygame.Vector2(0, 0), pygame.Vector2(0, 0), ["static"]
    ),
    electron(pygame.Vector2(200, 200), pygame.Vector2(0, 0), pygame.Vector2(0, 0), []),
]
main_window = SimulationWidget((0, 0), (WIDTH - 400, HEIGHT), None, sim.get_particles)

# main_window = SimulationWidget((0, 0), (WIDTH - 400, HEIGHT), None, lambda: [])

side_menu = VerticalContainer(
    (0, 0), (400, HEIGHT), None, default_style.background_color
)
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

partice_append_pos_x: int = 0
partice_append_pos_y: int = 0


def set_particle_append_pos_x(i: str):
    global partice_append_pos_x
    partice_append_pos_x = int(i)


def set_particle_append_pos_y(i: str):
    global partice_append_pos_y
    partice_append_pos_y = int(i)


side_menu.push(
    Label(
        pos=(0, 0),
        dimensions=(400, 50),
        parent=None,
        label="X:",
        align="left",
        style=default_style,
    )
)

side_menu.push(
    TextInput(
        pos=(0, 0),
        dimensions=(400, 50),
        parent=None,
        style=default_style,
        set_content=set_particle_append_pos_x,
    )
)


side_menu.push(
    Label(
        pos=(0, 0),
        dimensions=(400, 50),
        parent=None,
        label="Y:",
        align="left",
        style=default_style,
    )
)

side_menu.push(
    TextInput(
        pos=(0, 0),
        dimensions=(400, 50),
        parent=None,
        style=default_style,
        set_content=set_particle_append_pos_y,
    )
)

side_menu.push(
    Button(
        pos=(0, 0),
        dimensions=(300, 100),
        parent=None,
        on_click=lambda: sim.particles.append(
            electron(
                pygame.Vector2(partice_append_pos_x, partice_append_pos_y),
                pygame.Vector2(0, 0),
                pygame.Vector2(0, 0),
                [],
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
        # get_label=lambda: f"Particles",
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


# def get_first_particle_vel() -> float:
#    return sim.particles[0].vel.magnitude()
#
#
# side_menu.push(
#    DynamicLabel(
#        pos=(0, 0),
#        dimensions=(400, 50),
#        parent=None,
#        get_label=lambda: f"First Particle Vel: {get_first_particle_vel()}",
#        align="left",
#        style=default_style,
#    )
# )
#


def exit():
    pygame.quit()
    sys.exit(0)


side_menu.push(
    Button(
        pos=(10, 0),
        dimensions=(200, 60),
        parent=None,
        on_click=exit,
        label="Exit",
        style=default_style,
    )
)

side_menu.push(
    Button(
        pos=(10, 10),
        dimensions=(200, 60),
        parent=None,
        on_click=sim.toggle_running,
        label="Pause",
        style=default_style,
    )
)


def add_magic():
    side_menu.push(
        Label(
            pos=(0, 0),
            dimensions=(400, 50),
            parent=None,
            label="Magic!",
            align="left",
            style=default_style,
        )
    )


side_menu.push(
    Button(
        pos=(10, 10),
        dimensions=(200, 60),
        parent=None,
        on_click=add_magic,
        label="Secret",
        style=default_style,
    )
)

side_menu.push(
    Button(
        pos=(10, 10),
        dimensions=(200, 60),
        parent=None,
        on_click=side_menu.pop,
        label="Poof",
        style=default_style,
    )
)


cnt.push(main_window)
cnt.push(side_menu)

clock = pygame.time.Clock()


def main():
    last_time = pygame.time.get_ticks()
    delta_time = 0

    while True:
        # for event in pygame.event.get(exclude=(pygame.MOUSEMOTION,)):
        for event in pygame.event.get():
            # print(event)

            if event.type == pygame.QUIT:
                profiler.disable()
                stats = pstats.Stats(profiler)
                stats.dump_stats("profile.prof")

                pygame.quit()
                exit()

            cnt.handle_event(event)

        now = pygame.time.get_ticks()
        delta_time = now - last_time
        last_time = now

        sim.update(delta_time)
        # screen.fill((0, 0, 0))

        cnt.draw(screen)
        # print(clock.get_fps())

        pygame.display.flip()
        clock.tick(60)


profiler = cProfile.Profile()
profiler.enable()
main()
profiler.disable()
stats = pstats.Stats(profiler)
stats.dump_stats("profile.prof")
