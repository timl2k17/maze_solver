from tkinter import Tk, BOTH, Canvas
from maze import Maze
from window import Window


win = Window(800, 600)
'''
line1 = Line(Point(100, 100), Point(200, 200))
line2 = Line(Point(200, 100), Point(100, 200))
cell = Cell(win)
cell.has_left_wall = False
cell.draw(50, 50, 150, 150)
cell2 = Cell(win)
cell2.draw(200, 50, 300, 150)
cell3 = Cell(win)
cell3.draw(400, 400, 500, 500)
cell2.draw_move(cell3)
win.draw_line(line2, "red")
win.draw_line(line1, "black")
'''
maze = Maze(5, 5, 10, 20, 25, 25, win, 7)
maze._Maze__break_entrance_and_exit()
maze._Maze__break_walls_r(0, 0)
maze._Maze__reset_cells_visited()
maze.solve()
win.wait_for_close()