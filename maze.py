from cell import Cell
import time

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        """
        [
            [cell,cell,cell,cell]
            [cell,cell,cell,cell]
        ]"""

        for i in range(self._num_cols):
            new_col = []
            for j in range(self._num_rows):
                c = Cell(self._win)
                new_col.append(c)                
            
            self._cells.append(new_col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell:Cell = self._cells[i][j]
        x1 = self._x1 + (i * self._cell_size_x) # 10 + (0 * 20) = 10 | 10 + (1 * 20) = 30 | 10 + (2 * 20) = 50
        y1 = self._y1 + (j * self._cell_size_y) # 10 + (0 * 20) = 10 | 10 + (1 * 20) = 30 | 10 + (2 * 20) = 50
        x2 = self._x1 + self._cell_size_x + (i * self._cell_size_x) # 10 + 20 + (0 * 20) = 30 | 10 + 20 + (1 * 20) = 50 | 10 + 20 + (2 * 20) = 70
        y2 = self._y1 + self._cell_size_y + (j * self._cell_size_y)

        cell.draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

        
