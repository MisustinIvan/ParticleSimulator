import sys
import pygame

from number_input import NumberInput
from root import Root
from button import Button
from simulation import Simulation, SimulationWidget
from style import Style
from text_input import TextInput
from electron import electron

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
(WIDTH, HEIGTH) = screen.get_size()


def main():

    state = "test"

    root = Root(
        pygame.Vector2(0, 0), pygame.Vector2(WIDTH, HEIGTH), None, None, "horizontal"
    )

    sim = Simulation()
    sim.particles = [
        electron(pygame.Vector2(100, 100), pygame.Vector2(0, 0), pygame.Vector2(0, 0))
    ]

    def get_particles():
        return sim.particles

    root.append(
        SimulationWidget(
            pos=pygame.Vector2(0, 0),
            dimensions=pygame.Vector2(int(WIDTH * 0.7), HEIGTH),
            parent=root,
            children=None,
            get_particles=get_particles,
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

        screen.fill((0, 0, 0))

        root.draw(screen)

        pygame.display.flip()


main()
