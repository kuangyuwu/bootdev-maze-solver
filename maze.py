from math import sqrt
from time import sleep

from cell import HexCell
from geometry import Point, Vector
from window import Window

class Maze:

    def __init__(self, num_rows: int, num_columns: int, side_len: float, win: Window) -> None:
        self.__num_rows: int = num_rows
        self.__num_columns: int = num_columns
        self.__side_len: float = side_len
        self.__win: Window = win
        self._cells: list[list[HexCell]] = []
        self._create_cells()
        self._draw_cells()
        return

    def _create_cells(self) -> None:

        def create_cell(center: Point) -> HexCell:
            return HexCell(center, self.__side_len, self.__win)

        first_center: Point = Point(30.0, 30.0)
        move_along_row_even: Vector = Point(self.__side_len * 1.5, self.__side_len * 0.5 * sqrt(3))
        move_along_row_odd: Vector = Point(self.__side_len * 1.5, -self.__side_len * 0.5 * sqrt(3))
        move_along_column: Vector = Point(0, self.__side_len * sqrt(3))
        first_center_of_row: Point = first_center
        for i in range(self.__num_rows):
            center: Point = first_center_of_row
            self._cells.append([])
            for j in range(self.__num_columns):
                self._cells[-1].append(create_cell(center))
                center += move_along_row_even if j % 2 == 0 else move_along_row_odd
            first_center_of_row += move_along_column
        return
    
    def _draw_cells(self) -> None:
        for row in self._cells:
            for cell in row:
                cell.draw()
                self._animate()
        return
    
    def _animate(self) -> None:
        self.__win.redraw()
        sleep(0.05)