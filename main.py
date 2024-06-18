from cell import HexCell
from geometry import Point, Line
from maze import Maze
from window import Window

def main():
    win = Window(800, 600)
    # maze = Maze(10, 10, 20, win) 
    maze = Maze(16, 26, 20, win)
    # maze = Maze(20, 34, 15, win) 
    # maze = Maze(30, 50, 10, win) 
    maze.solve()
    win.wait_for_close()

if __name__ == "__main__":
    main()