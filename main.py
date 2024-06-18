from cell import HexCell
from geometry import Point, Line
from maze import Maze
from window import Window

def main():
    win = Window(800, 600)
    maze = Maze(30, 50, 10, win) 
    maze.solve()
    win.wait_for_close()

if __name__ == "__main__":
    main()