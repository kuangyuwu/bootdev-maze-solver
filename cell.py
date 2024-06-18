from math import sqrt
from typing import Self

from config import Color, DEFAULT_COLOR, PATH_COLOR, UNDONE_PATH_COLOR, BACKGROUND_COLOR
from geometry import Point, Line, Vector
from window import Window

class HexCell:
    
    def __init__(self, center: Point, side_len: float, win: Window) -> None:
        self.visited: bool = False
        self.has_walls: list[bool] = [True] * 6
        self.center: Point = center
        self.__win: Window = win
        if not hasattr(HexCell, "side_len"):
            setattr(HexCell, "side_len", side_len)
            setattr(HexCell, "height", self.side_len * sqrt(3))
            setattr(HexCell, "center_to_vertices", [
                    Point(self.side_len, 0.0),
                    Point(self.side_len / 2.0, - self.height / 2.0),
                    Point(- self.side_len / 2.0, - self.height / 2.0),
                    Point(- self.side_len, 0.0),
                    Point(- self.side_len / 2.0, self.height / 2.0),
                    Point(self.side_len / 2.0, self.height / 2.0),
                ]
            )
        if side_len != getattr(HexCell, "side_len"):
            raise ValueError("Invalid HexCell: incorrect side length")
        return
    
    # @property
    # def height(self) -> float:
    #     if not hasattr(self, "_height"):
    #         setattr(self, "_height", self.side_len * sqrt(3))
    #     return self._height
    
    # @property
    # def center_to_vertices(self) -> list[Vector]:
    #     if not hasattr(self, "_center_to_vertices"):
    #         setattr(
    #             self,
    #             "_center_to_vertices",
    #             [
    #                 Point(self.side_len, 0.0),
    #                 Point(self.side_len / 2.0, - self.height / 2.0),
    #                 Point(- self.side_len / 2.0, - self.height / 2.0),
    #                 Point(- self.side_len, 0.0),
    #                 Point(- self.side_len / 2.0, self.height / 2.0),
    #                 Point(self.side_len / 2.0, self.height / 2.0),
    #             ]
    #         )
    #     return self._center_to_vertices

    @property
    def vertices(self) -> list[Point]:
        if not hasattr(self, "_vertices"):
            setattr(self, "_vertices", [self.center + vector for vector in self.center_to_vertices])
        return self._vertices
    
    @property
    def walls(self) -> list[Line]:
        if not hasattr(self, "_walls"):
            setattr(self, "_walls", [Line(self.vertices[i], self.vertices[(i + 1) % 6]) for i in range(6)])
        return self._walls
    
    def draw(self, border_color: Color = DEFAULT_COLOR) -> None:
    #     vertices: list[Point] = [self.center + vector for vector in self.center_to_vertices]
    #     walls: list[Line] = [Line(vertices[i], vertices[(i + 1) % 6]) for i in range(6)]
        for i in range(6):
            if self.has_walls[i]:
                self.__win.draw_line(self.walls[i], border_color)
            else:
                self.__win.draw_line(self.walls[i], BACKGROUND_COLOR)
        return
    
    def draw_move(self, to_cell: Self, undo: bool = False) -> None:
        path: Line = Line(self.center, to_cell.center)
        fill_color: Color = UNDONE_PATH_COLOR if undo else PATH_COLOR
        self.__win.draw_line(path, fill_color)
        return