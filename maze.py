from cell import Cell
import time, random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._seed = seed
        if seed != None:
            random.seed(seed)

        self._break_walls_r(random.randrange(num_cols), random.randrange(num_rows))

        self._reset_cells_visited()

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
        if self._win is None:
            return   
        x1 = self._x1 + (i * self._cell_size_x) # 10 + (0 * 20) = 10 | 10 + (1 * 20) = 30 | 10 + (2 * 20) = 50
        y1 = self._y1 + (j * self._cell_size_y) # 10 + (0 * 20) = 10 | 10 + (1 * 20) = 30 | 10 + (2 * 20) = 50
        x2 = self._x1 + self._cell_size_x + (i * self._cell_size_x) # 10 + 20 + (0 * 20) = 30 | 10 + 20 + (1 * 20) = 50 | 10 + 20 + (2 * 20) = 70
        y2 = self._y1 + self._cell_size_y + (j * self._cell_size_y)

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.02)

    def _break_entrance_and_exit(self):
        if len(self._cells) < 1:
            return
        
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)        

        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False        
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i - 1][j]._visited:
                    to_visit.append((i - 1, j, "left"))
            if j > 0 and not self._cells[i][j - 1]._visited:
                    to_visit.append((i, j - 1, "top"))
            if i < self._num_cols - 1 and not self._cells[i + 1][j]._visited:
                    to_visit.append((i + 1, j, "right"))
            if j < self._num_rows - 1 and not self._cells[i][j + 1]._visited:
                    to_visit.append((i, j + 1, "bottom"))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
                        
            cell_to_visit = to_visit[random.randrange(len(to_visit))]

            if cell_to_visit[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if cell_to_visit[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if cell_to_visit[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if cell_to_visit[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(cell_to_visit[0], cell_to_visit[1])
                        
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell._visited = False

    def solve(self):
         return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()

        self._cells[i][j]._visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        if i > 0 and not self._cells[i - 1][j].has_right_wall and not self._cells[i - 1][j]._visited:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        if i < self._num_cols - 1 and not self._cells[i + 1][j].has_left_wall and not self._cells[i + 1][j]._visited:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        if j > 0 and not self._cells[i][j - 1].has_bottom_wall and not self._cells[i][j - 1]._visited:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        
        if j < self._num_rows - 1 and not self._cells[i][j + 1].has_top_wall and not self._cells[i][j + 1]._visited:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False
            


            

