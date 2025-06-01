from time import sleep
from cell import Cell

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for row in range(self.__num_rows):
            cell_row = []
            for col in range(self.__num_cols):
                cell = Cell(self.__win)
                cell_row.append(cell)
            self.__cells.append(cell_row)
        for row in range(self.__num_rows):
            for col in range(self.__num_cols):
                self.__draw_cell(row, col)
    
    def __draw_cell(self, i, j):
        x1 = self.__x1 + j * self.__cell_size_x
        y1 = self.__y1 + i * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.__win:
            self.__win.redraw()
            sleep(0.1)  # Adjust the sleep time to control the animation speed