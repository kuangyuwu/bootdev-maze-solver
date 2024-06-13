from cell import HexCell
from geometry import Point, Line
from window import Window

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(155.8, 290.3), Point(312.6, 183.7)), "black")
    cell = HexCell(Point(400, 300), win)
    cell.draw()
    cell2 = HexCell(Point(100, 500), win)
    cell2.draw()
    cell.draw_move(cell2)
    cell3 = HexCell(Point(500, 100), win)
    cell3.draw()
    cell.draw_move(cell3, True)
    win.wait_for_close()

if __name__ == "__main__":
    main()