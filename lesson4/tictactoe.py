from graphics import *

def draw_sells(wim):


    sell_1_1 = Rectangle(Point(0, 0), Point(200, 200))
    sell_1_2 = Rectangle(Point(200, 0), Point(400, 200))
    sell_1_3 = Rectangle(Point(400, 0), Point(600, 200))
    sell_2_1 = Rectangle(Point(0, 200), Point(200, 400))
    sell_2_2 = Rectangle(Point(200, 200), Point(400, 400))
    sell_2_3 = Rectangle(Point(400, 200), Point(600, 400))
    sell_3_1 = Rectangle(Point(0, 400), Point(200, 600))
    sell_3_2 = Rectangle(Point(200, 400), Point(400, 600))
    sell_3_3 = Rectangle(Point(400, 400), Point(600, 600))

    sell_1_1.draw(wim)
    sell_1_2.draw(wim)
    sell_1_3.draw(wim)
    sell_2_1.draw(wim)
    sell_2_2.draw(wim)
    sell_2_3.draw(wim)
    sell_3_1.draw(wim)
    sell_3_2.draw(wim)
    sell_3_3.draw(wim)

def get_cell(point):
    cell_x = int(point.getX()) // 200
    cell_y = int(point.getY()) // 200
    return [cell_x, cell_y]

def draw_x(cell_x, cell_y, wim):
    line1 = Line(Point(50 + cell_x * 200, 50 + cell_y * 200), Point(150 + cell_x * 200, 150 + cell_y * 200))
    line2 = Line(Point(150 + cell_x * 200, 50 + cell_y * 200), Point(50 + cell_x * 200, 150 + cell_y * 200))
    line1.draw(wim)
    line2.draw(wim)

def draw_o(cell_x, cell_y, wim):
    circ = Circle(Point(100 + cell_x * 200, 100 + cell_y * 200), 50)
    circ.draw(wim)

def is_win(cells):
    if [0, 0] in cells and [1, 1] in cells and [2, 2] in cells:
        return True
    if [0, 2] in cells and [1, 1] in cells and [2, 0] in cells:
        return True
    cells_x = [c[0] for c in cells]
    if cells_x.count(0) == 3 or cells_x.count(1) == 3 or cells_x.count(2) == 3:
        return True
    cells_y = [c[1] for c in cells]
    if cells_y.count(0) == 3 or cells_y.count(1) == 3 or cells_y.count(2) == 3:
        return True
    return False

def draw_message(text):
    mess_back = Rectangle(Point(150, 250), Point(450, 350))
    mess_back.setFill("white")
    message = Text(Point(300, 300), text)
    mess_back.draw(field)
    message.draw(field)

def input_message(ask):
    message = Entry(Point(300, 300), 15)
    message.setText(ask)
    message.draw(field)
    field.getMouse()
    answer = message.getText()
    message.undraw()
    return answer


field = GraphWin("Крестики-нолики", 600, 600)

name1 = input_message("What's your name?")
name2 = input_message("What's your name?")

draw_sells(field)

used_x_cells = []
used_o_cells = []
while True:
    cell = get_cell(field.getMouse())
    while cell in used_x_cells + used_o_cells:
        cell = get_cell(field.getMouse())
    used_x_cells.append(cell)
    draw_x(cell[0], cell[1], field)
    if is_win(used_x_cells):
        draw_message('Congratulation! '+name1+' win!')
        break
    if len(used_x_cells + used_o_cells) == 9:
        draw_message('Draw!')
        break
    cell = get_cell(field.getMouse())
    while cell in used_x_cells + used_o_cells:
        cell = get_cell(field.getMouse())
    used_o_cells.append(cell)
    draw_o(cell[0], cell[1], field)
    if is_win(used_o_cells):
        draw_message('Congratulation! '+name1+' win!')
        break


field.getMouse()
field.close()