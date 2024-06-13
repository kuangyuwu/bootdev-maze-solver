from tkinter import Canvas
from typing import Self

from config import Color

class Point:

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        return
    
    def __add__(self, other: Self) -> Self:
        return Point(self.x + other.x, self.y + other.y)

class Line:

    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end
        return

    def draw(self, canvas: Canvas, fill_color: Color) -> None:
        canvas.create_line(
            self.start.x, self.start.y,
            self.end.x, self.end.y,
            fill=fill_color,
            width=2,
        )
        return
