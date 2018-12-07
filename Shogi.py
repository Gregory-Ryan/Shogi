import turtle


def make_board():
    maker = turtle.Turtle()
    maker.ht()
    maker.speed(0)
    maker.penup()
    maker.setpos(225,-225)
    maker.pendown()
    for lines in range(0,2):
        maker.left(90)
        for repeat in range(0,5):
            maker.forward(450)
            maker.left(90)
            maker.forward(50)
            maker.left(90)
            maker.forward(450)
            if repeat != 4:
                maker.right(90)
                maker.forward(50)
                maker.right(90)


def death(piece,player):
    if player == 1:
        player_one.remove(piece)
        player_one_dead.append(piece)
        turtle_name = piece[3]
        turtle_name.turn(180)
    elif player == 2:
        player_two.remove(piece)
        player_two_dead.append(piece)
        turtle_name = piece[3]
        turtle_name.turn(180)


def move(x,y):
    global turn_counter
    fail = 0
    selected = turn_order[len(turn_order) -1]
    turtle_name = selected[3]
    if turn_counter % 2 != 0:
        if selected in player_two_dead:
            player_two_dead.remove(selected)
            player_one.append(selected)
        for piece in player_one:
            if piece[1] == x and piece[2] == y:
                fail = 1
        for piece in player_two:
            if piece[1] == x and piece[2] == y:
                death(piece,2)
    elif turn_counter % 2 == 0:
        if selected in player_one_dead:
            player_one_dead.remove(selected)
            player_two.append(selected)
        for piece in player_two:
            if piece[1] == x and piece[2] == y:
                fail = 1
        for piece in player_one:
            if piece[1] == x and piece[2] == y:
                death(piece,1)
    if fail != 1:
        del selected[0:1]
        selected.insert(1,x)
        del selected[1:2]
        selected.insert(2,y)
        turtle_name.setpos(x,y)
        turtle_name.color("black")
        turn_counter += 1
        wn.onclick(select)
    else:
        wn.onclick(move)


def select(x,y):
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
        turn_order.append(selected)
        wn.onclick(move)
    else:
        wn.onclick(select)


player_one = [['turtle1',10,100,turtle.Turtle()]]
player_one_dead = []
player_two = [['turtle2',200,100,turtle.Turtle()]]
player_two_dead = []
turn_order = []
turn_counter = 1

wn = turtle.Screen()
wn.title("Shogi")
make_board()

for player_one_set in player_one:
    turtle_names = player_one_set[3]
    turtle_names.penup()
    turtle_names.setpos(player_one_set[1],player_one_set[2])

for player_two_set in player_two:
    turtle_names = player_two_set[3]
    turtle_names.penup()
    turtle_names.setpos(player_two_set[1],player_two_set[2])


if turn_counter == 1:
    wn.onclick(select)


wn.mainloop()