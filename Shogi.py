import turtle


def death(piece,player):
    if player == 1:
        player_one.remove(piece)
        player_one_dead.append(piece)
        turtle_name = piece[1]
        turtle_name.turn(180)
    elif player == 2:
        player_two.remove(piece)
        player_two_dead.append(piece)
        turtle_name = piece[1]
        turtle_name.turn(180)


def move(x,y):
    fail = 0
    selected = turn_order[len(turn_order)]
    turtle_name = selected[1]
    if turn_counter % 2 != 0:
        if selected in player_two_dead:
            player_two_dead.remove(selected)
            player_one.append(selected)
        for piece in player_one:
            if piece[2] == x and piece[3] == y:
                fail = 1
        for piece in player_two:
            if piece[2] == x and piece[3] == y:
                death(piece,2)
    elif turn_counter % 2 == 0:
        if selected in player_one_dead:
            player_one_dead.remove(selected)
            player_two.append(selected)
        for piece in player_two:
            if piece[2] == x and piece[3] == y:
                fail = 1
        for piece in player_one:
            if piece[2] == x and piece[3] == y:
                death(piece,1)
    if fail != 1:
        turtle_name.setpos(x,y)
        turn_counter += 1
        wn.onclick(select)

    else:
        wn.onclick(move)


def select(x,y):
    selected = []
    if turn_counter % 2 != 0:
        for piece in player_one:
            if piece[2] == x and piece[3] == y:
                selected = piece
        for piece in player_two_dead:
            if piece[2] == x and piece[3] == y:
                selected = piece
    elif turn_counter % 2 == 0:
        for piece in player_two:
            if piece[2] == x and piece[3] == y:
                selected = piece
        for piece in player_one_dead:
            if piece[2] == x and piece[3] == y:
                selected = piece
    if selected != []:
        turn_order.append(selected)
        wn.onclick(move)
    else:
        wn.onclick(select)


player_one = [['turtle1',10,100]]
player_one_dead = []
player_two = [['turtle2',10,100]]
player_two_dead = []
turn_counter = 1
turn_order = []

wn = turtle.Screen()

for player_one_set in player_one:
    turtle_name_set = player_one_set[1]
    turtle_name_set = turtle.Turtle()
    turtle_name_set.setpos(player_one_set[2],player_one_set[3])

for player_two_set in player_two:
    turtle_name_set = player_two_set[1]
    turtle_name_set = turtle.Turtle()
    turtle_name_set.setpos(player_two_set[2],player_two_set[3])

if turn_counter == 1:
    wn.onclick(select)


wn.mainloop()