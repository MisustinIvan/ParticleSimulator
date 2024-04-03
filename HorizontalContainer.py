from container import Container
from typing import Tuple, Union
from widget import Widget


from pygame import Vector2


class HorizontalContainer(Container):
    def __init__(
        self,
        pos: Union[Vector2, Tuple[int, int]],
        dimensions: Union[Vector2, Tuple[int, int]],
        parent: Widget | None,
        children: list[Widget],
        background_debug_color: Tuple[int, int, int],
    ) -> None:
        super().__init__(pos, dimensions, parent, children, background_debug_color)

    def push(self, widget: Widget) -> None:
        widget.parent = self

        def update_children_pos(widget: Widget) -> None:
            for child in widget.children:
                child.pos += widget.pos
                update_children_pos(child)

        if self.children == []:
            widget.pos += self.pos
            update_children_pos(widget)
            self.children.append(widget)
        else:
            widget.pos += Vector2(
                self.children[-1].dimensions.x + self.children[-1].pos.x, 0
            )
            update_children_pos(widget)
            self.children.append(widget)

    def pop(self) -> None:
        self.children = self.children[:-1]
