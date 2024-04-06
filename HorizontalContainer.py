from Container import Container
from typing import Tuple, Union
from Widget import Widget
from pygame import Vector2


class HorizontalContainer(Container):
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
                self.children[-1].dimensions.x + self.children[-1].pos.x, 0
            )

        # God lent me his infinite wisdom during the creation of this recursive sin
        def update_children_pos(widget: Widget) -> None:
            if "children" in dir(widget):
                for child in widget.children:
                    child.pos += widget.pos
                    update_children_pos(child)

        update_children_pos(widget)

        self.children.append(widget)

    def pop(self) -> None:
        self.children = self.children[:-1]
