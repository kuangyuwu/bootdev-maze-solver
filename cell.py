from math import sqrt
from tkinter import Canvas

from config import Color
from geometry import Point, Line

class HexCell:

    SIDE_LEN: float = 15.0
    HEIGHT: float = SIDE_LEN * sqrt(3)
    CENTER_TO_RIGHT_VERTEX: Point = Point(SIDE_LEN, 0.0)
    CENTER_TO_TOP_RIGHT_VERTEX: Point = Point(SIDE_LEN / 2.0, HEIGHT / 2.0)
    CENTER_TO_TOP_LEFT_VERTEX: Point = Point(- SIDE_LEN / 2.0, HEIGHT / 2.0)
    CENTER_TO_LEFT_VERTEX: Point = Point(- SIDE_LEN, 0.0)
    CENTER_TO_BOTTOM_LEFT_VERTEX: Point = Point(- SIDE_LEN / 2.0, - HEIGHT / 2.0)
    CENTER_TO_BOTTOM_RIGHT_VERTEX: Point = Point(SIDE_LEN / 2.0, - HEIGHT / 2.0)
    
    def __init__(self, center: Point) -> None:
        self._center: Point = center
        self.has_top_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_top_left_wall: bool = True
        self.has_bottom_left_wall: bool = True
        self.has_bottom_wall: bool = True
        self.has_bottom_right_wall: bool = True
        return
    
    def draw(self, canvas: Canvas, border_color: Color) -> None:
        right_vertex: Point = self._center + self.CENTER_TO_RIGHT_VERTEX
        top_right_vertex: Point = self._center + self.CENTER_TO_TOP_RIGHT_VERTEX
        top_left_vertex: Point = self._center + self.CENTER_TO_TOP_LEFT_VERTEX
        left_vertex: Point = self._center + self.CENTER_TO_LEFT_VERTEX
        bottom_left_vertex: Point = self._center + self.CENTER_TO_BOTTOM_LEFT_VERTEX
        bottom_right_vertex: Point = self._center + self.CENTER_TO_BOTTOM_RIGHT_VERTEX
        
        top_right_wall: Line = Line(right_vertex, top_right_vertex)
        top_wall: Line = Line(top_right_vertex, top_left_vertex)
        top_left_wall: Line = Line(top_left_vertex, left_vertex)
        bottom_left_wall: Line = Line(left_vertex, bottom_left_vertex)
        bottom_wall: Line = Line(bottom_left_vertex, bottom_right_vertex)
        bottom_right_wall: Line = Line(bottom_right_vertex, right_vertex)

        if self.has_top_right_wall:
            top_right_wall.draw(canvas, border_color)
        if self.has_top_wall:
            top_wall.draw(canvas, border_color)
        if self.has_top_left_wall:
            top_left_wall.draw(canvas, border_color)
        if self.has_bottom_left_wall:
            bottom_left_wall.draw(canvas, border_color)
        if self.has_bottom_wall:
            bottom_wall.draw(canvas, border_color)
        if self.has_bottom_right_wall:
            bottom_right_wall.draw(canvas, border_color)

        pass