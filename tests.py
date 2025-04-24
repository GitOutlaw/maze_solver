import unittest
from maze import Maze
from graphics import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        win = Window(800, 600)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_default_walls(self):
        num_cols = 5
        num_rows = 5
        win = Window(800, 600)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        cell = m1._cells[0][0]
        self.assertTrue(cell.has_left_wall)
        self.assertTrue(cell.has_right_wall)
        self.assertTrue(cell.has_top_wall)
        self.assertTrue(cell.has_bottom_wall)

    def test_break_entrance_and_exit(self):
        num_cols = 5
        num_rows = 5
        win = Window(800, 600)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)

        # Check entrance
        self.assertFalse(m1._cells[0][0].has_top_wall)

        # Check exit
        self.assertFalse(m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall)

        # Optionally check other walls of these cells
        self.assertTrue(m1._cells[0][0].has_left_wall)
        self.assertTrue(m1._cells[0][0].has_right_wall)
        self.assertTrue(m1._cells[0][0].has_bottom_wall)

        self.assertTrue(m1._cells[num_cols - 1][num_rows - 1].has_left_wall)
        self.assertTrue(m1._cells[num_cols - 1][num_rows - 1].has_right_wall)
        self.assertTrue(m1._cells[num_cols - 1][num_rows - 1].has_top_wall)


if __name__ == "__main__":
    unittest.main()