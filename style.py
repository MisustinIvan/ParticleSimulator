from typing import Tuple


class Style:
    text_size: int
    text_color: Tuple[int, int, int]
    background_color: Tuple[int, int, int]
    background_secondary_color: Tuple[int, int, int]
    border_color: Tuple[int, int, int]
    border_width: int
    border_radius: int

    def __init__(
        self,
        text_size: int,
        text_color: Tuple[int, int, int],
        background_color: Tuple[int, int, int],
        background_secondary_color: Tuple[int, int, int],
        border_color: Tuple[int, int, int],
        border_width: int,
        border_radius: int,
    ) -> None:
        self.border_color = border_color
        self.border_width = border_width
        self.border_radius = border_radius
        self.background_color = background_color
        self.background_secondary_color = background_secondary_color
        self.text_color = text_color
        self.text_size = text_size
