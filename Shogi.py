import turtle


def make_yards():
    make = turtle.Turtle()
    make.ht()
    make.speed(0)
    make.penup()
    make.setpos(-400, -175)
    make.pendown()
    make.forward(150)
    make.back(150)
    make.left(180)
    for q in range(0, 2):
        if q == 1:
            make.penup()
            make.setpos(400, 175)
            make.pendown()
            make.left(90)
            make.forward(150)
            make.back(150)
            make.right(180)
        for i in range(0, 7):
            if i % 2 == 0:
                make.right(90)
                make.forward(50)
                make.right(90)
                make.forward(150)
            else:
                make.left(90)
                make.forward(50)
                make.left(90)
                make.forward(150)

        make.right(90)
        make.forward(350)
        make.right(90)
        make.forward(50)
        make.right(90)
        make.forward(350)
        make.left(90)
        make.forward(50)
        make.left(90)
        make.forward(350)
        make.right(90)
        make.forward(50)
        make.right(90)
        make.forward(350)


def round_to_mid(x, y):
    for location in middle:
        if location[0] - 25 <= x <= location[0] + 25 and location[1] - 25 <= y <= location[1] + 25:
            return [location[0], location[1]]
    return ["na","na"]


def mid():
    midd = []
    for midd_y in range(0, 9):
        for midd_x in range(0, 9):
            midd.append([-200 + midd_x * 50, 200 - midd_y * 50])
    return midd


# def promote(piece):
#     prompt = wn.textinput("Promotion","Promote?(y or n)")
#     if piece in promotion and prompt == "y":
#         name = piece[0]
#         new_name = "promoted" + name
#         del piece[0]
#         piece.insert(0, new_name)


def make_board():
    maker = turtle.Turtle()
    maker.ht()
    maker.speed(0)
    maker.penup()
    maker.setpos(225, -225)
    maker.pendown()
    for lines in range(0, 2):
        maker.left(90)
        for repeat in range(0, 5):
            maker.forward(450)
            maker.left(90)
            maker.forward(50)
            maker.left(90)
            maker.forward(450)
            if repeat != 4:
                maker.right(90)
                maker.forward(50)
                maker.right(90)


def death(piece, player):
    if player == 1:
        player_one.remove(piece)
        player_one_dead.append(piece)
        turtle_name = piece[3]
        turtle_name.clear()
        turtle_name.setpos(375 - 50 * (len(player_one_dead) - 1), 150)
        turtle_name.right(180)
        turtle_name.write(piece[0] + "\n", align="center",font=("Arial",7,"bold"))
        del piece[1]
        piece.insert(1, 375 - 50 * (len(player_one_dead) - 1))
        del piece[2]
        piece.insert(2, 150)
    elif player == 2:
        player_two.remove(piece)
        player_two_dead.append(piece)
        turtle_name = piece[3]
        turtle_name.clear()
        turtle_name.setpos(-375 + 50 * (len(player_two_dead) - 1), 150)
        turtle_name.right(180)
        turtle_name.write(piece[0] + "\n", align="center",font=("Arial",7,"bold"))
        del piece[1]
        piece.insert(1, -375 + 50 * (len(player_two_dead) - 1))
        del piece[2]
        piece.insert(2, 150)


def move(u, v):
    global turn_counter
    cord = round_to_mid(u, v)
    x = cord[0]
    y = cord[1]
    fail = 0
    returned = 0
    selected = order_selected[len(order_selected) - 1]
    turtle_name = selected[3]
    if x == "na" and y == "na":
        fail = 1
    if turn_counter % 2 != 0:
        if selected in player_two_dead:
            player_two_dead.remove(selected)
            player_one.append(selected)
            returned = 1
        for piece in player_one:
            if piece[1] == x and piece[2] == y:
                fail = 1
        for piece in player_two:
            if piece[1] == x and piece[2] == y:
                if returned == 1:
                    fail = 1
                else:
                    death(piece, 2)
    elif turn_counter % 2 == 0:
        if selected in player_one_dead:
            player_one_dead.remove(selected)
            player_two.append(selected)
            returned = 1
        for piece in player_two:
            if piece[1] == x and piece[2] == y:
                fail = 1
        for piece in player_one:
            if piece[1] == x and piece[2] == y:
                if returned == 1:
                    fail = 1
                else:
                    death(piece, 1)
    if fail != 1:
        del selected[1]
        selected.insert(1, x)
        del selected[2]
        selected.insert(2, y)
        turtle_name.clear()
        turtle_name.setpos(x, y)
        turtle_name.color("black")
        turtle_name.write(selected[0] + "\n", align="center",font=("Arial",7,"bold"))
        turn_counter += 1
        wn.onclick(select)
    else:
        turtle_name.color("black")
        wn.onclick(select)


def select(x, y):
    global turn_counter
    selected = []
    fail = 1
    if turn_counter % 2 != 0:
        for piece in player_one:
            if piece[1] - 25 <= x <= piece[1] + 25 and piece[2] - 25 <= y <= piece[2] + 25:
                selected = piece
                fail = 0
        for piece in player_two_dead:
            if piece[1] - 25 <= x <= piece[1] + 25 and piece[2] - 25 <= y <= piece[2] + 25:
                selected = piece
                fail = 0
    elif turn_counter % 2 == 0:
        for piece in player_two:
            if piece[1] - 25 <= x <= piece[1] + 25 and piece[2] - 25 <= y <= piece[2] + 25:
                selected = piece
                fail = 0
        for piece in player_one_dead:
            if piece[1] - 25 <= x <= piece[1] + 25 and piece[2] - 25 <= y <= piece[2] + 25:
                selected = piece
                fail = 0
    if fail != 1:
        turtle_ref = selected[3]
        turtle_ref.color("blue")
        order_selected.append(selected)
        wn.onclick(move)
    else:
        wn.onclick(select)


player_one = [['turtle1', 50, 100, turtle.Turtle()], ['turtle3', 100, 100, turtle.Turtle()]]
player_one_dead = []
player_two = [['turtle2', 200, 100, turtle.Turtle()], ['turtle4', 200, 150, turtle.Turtle()]]
player_two_dead = []
# promotion = []
order_selected = []
middle = mid()
turn_counter = 1

wn = turtle.Screen()
wn.title("Shogi")
make_board()
make_yards()
wn.register_shape("tri", ((10,-3), (10,-20),  (-10,-20), (-10,-3), (-5,10), (5,10)))

for player_one_set in player_one:
    turtle_names = player_one_set[3]
    turtle_names.shape("tri")
    turtle_names.penup()
    turtle_names.setpos(player_one_set[1], player_one_set[2])
    turtle_names.write(player_one_set[0] + "\n", align="center",font=("Arial",7,"bold"))

for player_two_set in player_two:
    turtle_names = player_two_set[3]
    turtle_names.shape("tri")
    turtle_names.penup()
    turtle_names.setpos(player_two_set[1], player_two_set[2])
    turtle_names.right(180)
    turtle_names.write(player_two_set[0] + "\n", align="center",font=("Arial",7,"bold"))

if turn_counter == 1:
    wn.onclick(select)

wn.mainloop()
