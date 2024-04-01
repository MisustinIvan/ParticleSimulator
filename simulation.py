from typing import Callable
from particle import particle
from widget import Widget
import pygame


class Simulation:

    particles: list[particle]

    def __init__(self) -> None:
        pass

    def get_particles(self) -> list[particle]:
        return self.particles


class SimulationWidget(Widget):
    def __init__(
        self,
        pos: pygame.Vector2,
        dimensions: pygame.Vector2,
        parent: "Widget | None",
        children: list["Widget"] | None,
        get_particles: Callable[[], list[particle]],
    ) -> None:
        super().__init__(pos, dimensions, parent, children)
        self.get_particles = get_particles
        self.surface = pygame.Surface((int(dimensions.x), int(dimensions.y)))

    def draw(self, surface: pygame.Surface) -> None:
        self.surface.fill((0, 0, 0))

        for p in self.get_particles():
            pygame.draw.circle(self.surface, (255, 255, 255), p.pos, 5)

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
