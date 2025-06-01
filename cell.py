from window import Point, Line

class Cell():
    def __init__(self, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        if self.__win:
            if self.has_left_wall:
                self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "black")
            if self.has_right_wall:
                self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "black")
            if self.has_top_wall:
                self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "black")
            if self.has_bottom_wall:
                self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "black")

    def draw_move(self, to_cell, undo=False):
        if undo:
            color = "gray"
        else:
            color = "red"
        linestart_x = self.__x1 + (self.__x2 - self.__x1) / 2
        linestart_y = self.__y1 + (self.__y2 - self.__y1) / 2
        lineend_x = to_cell.__x1 + (to_cell.__x2 - to_cell.__x1) / 2
        lineend_y = to_cell.__y1 + (to_cell.__y2 - to_cell.__y1) / 2
        if self.__win:
            self.__win.draw_line(Line(Point(linestart_x, linestart_y), Point(lineend_x, lineend_y)), color)
