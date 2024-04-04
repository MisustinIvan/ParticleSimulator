from Container import Container
from typing import Tuple, Union
from Widget import Widget
from pygame import Vector2


class VerticalContainer(Container):
    def __init__(
        self,
        pos: Union[Vector2, Tuple[int, int]],
        dimensions: Union[Vector2, Tuple[int, int]],
        parent: Widget | None,
        background_debug_color: Tuple[int, int, int],
    ) -> None:
        super().__init__(pos, dimensions, parent, background_debug_color)

    def recompute_layout(self) -> None:
        pass

    def push(self, widget: Widget) -> None:
        widget.parent = self

        if self.children == []:
            widget.pos += self.pos
        else:
            widget.pos += Vector2(
                0, self.children[-1].dimensions.y + self.children[-1].pos.y
            )
        self.children.append(widget)

    def pop(self) -> None:
        self.children = self.children[:-1]
