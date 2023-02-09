from objects import Square, Rectangle, Canvas


def prompt_canvas():
    colors = {
        'white':(255, 255, 255),
        'black':(0, 0, 0)
    }
    canvas_width = int(input('How wide would you like the canvas?: '))
    canvas_height = int(input('How tall would you like the canvas?: '))
    canvas_color = input('Would you like a white or black canvas?: ').lower()
    canvas = Canvas(canvas_height, canvas_width, colors[canvas_color])
    return canvas


def prompt_square():
    side_length = int(input('How long would you like the sides to be?: '))
    color = tuple(int(x) for x in input('What RGB would you like the square to be?: ').strip().split(","))
    x = int(input('What x coordinate would you like the square to start at?: '))
    y = int(input('How far from the top would you like the top of the square?: '))
    return Square(side_length, x, y, color)


def prompt_rect():
    height = int(input('How tall would you like the rectangle to be?: '))
    width = int(input('How wide would you like the rectangle to be?: '))
    color = tuple(int(x) for x in input('What RGB would you like the rectangle to be?: ').strip().split(","))
    x = int(input('What x coordinate would you like the rectangle to start at?: '))
    y = int(input('How far from the top would you like the top of the rectangle?: '))
    return Rectangle(width, height, x, y, color)


canvas = prompt_canvas()

menu = True
while menu:
    shape = input('What shape would you like to draw? ')
    if shape.lower() == 'square':
        square = prompt_square()
        square.add_to_canvas(canvas)

    elif shape.lower() == 'rectangle':
        rectangle = prompt_rect()
        rectangle.add_to_canvas(canvas)

    elif shape.lower() == 'quit':
        break
    else:
        print('try again ser')

canvas.make_image('canvas.png')