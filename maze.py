import random
from math import sqrt
from time import sleep

from cell import HexCell
from geometry import Point, Vector
from window import Window

class Maze:

    def __init__(
            self,
            num_rows: int,
            num_columns: int,
            side_len: float,
            win: Window | None = None,
            seed: int | None = None
    ) -> None:
        self.__num_rows: int = num_rows
        self.__num_columns: int = num_columns
        self.__side_len: float = side_len
        self.__win: Window = win
        self.cells: list[list[HexCell]] = []
        random.seed(seed)
        self.__create_cells()
        if self.__win is not None:
            self.__draw_cells()
            self.__break_entrance_and_exit()
            self.__break_walls_r(0, 0)
            self.__reset_cells_visited()
        return

    def __create_cells(self) -> None:

        def create_cell(center: Point) -> HexCell:
            return HexCell(center, self.__side_len, self.__win)

        first_center: Point = Point(30.0, 30.0)
        move_along_row_even: Vector = Point(self.__side_len * 1.5, self.__side_len * 0.5 * sqrt(3))
        move_along_row_odd: Vector = Point(self.__side_len * 1.5, -self.__side_len * 0.5 * sqrt(3))
        move_along_column: Vector = Point(0, self.__side_len * sqrt(3))
        first_center_of_row: Point = first_center
        for _ in range(self.__num_rows):
            center: Point = first_center_of_row
            self.cells.append([])
            for j in range(self.__num_columns):
                self.cells[-1].append(create_cell(center))
                center += move_along_row_even if j % 2 == 0 else move_along_row_odd
            first_center_of_row += move_along_column
        return
    
    def __draw_cells(self) -> None:
        for row in self.cells:
            for cell in row:
                cell.draw()
                self.__animate(0)
        return
    
    def __animate(self, time: float = 0.05) -> None:
        self.__win.redraw()
        sleep(time)
        return
    
    def __break_entrance_and_exit(self) -> None:
        self.cells[0][0].has_walls[2] = False
        self.cells[0][0].draw()
        self.__animate(0)

        self.cells[-1][-1].has_walls[5] = False
        self.cells[-1][-1].draw()
        self.__animate(0)
        return

    def __break_walls_r(self, i: int, j: int) -> None:
        self.cells[i][j].visited = True
        directions = self.__get_possible_directions(i, j)
        if len(directions) > 0:
            di, dj, k = directions[random.randrange(len(directions))]
            ip: int = i + di
            jp: int = j + dj
            self.cells[i][j].has_walls[k] = False
            self.cells[i][j].draw()
            self.__animate(0)
            self.cells[ip][jp].has_walls[(k + 3) % 6] = False
            self.__break_walls_r(ip, jp)
            self.__break_walls_r(i, j)
        return

    def __get_possible_directions(self, i: int, j: int, solving: bool = False) -> list[tuple[int, int]]:
        if j % 2 == 0:
            all_directions: list[tuple[int, int]] = [
                (-1, 1, 0), (-1, 0, 1), (-1, -1, 2), (0, -1, 3), (1, 0, 4), (0, 1, 5)
            ]
            return [
                tup for tup in all_directions
                if i + tup[0] >= 0 and i + tup[0] < self.__num_rows
                and j + tup[1] >= 0 and j + tup[1] < self.__num_columns
                and not self.cells[i + tup[0]][j + tup[1]].visited
                and (not solving or not self.cells[i][j].has_walls[tup[2]])
            ]
        else:
            all_directions: list[tuple[int, int]] = [
                (0, 1, 0), (-1, 0, 1), (0, -1, 2), (1, -1, 3), (1, 0, 4), (1, 1, 5)
            ]
            return [
                tup for tup in all_directions
                if i + tup[0] >= 0 and i + tup[0] < self.__num_rows
                and j + tup[1] >= 0 and j + tup[1] < self.__num_columns
                and not self.cells[i + tup[0]][j + tup[1]].visited
                and (not solving or not self.cells[i][j].has_walls[tup[2]])
            ]
    
    def __reset_cells_visited(self) -> None:
        for row in self.cells:
            for cell in row:
                cell.visited = False
        return
    
    def solve(self) -> bool:
        return self.__solve_r(0, 0)

    def __solve_r(self, i: int, j: int) -> bool:
        if i == self.__num_rows - 1 and j == self.__num_columns - 1:
            return True
        self.cells[i][j].visited = True
        directions = self.__get_possible_directions(i, j, solving=True)
        done: bool = False
        if len(directions) > 0:
            di, dj, k = directions[random.randrange(len(directions))]
            ip: int = i + di
            jp: int = j + dj
            self.cells[i][j].draw_move(self.cells[ip][jp])
            self.__animate()
            done = self.__solve_r(ip, jp)
            if done:
                return True
            self.cells[i][j].draw_move(self.cells[ip][jp], undo=True)
            self.__animate()
            done = self.__solve_r(i, j)
        return done