from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("Window closed...")
    
    def close(self):
        self.running = False

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1:Point, point2:Point):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas:Canvas, fill_color="black"):
        x1, y1 = self.point1.x, self.point1.y        
        x2, y2 = self.point2.x, self.point2.y        
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)
