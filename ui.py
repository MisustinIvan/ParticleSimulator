from typing import Dict, List
from particle import particle
import pygame

def draw_save_menu(screen : pygame.Surface, saves : Dict[str, List[particle]], r : pygame.Rect, font : pygame.font.Font):
    pygame.draw.rect(screen, (45, 55, 70), r)

    i : int = 0
    for name, save in saves.items():
        text = font.render(name, True, (206, 223, 245))
        text_rect = text.get_rect()
        text_rect.topleft = (r.left + 8, r.top + 12 + (i*30))
        screen.blit(text, text_rect)
        
    

def draw_menu(screen : pygame.Surface ,particles : List['particle'], scroll : int, trace_mode : int, font : pygame.font.Font, r : pygame.Rect) -> None:
    # GOD WHAT IS THIS CODE -> DO NOT TOUCH
    pygame.draw.rect(screen, (45, 52, 61), r)
    i : int = 0
    for particle in particles:
        text = font.render(particle.__class__.__name__, True, (206, 223, 245))
        text_rect = text.get_rect()
        text_rect.topleft = (r.left + 8, 8 + (i*30) + scroll)

        if text_rect.centery + 10 < r.bottom and text_rect.centery > r.top:
            screen.blit(text, text_rect)
            p_pos = (text_rect.right + 16 ,text_rect.centery)
            pygame.draw.circle(screen, particle.draw_color, p_pos, 10)
    
    # GOD WHAT IS THIS CODE -> DO NOT TOUCH
        v_pos = (text_rect.right + 42 ,text_rect.centery)
        if v_pos[1] + 10 < r.bottom and text_rect.centery > r.top:
            if not particle.vel.length() == 0:
                pygame.draw.line(screen, (255, 255, 255), v_pos, v_pos + (particle.vel.normalize()*10), 2)
                pygame.draw.line(screen, (0, 255, 0), v_pos, v_pos + (particle.acc.normalize()*10), 2)
                pygame.draw.circle(screen, (255, 255, 255), v_pos, 12, 2)
            else:
                pygame.draw.circle(screen, (255, 255, 255), v_pos, 12, 2)
    
        if trace_mode and text_rect.centery + 10 < r.bottom and text_rect.centery > r.top:
            pygame.draw.line(screen, (255,255,255), (text_rect.left - 8, text_rect.centery), particle.pos)

        i += 1

        props = vars(particle)
        for prop, val in props.items():
            text = font.render(prop + " : " + str(val), True, (206, 223, 245))
            text_rect = text.get_rect()
            text_rect.topleft = (r.left + 8 + 16, 8 + (i*30) + scroll)
            if text_rect.centery + 10 < r.bottom and text_rect.centery > r.top:
                screen.blit(text, text_rect)
            i += 1

def draw_spd(screen : pygame.Surface, spd : int, font : pygame.font.Font) -> None:
    text = font.render("SPD : " + str(spd), True, (206, 223, 245))
    text_rect = text.get_rect()
    text_rect.topleft = (8, 8)
    screen.blit(text, text_rect)

def draw_cmd(screen : pygame.Surface, cmd_mode : float, cmd : str, font : pygame.font.Font, r : pygame.Rect) -> None:
    if cmd_mode:
        pygame.draw.rect(screen, (75, 82, 81), pygame.Rect(r.left, r.top, r.width, r.height))
    else:
        pygame.draw.rect(screen, (45, 52, 61), pygame.Rect(r.left, r.top, r.width, r.height))
    text = font.render("exec : " + cmd, True, (206, 223, 245))
    text_rect = text.get_rect()
    text_rect.topleft = (r.left + 8, r.top + 4)
    screen.blit(text, text_rect)
