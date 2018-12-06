import turtle


def move(x,y):
    fail = 0
    selected = turn_order[len(turn_order)]
    turtle_name = selected[1]
    for piece in player_one:
        if piece[2] == x and piece[3] == y:
            fail = 1
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
        if selected != []:
            turn_order.appened(selected)
            wn.onclick(move)
        else:
            wn.onclick(select)
    elif turn_counter % 2 == 0:
        for piece in player_two:
            if piece[2] == x and piece[3] == y:
                selected = piece
        for piece in player_one_dead:
            if piece[2] == x and piece[3] == y:
                selected = piece
        if selected != []:
            turn_order.appened(selected)
            wn.onclick(move)
        else:
            wn.onclick(select)


player_one = []
player_one_dead = []
player_two = []
player_two_dead = []
turn_counter = 1
turn_order = []

wn = turtle.Screen()

if turn_counter == 1:
    wn.onclick(select)


wn.mainloop()