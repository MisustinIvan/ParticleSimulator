from typing import Tuple


class Style:

    border_color: Tuple[int, int, int]
    border_width: int
    border_radius: int
    background_color: Tuple[int, int, int]
    background_secondary_color: Tuple[int, int, int]
    text_color: Tuple[int, int, int]
    font_size: int
    padding: Tuple[int, int]

    def __init__(
        self,
        border_color: Tuple[int, int, int],
        border_width: int,
        border_radius: int,
        background_color: Tuple[int, int, int],
        background_secondary_color: Tuple[int, int, int],
        text_color: Tuple[int, int, int],
        font_size: int,
        padding: Tuple[int, int],
    ) -> None:
        self.border_color = border_color
        self.border_width = border_width
        self.border_radius = border_radius
        self.background_color = background_color
        self.background_secondary_color = background_secondary_color
        self.text_color = text_color
        self.font_size = font_size
        self.padding: Tuple[int, int]
