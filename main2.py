import sys
import pygame

from number_input import NumberInput
from root import Root
from button import Button
from style import Style
from text_input import TextInput

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
(WIDTH, HEIGTH) = screen.get_size()


def main():

    state = "test"

    def get_state() -> str:
        nonlocal state
        return state

    def set_state(s: str):
        nonlocal state
        state = s

    root = Root(
        pygame.Vector2(0, 0), pygame.Vector2(WIDTH, HEIGTH), None, None, "horizontal"
    )
    root.append(
        Button(
            pos=pygame.Vector2(0, 0),
            dimensions=pygame.Vector2(200, 100),
            parent=None,
            on_click=lambda: print("Button 1 clicked"),
            label="Button 1",
            style=Style(
                border_color=(255, 255, 255),
                border_width=8,
                border_radius=0,
                background_color=(80, 80, 80),
                background_secondary_color=(110, 110, 110),
                text_color=(255, 0, 0),
                font_size=60,
            ),
        )
    )

    root.append(
        Button(
            pos=pygame.Vector2(0, 0),
            dimensions=pygame.Vector2(200, 100),
            parent=None,
            on_click=lambda: print("Button 2 clicked"),
            label="Button 2",
            style=Style(
                border_color=(255, 255, 255),
                border_width=8,
                border_radius=0,
                background_color=(80, 80, 80),
                background_secondary_color=(110, 110, 110),
                text_color=(255, 255, 255),
                font_size=40,
            ),
        )
    )

    root.append(
        Button(
            pos=pygame.Vector2(0, 0),
            dimensions=pygame.Vector2(200, 100),
            parent=None,
            on_click=lambda: print("Button 3 clicked"),
            label="Button 3",
            style=Style(
                border_color=(255, 255, 255),
                border_width=4,
                border_radius=10,
                background_color=(80, 0, 80),
                background_secondary_color=(110, 110, 110),
                text_color=(255, 255, 255),
                font_size=40,
            ),
        )
    )

    root.append(
        TextInput(
            pos=pygame.Vector2(0, 0),
            dimensions=pygame.Vector2(400, 100),
            parent=None,
            children=None,
            style=(
                Style(
                    border_color=(255, 255, 255),
                    border_width=2,
                    border_radius=8,
                    background_color=(80, 80, 80),
                    background_secondary_color=(110, 110, 110),
                    text_color=(255, 255, 255),
                    font_size=50,
                )
            ),
            on_submit=lambda: print(state),
            get_content=get_state,
            set_content=set_state,
        )
    )

    number = 123

    def set_number(val: str) -> None:
        nonlocal number
        if not val == "":
            number = int(val)

    def get_number() -> str:
        nonlocal number
        return str(number)

    root.append(
        NumberInput(
            pos=pygame.Vector2(0, 0),
            dimensions=pygame.Vector2(300, 80),
            parent=None,
            children=None,
            style=Style(
                border_color=(255, 255, 255),
                border_width=2,
                border_radius=8,
                background_color=(80, 80, 80),
                background_secondary_color=(110, 110, 110),
                text_color=(255, 255, 255),
                font_size=50,
            ),
            on_submit=lambda: print(get_number()),
            get_content=get_number,
            set_content=set_number,
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
