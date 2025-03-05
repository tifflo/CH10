from tkinter import Tk, BOTH, Canvas
from envs import TITLE, LINE_WIDTH

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title(TITLE)
        self.__canvas = Canvas(master=self.__root, height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")
    

    def draw_line(self, line, fill_color='black'):
        line.draw(self.__canvas, fill_color)


    def close(self):
        self.__running = False


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color='black'):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width = LINE_WIDTH)


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win
        self.visited = False
    
    def set(self,p1,p2):
        self._x1 = p1.x
        self._x2 = p2.x
        self._y1 = p1.y
        self._y2 = p2.y

    def draw(self):
        if self._win is None:
            return
        
        if self.has_left_wall  == True:
            wall = Line(Point(self._x1, self._y1),Point(self._x1, self._y2))
            self._win.draw_line(wall)
        else:
            wall = Line(Point(self._x1, self._y1),Point(self._x1, self._y2))
            self._win.draw_line(wall, 'white')

        if self.has_right_wall  == True:
            wall = Line(Point(self._x2, self._y1),Point(self._x2, self._y2))
            self._win.draw_line(wall)
        else:
            wall = Line(Point(self._x2, self._y1),Point(self._x2, self._y2))
            self._win.draw_line(wall, 'white')
        
        if self.has_top_wall  == True:
            wall = Line(Point(self._x1, self._y1),Point(self._x2, self._y1))
            self._win.draw_line(wall)
        else:
            wall = Line(Point(self._x1, self._y1),Point(self._x2, self._y1))
            self._win.draw_line(wall, 'white')

        if self.has_bottom_wall  == True:
            wall = Line(Point(self._x1, self._y2),Point(self._x2, self._y2))
            self._win.draw_line(wall)
        else:
            wall = Line(Point(self._x1, self._y2),Point(self._x2, self._y2))
            self._win.draw_line(wall, 'white')
    
    def cell_center(self):
        xcenter = self._x1 + (self._x2-self._x1)//2
        ycenter = self._y1 + (self._y2-self._y1)//2
        return Point(xcenter,ycenter)
    
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        fill_color  = 'red'
        if undo:
            fill_color = 'grey'
        line = Line(self.cell_center(),to_cell.cell_center())
        self._win.draw_line(line,fill_color)

