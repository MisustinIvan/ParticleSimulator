import sys
import pygame

from root import Root
from button import Button
from simulation import Simulation, SimulationWidget
from style import Style
from electron import electron
from positron import positron

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
(WIDTH, HEIGTH) = screen.get_size()

clock = pygame.time.Clock()


def main():
    base_style = Style(
        border_color=(255, 0, 0),
        border_width=2,
        border_radius=8,
        background_color=(40, 40, 40),
        background_secondary_color=(110, 110, 110),
        text_color=(255, 255, 255),
        font_size=56,
    )

    root = Root(
        pygame.Vector2(0, 0), pygame.Vector2(WIDTH, HEIGTH), None, [], "horizontal"
    )

    sim = Simulation()
    sim.particles = [
        electron(pygame.Vector2(0, 0), pygame.Vector2(0, 0), pygame.Vector2(0, 0)),
        electron(pygame.Vector2(100, 100), pygame.Vector2(0, 0), pygame.Vector2(0, 0)),
        positron(pygame.Vector2(-100, 100), pygame.Vector2(0, 0), pygame.Vector2(0, 0)),
    ]

    def get_particles():
        return sim.particles

    root.append(
        SimulationWidget(
            pos=pygame.Vector2(0, 0),
            dimensions=pygame.Vector2(int(WIDTH * 0.7), HEIGTH),
            parent=root,
            children=[],
            get_particles=get_particles,
        )
    )

    root.append(
        Root(
            pos=pygame.Vector2(0, 0),
            dimensions=pygame.Vector2(WIDTH * 0.3, HEIGTH),
            parent=root,
            children=[
                Button(
                    pos=pygame.Vector2(0, 0),
                    dimensions=pygame.Vector2(400, 100),
                    parent=None,
                    on_click=sim.toggle_running,
                    label="Toggle",
                    style=base_style,
                )
            ],
            direction="vertical",
        )
    )

    # root.children[1].append(
    #     Button(
    #         pygame.Vector2(0, 0),
    #         pygame.Vector2(300, 100),
    #         None,
    #         sim.toggle_running,
    #         "Pause",
    #         style=base_style,
    #     )
    # )

    # root.children[1].append(
    #     Button(
    #         pygame.Vector2(0, 0),
    #         pygame.Vector2(300, 100),
    #         None,
    #         sim.toggle_running,
    #         "Pause",
    #         style=base_style,
    #     )
    # )

    root.children[1].append(
        Button(
            pygame.Vector2(0, 0),
            pygame.Vector2(300, 100),
            None,
            sim.toggle_running,
            "Pause",
            style=base_style,
        )
    )

    while True:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                case pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            root.handle_event(event)

        sim.update()

        screen.fill((0, 0, 0))

        root.draw(screen)

        pygame.display.flip()
        clock.tick(60)


main()
