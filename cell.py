from math import sqrt

from config import Color, DEFAULT_COLOR
from geometry import Point, Line
from window import Window

class HexCell:

    SIDE_LEN: float = 15.0
    HEIGHT: float = SIDE_LEN * sqrt(3)
    CENTER_TO_VERTICES: list[Point] = [
        Point(SIDE_LEN, 0.0),
        Point(SIDE_LEN / 2.0, HEIGHT / 2.0),
        Point(- SIDE_LEN / 2.0, HEIGHT / 2.0),
        Point(- SIDE_LEN, 0.0),
        Point(- SIDE_LEN / 2.0, - HEIGHT / 2.0),
        Point(SIDE_LEN / 2.0, - HEIGHT / 2.0),
    ]
    
    def __init__(self, center: Point, win: Window) -> None:
        self.has_walls: list[bool] = [True] * 6
        
        self._center: Point = center
        self._win: Window = win
        
        return
    
    def draw(self, border_color: Color = DEFAULT_COLOR) -> None:

        vertices: list[Point] = [self._center + vector for vector in self.CENTER_TO_VERTICES]
        walls: list[Line] = [Line(vertices[i], vertices[(i + 1) % 6]) for i in range(6)]

        for i in range(6):
            if self.has_walls[i]:
                self._win.draw_line(walls[i], border_color)

        return