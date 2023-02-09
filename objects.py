import numpy as np
from PIL import Image


class Canvas:
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

        self.array = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.array[:] = self.color

    def make_image(self, savepath):
        img = Image.fromarray(self.array, 'RGB')
        img.save(savepath)


class Rectangle:
    def __init__(self, width, height, x, y, color):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.color = color

    def add_to_canvas(self, canvas):
        canvas.array[self.y:self.y + self.height, self.x:self.x + self.width] = self.color


class Square:
    def __init__(self, side_length, x, y, color):
        self.side_length = side_length
        self.x = x
        self.y = y
        self.color = color

    def add_to_canvas(self, canvas):
        canvas.array[self.y:self.y + self.side_length, self.x:self.x + self.side_length] = self.color


canvas = Canvas(height=20, width=30, color=(255, 255, 255))
r1 = Rectangle(x=6, y=1, height=7, width=10, color=(100, 200, 125))
r1.add_to_canvas(canvas)
s1 = Square(x=3, y=1, side_length=3, color=(0, 100, 222))
s1.add_to_canvas(canvas)
canvas.make_image('canvas.png')