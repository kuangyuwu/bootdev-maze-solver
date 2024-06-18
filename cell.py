from math import sqrt
from typing import Self

from config import Color, DEFAULT_COLOR, PATH_COLOR, UNDONE_PATH_COLOR
from geometry import Point, Line, Vector
from window import Window

class HexCell:
    
    def __init__(self, center: Point, side_len: float, win: Window) -> None:
        self.has_walls: list[bool] = [True] * 6
        self._center: Point = center
        self._side_len: float = side_len
        self.__win: Window = win
        return
    
    @property
    def height(self) -> float:
        if not hasattr(self, "_height"):
            setattr(self, "_height", self._side_len * sqrt(3))
        return self._height
    
    @property
    def center_to_vertices(self) -> list[Vector]:
        if not hasattr(self, "_center_to_vertices"):
            setattr(
                self,
                "_center_to_vertices",
                [
                    Point(self._side_len, 0.0),
                    Point(self._side_len / 2.0, self.height / 2.0),
                    Point(- self._side_len / 2.0, self.height / 2.0),
                    Point(- self._side_len, 0.0),
                    Point(- self._side_len / 2.0, - self.height / 2.0),
                    Point(self._side_len / 2.0, - self.height / 2.0),
                ]
            )
        return self._center_to_vertices
    
    def draw(self, border_color: Color = DEFAULT_COLOR) -> None:
        vertices: list[Point] = [self._center + vector for vector in self.center_to_vertices]
        walls: list[Line] = [Line(vertices[i], vertices[(i + 1) % 6]) for i in range(6)]
        for i in range(6):
            if self.has_walls[i]:
                self.__win.draw_line(walls[i], border_color)
        return
    
    def draw_move(self, to_cell: Self, undo: bool = False) -> None:
        path: Line = Line(self._center, to_cell._center)
        fill_color: Color = UNDONE_PATH_COLOR if undo else PATH_COLOR
        self.__win.draw_line(path, fill_color)
        return