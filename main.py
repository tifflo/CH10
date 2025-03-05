from window import Window, Point, Line, Cell
from maze import Maze
win = Window(800, 600)

# line1 = Line(Point(10,10),Point(200,200))
# win.draw_line(line1, 'black')

# line2 = Line(Point(100,90),Point(300,90))
# win.draw_line(line2, 'blue')

# line3 = Line(Point(400,420),Point(400,600))
# win.draw_line(line3, 'red')

# c1 = Cell(win)
# c1.set(Point(10,10),Point(200,200))
# c1.draw()

# c2 = Cell(win)
# c2.set(Point(210,210),Point(400,400))
# c2.draw()

# c1.draw_move(c2)

mz = Maze(5,5,10,10,30,30,win)
mz._create_cells()
mz._draw_cell(1,2)
win.wait_for_close()