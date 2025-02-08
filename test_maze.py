import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

        num_cols = 22
        num_rows = 15
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_break_walls_entrance_exit(self):
        num_cols = 22
        num_rows = 15
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    def test_maze_visited_false(self):
        num_cols = 10
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._reset_cells_visited()
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell._visited,
                    False)



if __name__ == "__main__":
    unittest.main()