from typing import Callable, Tuple

from particle import particle
from Widget import Widget
import pygame


class Simulation:
    particles: list[particle]
    running: bool = True

    def __init__(self) -> None:
        pass

    def get_particles(self) -> list[particle]:
        return self.particles

    def pause(self) -> None:
        self.running = False

    def play(self) -> None:
        self.running = True

    def toggle_running(self) -> None:
        self.running = not self.running

    def update(self) -> None:
        if self.running:
            for particle in self.particles:
                f = pygame.Vector2(0, 0)
                for other in self.particles:
                    f += particle.calculate_forces(other)

                particle.acc = f / particle.mass

            for particle in self.particles:
                particle.vel += particle.acc
                particle.pos += particle.vel


class SimulationWidget(Widget):
    get_particles: Callable[[], list[particle]]

    def __init__(
        self,
        pos: pygame.Vector2 | Tuple[int],
        dimensions: pygame.Vector2 | Tuple[int],
        parent: Widget | None,
        get_particles: Callable[[], list[particle]],
    ) -> None:
        super().__init__(pos, dimensions, parent)

        self.get_particles = get_particles

    def draw(self, surface: pygame.Surface) -> None:
        self.surface.fill((0, 0, 0, 255))

        for p in self.get_particles():
            pygame.draw.circle(
                self.surface,
                (255, 255, 255),
                (int(p.pos.x), int(p.pos.y)),
                8,
            )

        surface.blit(self.surface, self.pos)

    def handle_event(self, event: pygame.event.Event) -> None:
        pass

    def is_mouse_over(self) -> bool:
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        return (
            self.pos.x < mouse_pos[0] < self.pos.x + self.dimensions.x
            and self.pos.y < mouse_pos[1] < self.pos.y + self.dimensions.y
        )
