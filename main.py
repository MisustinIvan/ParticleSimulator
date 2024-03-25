from typing import Dict, List
import pygame
import sys
from concurrent.futures import ThreadPoolExecutor
from ui import draw_menu, draw_spd, draw_cmd, draw_save_menu

spd: int = 10

CLR_TRACES: bool = False
CLR_TIMEOUT: int = 5
counter: int = 0
paused: bool = False
scroll: int = 0

cmd_mode: bool = False
cmd: str = ""

trace_mode: bool = False

from electron import electron
from positron import positron
from proton import proton
from particle import particle

pygame.init()

clock: pygame.time.Clock = pygame.time.Clock()
font: pygame.font.Font = pygame.font.Font(None, 30)


FPS: int = 60
WIDTH: int = 2500
HEIGTH: int = 1400

simulation_rect: pygame.Rect = pygame.Rect(0, 0, 2000, 1368)
menu_rect: pygame.Rect = pygame.Rect(2000, 0, 500, 1000)
cmd_rect: pygame.Rect = pygame.Rect(0, 1368, 2000, 32)
save_menu_rect: pygame.Rect = pygame.Rect(2000, 1000, 500, 400)

screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Particle simulation using Newtonean physics")

trace_buffer: pygame.Surface = pygame.Surface((2000, 1368))
trace_buffer.set_colorkey((0, 0, 0))
trace_buffer.convert_alpha()


# p : electron = electron(pygame.Vector2(WIDTH/2, HEIGTH/2), pygame.Vector2(0,0), pygame.Vector2(0,0))
# p.mass = 1.672e-27
# p.ee_charge = 1
# p.e_charge = p.e_charge*-1

saves: Dict[str, List[particle]] = {
    "Hydrogen molecule": [
        proton(pygame.Vector2(950, 700), pygame.Vector2(0, 0), pygame.Vector2(0, 0)),
        proton(pygame.Vector2(1050, 700), pygame.Vector2(0, 0), pygame.Vector2(0, 0)),
        electron(pygame.Vector2(1005, 715), pygame.Vector2(0, 0), pygame.Vector2(0, 0)),
        electron(pygame.Vector2(1000, 685), pygame.Vector2(0, 0), pygame.Vector2(0, 0)),
    ]
}

particles: List[particle] = saves["Hydrogen molecule"]

# particles : List[particle] = []


def place_electron() -> None:
    pos = pygame.mouse.get_pos()
    particles.append(
        electron(
            pygame.Vector2(pos[0], pos[1]), pygame.Vector2(0, 0), pygame.Vector2(0, 0)
        )
    )


def place_positron() -> None:
    pos = pygame.mouse.get_pos()
    particles.append(
        positron(
            pygame.Vector2(pos[0], pos[1]), pygame.Vector2(0, 0), pygame.Vector2(0, 0)
        )
    )


def place_proton() -> None:
    pos = pygame.mouse.get_pos()
    particles.append(
        proton(
            pygame.Vector2(pos[0], pos[1]), pygame.Vector2(0, 0), pygame.Vector2(0, 0)
        )
    )


def draw_particles() -> None:
    for p in particles:
        pygame.draw.circle(screen, p.draw_color, p.pos, p.draw_radius)


def draw_traces() -> None:
    for p in particles:
        pygame.draw.line(trace_buffer, (137, 250, 50, 50), p.pos, p.last_pos, 1)


def clear_traces(ctr) -> int:
    if ctr == CLR_TIMEOUT:
        trace_buffer.fill((0, 0, 0))
        return 0
    return ctr + 1


def set_spd(n) -> None:
    global spd
    spd = n


def calculate_particle_forces(particle: "particle") -> None:
    net_force: pygame.Vector2 = pygame.Vector2(0, 0)
    for other_particle in particles:
        net_force = net_force + particle.electric_interaction(other_particle)
    particle.acc = net_force / particle.mass
    particle.vel = particle.vel + (particle.acc * spd)


def update_particle(particle: "particle") -> None:
    if particle.pos.x < simulation_rect.left:
        particle.pos.x = simulation_rect.left + 1
        particle.vel.x = particle.vel.x * -0.9

    if particle.pos.x > simulation_rect.right:
        particle.pos.x = simulation_rect.right - 1
        particle.vel.x = particle.vel.x * -0.9

    if particle.pos.y < simulation_rect.top:
        particle.pos.y = simulation_rect.top + 1
        particle.vel.y = particle.vel.y * -0.9

    if particle.pos.y > simulation_rect.bottom:
        particle.pos.y = simulation_rect.bottom - 1
        particle.vel.y = particle.vel.y * -0.9

    particle.last_pos = particle.pos
    particle.pos = particle.pos + particle.vel


def update_particles() -> None:
    num_threads = 16

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [
            executor.submit(calculate_particle_forces, particle)
            for particle in particles
        ]

        for future in futures:
            future.result()

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(update_particle, particle) for particle in particles]

        for future in futures:
            future.result()


def calculate_total_energy() -> float:
    sum: float = 0
    for particle in particles:
        e_k: float = (particle.mass * particle.vel.magnitude_squared()) / 2
        sum += e_k

    return sum


def main() -> None:
    global counter
    global paused
    global scroll
    global cmd
    global cmd_mode
    global spd
    global trace_mode
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.KEYDOWN:

                if not cmd_mode:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

                    if event.key == pygame.K_e:
                        place_electron()

                    if event.key == pygame.K_r:
                        place_positron()

                    if event.key == pygame.K_d:
                        place_proton()

                    if event.key == pygame.K_c:
                        particles.clear()

                    if event.key == pygame.K_v:
                        trace_buffer.fill((0, 0, 0))

                    if event.key == pygame.K_SPACE:
                        paused = not paused

                    if event.key == pygame.K_t:
                        cmd_mode = True
                        break

                    if event.key == pygame.K_UP:
                        spd += 10

                    if event.key == pygame.K_DOWN:
                        if spd != 10:
                            spd -= 10

                    if event.key == pygame.K_m:
                        trace_mode = not trace_mode

                if cmd_mode:
                    if event.key == pygame.K_ESCAPE:
                        cmd_mode = False

                    elif event.key == pygame.K_BACKSPACE:
                        cmd = cmd[:-1]

                    elif event.key == pygame.K_RETURN:
                        try:
                            exec(cmd)
                            cmd = ""
                            cmd_mode = False
                        except Exception as e:
                            cmd = ""
                            cmd_mode = False
                            print(e)
                    else:
                        cmd += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4 and not scroll == 0:
                    scroll += 20
                if event.button == 5:
                    scroll -= 20

        if CLR_TRACES:
            counter = clear_traces(counter)
        screen.fill((59, 61, 66))

        draw_traces()
        screen.blit(trace_buffer, (0, 0))

        if not paused:
            update_particles()
        draw_particles()
        draw_menu(screen, particles, scroll, trace_mode, font, menu_rect)
        draw_spd(screen, spd, font)
        draw_save_menu(screen, saves, save_menu_rect, font)

        draw_cmd(screen, cmd_mode, cmd, font, cmd_rect)

        # print(calculate_total_energy())

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
