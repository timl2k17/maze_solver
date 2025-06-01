from time import sleep
from cell import Cell
import random

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
        seed = None
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
        if seed:
            random.seed(seed)

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
            sleep(0.02)  # Adjust the sleep time to control the animation speed

    def __break_entrance_and_exit(self):
        # Break the entrance and exit walls of the maze
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_rows - 1][self.__num_cols - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_rows - 1, self.__num_cols - 1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            directions = []
            if i > 0 and not self.__cells[i - 1][j].visited:
                directions.append("up")
            if i < self.__num_rows - 1 and not self.__cells[i + 1][j].visited:
                directions.append("down")
            if j > 0 and not self.__cells[i][j - 1].visited:
                directions.append("left")
            if j < self.__num_cols - 1 and not self.__cells[i][j + 1].visited:
                directions.append("right")
            if not directions:
                return
            direction = directions[int(random.random() * len(directions))]
            if direction == "up":
                self.__cells[i][j].has_top_wall = False
                self.__draw_cell(i, j)
                self.__cells[i - 1][j].has_bottom_wall = False
                self.__draw_cell(i - 1, j)
                self.__break_walls_r(i - 1, j)
            elif direction == "down":
                self.__cells[i][j].has_bottom_wall = False
                self.__draw_cell(i, j)
                self.__cells[i + 1][j].has_top_wall = False
                self.__draw_cell(i + 1, j)
                self.__break_walls_r(i + 1, j)
            elif direction == "left":
                self.__cells[i][j].has_left_wall = False
                self.__draw_cell(i, j)
                self.__cells[i][j - 1].has_right_wall = False
                self.__draw_cell(i, j - 1)
                self.__break_walls_r(i, j - 1)
            elif direction == "right":
                self.__cells[i][j].has_right_wall = False
                self.__draw_cell(i, j)
                self.__cells[i][j + 1].has_left_wall = False
                self.__draw_cell(i, j + 1)
                self.__break_walls_r(i, j + 1)

    def __reset_cells_visited(self):
        for row in self.__cells:
            for cell in row:
                cell.visited = False
    
    def solve(self):
        self.__solve_r(0, 0)

    def __solve_r(self, i, j):
        if i < 0 or i >= self.__num_rows or j < 0 or j >= self.__num_cols:
            return
        cell = self.__cells[i][j]
        if cell.visited:
            return
        cell.visited = True
        if i == self.__num_rows - 1 and j == self.__num_cols - 1:
            return True
        if not cell.has_top_wall and self.__solve_r(i - 1, j):
            cell.draw_move(self.__cells[i - 1][j])
            return True
        if not cell.has_bottom_wall and self.__solve_r(i + 1, j):
            cell.draw_move(self.__cells[i + 1][j])
            return True
        if not cell.has_left_wall and self.__solve_r(i, j - 1):
            cell.draw_move(self.__cells[i][j - 1])
            return True
        if not cell.has_right_wall and self.__solve_r(i, j + 1):
            cell.draw_move(self.__cells[i][j + 1])
            return True
        return False