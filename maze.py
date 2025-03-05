from window import Cell, Point
import time
from random import random, randrange

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed = None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        
        if seed is not None:
            random.seed(seed)

        self._cells = []
        self._create_cells()
        self._break_walls_r(0,0)
        self._reset_visited()
        solved = self._solve_r(0,0)
        print(solved)

    
    def _create_cells(self):
        for i in range(self._num_cols):
            cell_rows = []
            for j in range(self._num_rows):
                if (i == 0 and j==0):
                    cl = Cell(self._win)
                    cl.has_top_wall=False
                elif (i==self._num_cols-1 and j==self._num_rows-1):
                    cl = Cell(self._win)
                    cl.has_bottom_wall = False
                else:
                    cl = Cell(self._win)
                cell_rows.append(cl)
            self._cells.append(cell_rows)
        # for i in range(self._num_cols):
        #     for j in range(self._num_rows):
        #         self._draw_cell(i,j)
        

    def _draw_cell(self,i,j):
        if self._win is None:
            return
        x1 = self._x1 + int(i*self._cell_size_x)
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + int(j*self._cell_size_y)
        y2 = y1 + self._cell_size_y
        self._cells[i][j].set(Point(x1,y1),Point(x2,y2))
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.1)
    
    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # check left cell:
            if i>0:
                if not self._cells[i-1][j].visited:
                    to_visit.append((i-1,j,'left'))
            # check right cell:
            if i<self._num_cols-1:
                if not self._cells[i+1][j].visited:
                    to_visit.append((i+1,j,'right'))
            # check top cell:
            if j>0:
                if not self._cells[i][j-1].visited:
                    to_visit.append((i,j-1,'top'))
            # check bottom cell:
            if j<self._num_rows-1:
                if not self._cells[i][j+1].visited:
                    to_visit.append((i,j+1,'bottom'))
            # check if no direction is available:
            if not to_visit: 
                self._draw_cell(i,j)
                return
            # check if a direction is available:
            #  choose a random direction
            possible_directions = len(to_visit)
            p = to_visit[randrange(0,possible_directions)]
            # knock down walls
            if p[2] == 'top':
                self._cells[i][j].has_top_wall = False
                self._cells[p[0]][p[1]].has_bottom_wall = False
            elif p[2] == 'bottom':
                self._cells[i][j].has_bottom_wall = False
                self._cells[p[0]][p[1]].has_top_wall = False
            elif p[2] == 'left':
                self._cells[i][j].has_left_wall = False
                self._cells[p[0]][p[1]].has_right_wall = False
            elif p[2] == 'right':
                self._cells[i][j].has_right_wall = False
                self._cells[p[0]][p[1]].has_left_wall = False

            # move to picked cell:
            self._break_walls_r(p[0],p[1])
    
    def _reset_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def _solve_r(self, i,j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols -1 and j == self._num_rows -1:
            return True
        # check left cell:
        if i>0:
            if not self._cells[i-1][j].visited:
                if self._cells[i][j].has_left_wall == False:
                        self._cells[i][j].draw_move(self._cells[i-1][j])
                        finished = self._solve_r(i-1,j)
                        if finished:
                            return finished
                        self._cells[i][j].draw_move(self._cells[i-1][j],undo=True)
        # check right cell:
        if i<self._num_cols-1:
            if not self._cells[i+1][j].visited:
                if self._cells[i][j].has_right_wall == False:
                        self._cells[i][j].draw_move(self._cells[i+1][j])
                        finished = self._solve_r(i+1,j)
                        if finished:
                            return finished
                        self._cells[i][j].draw_move(self._cells[i+1][j],undo=True)
        # check top cell:
        if j>0:
            if not self._cells[i][j-1].visited:
                if self._cells[i][j].has_top_wall == False:
                        self._cells[i][j].draw_move(self._cells[i][j-1])
                        finished = self._solve_r(i,j-1)
                        if finished:
                            return finished
                        self._cells[i][j].draw_move(self._cells[i][j-1],undo=True)
        # check bottom cell:
        if j<self._num_rows-1:
            if not self._cells[i][j+1].visited:
                if self._cells[i][j].has_bottom_wall == False:
                        self._cells[i][j].draw_move(self._cells[i][j+1])
                        finished = self._solve_r(i,j+1)
                        if finished:
                            return finished
                        self._cells[i][j].draw_move(self._cells[i][j+1],undo=True)
        return False
