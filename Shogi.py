import turtle


def create(name):
    name = turtle.Turtle()
    return name


def move_turtle(name,x,y):
    name.setpos(x,y)


def death(piece,player):
    if player == 1:
        player_one.remove(piece)
        player_one_dead.append(piece)
        turtle_name = piece[0]
        turtle_name.turn(180)
    elif player == 2:
        player_two.remove(piece)
        player_two_dead.append(piece)
        turtle_name = piece[0]
        turtle_name.turn(180)


def move(x,y):
    fail = 0
    selected = turn_order[len(turn_order) -1]
    turtle_name = selected[0]
    if len(turn_order) % 2 != 0:
        if selected in player_two_dead:
            player_two_dead.remove(selected)
            player_one.append(selected)
        for piece in player_one:
            if piece[1] == x and piece[2] == y:
                fail = 1
        for piece in player_two:
            if piece[1] == x and piece[2] == y:
                death(piece,2)
    elif len(turn_order) % 2 == 0:
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
        move_turtle(turtle_name,x,y)
        wn.onclick(select)

    else:
        wn.onclick(move)


def select(x,y):
    selected = []
    if len(turn_order) + 1 % 2 != 0:
        for piece in player_one:
            if piece[1] - 50 <= x <= piece[1] + 50 and piece[2] - 50 <= y <= piece[2] + 50:
                selected = piece
        for piece in player_two_dead:
            if piece[1] - 50 <= x <= piece[1] + 50 and piece[2] - 50 <= y <= piece[2] + 50:
                selected = piece
    elif len(turn_order) + 1 % 2 == 0:
        for piece in player_two:
            if piece[1] - 50 <= x <= piece[1] + 50 and piece[2] - 50 <= y <= piece[2] + 50:
                selected = piece
        for piece in player_one_dead:
            if piece[1] - 50 <= x <= piece[1] + 50 and piece[2] - 50 <= y <= piece[2] + 50:
                selected = piece
    if selected != []:
        turn_order.append(selected)
        wn.onclick(move)
    else:
        wn.onclick(select)


player_one = [['turtle1',10,100]]
player_one_dead = []
player_two = [['turtle2',200,100]]
player_two_dead = []
turn_order = []

wn = turtle.Screen()

for player_one_set in player_one:
    turtle_names = player_one_set[0]
    turtle_name_set = create(turtle_names)
    turtle_name_set.setpos(player_one_set[1],player_one_set[2])

for player_two_set in player_two:
    turtle_names = player_two_set[0]
    turtle_name_set = create(turtle_names)
    turtle_name_set.setpos(player_two_set[1],player_two_set[2])

if len(turn_order) + 1 == 1:
    wn.onclick(select)


wn.mainloop()