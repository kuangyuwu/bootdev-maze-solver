import unittest

from maze import Maze

class Tests(unittest.TestCase):
    
    def test_create_maze(self):
        num_rows = 12
        num_columns = 15
        maze = Maze(num_rows, num_columns, 1)
        self.assertEqual(len(maze._cells), num_rows)
        for row in maze._cells:
            self.assertEqual(len(row), num_columns)