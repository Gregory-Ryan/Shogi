import turtle


def move(x,y):
    selected = turn_order[len(turn_order)]


def select(x,y):
    selected = []
    if turn_counter % 2 != 0:
        for piece in player_one:
            if piece[2] == x and piece[3] == y:
                selected = piece
    elif turn_counter % 2 == 0:
        for piece in player_two:
            if piece[2] == x and piece[3] == y:
                selected = piece
    turn_order.appened(selected)
    wn.onclick(move)


player_one = []
player_two = []
turn_counter = 1
turn_order = []

wn = turtle.Screen()
