from typing import Callable
from old.particle import particle
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
    def __init__(
        self,
        pos: pygame.Vector2,
        dimensions: pygame.Vector2,
        parent: "Widget | None",
        children: list["Widget"],
        get_particles: Callable[[], list[particle]],
    ) -> None:
        super().__init__(pos, dimensions, parent, children)
        self.get_particles = get_particles
        self.surface = pygame.Surface((int(dimensions.x), int(dimensions.y)))

    def draw(self, surface: pygame.Surface) -> None:
        self.surface.fill((0, 0, 0))

        for p in self.get_particles():
            pygame.draw.circle(
                self.surface,
                p.draw_color,
                p.pos + self.dimensions / 2,
                p.draw_radius,
            )

        pygame.draw.rect(self.surface, (255, 255, 255), (0, 0, *self.dimensions), 2)

        surface.blit(self.surface, self.pos)

    def update(self) -> None:
        pass

    def handle_event(self, event: pygame.event.Event) -> None:
        pass

    def on_click(self) -> None:
        pass

    def append(self, widget: "Widget") -> None:
        pass

    def remove(self, widget: "Widget") -> None:
        pass
