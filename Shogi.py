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


def legal_move(piece):
    global turn_counter
    global temp_move_list
    restrict = 0
    player = 0
    if turn_counter % 2 != 0:
        player = 1
        if piece in player_one:
            restrict = 1
    elif turn_counter % 2 == 0:
        player = 2
        if piece in player_two:
            restrict = 1
    if restrict == 1:
        piece_name = piece[0]
        for rule in movement_rules:
            if piece_name == rule[0]:
                move_list = rule[1:len(rule)]
                for location in move_list:
                    if player == 1:
                        for part in player_one:
                            if part[1] != location[0] + piece[1] and part[2] != location[1] + piece[2]:
                                high_light_space(location[0] + piece[1],location[1] + piece[2],"blue")
                                temp_move_list.append([location[0] + piece[1],location[1] + piece[2]])
                        for part in player_two:
                            if [part[1],part[2]] == [location[0] + piece[1],location[1] + piece[2]]:
                                high_light_space(location[0] + piece[1],location[1] + piece[2],"red")
                                temp_move_list.append([location[0] + piece[1],location[1] + piece[2]])
                    elif player == 2:
                        for part in player_two:
                            if part[1] != location[0] + piece[1] and part[2] != location[1] + piece[2]:
                                high_light_space(location[0] + piece[1],location[1] + piece[2],"blue")
                                temp_move_list.append([location[0] + piece[1],location[1] + piece[2]])
                        for part in player_one:
                            if [part[1],part[2]] == [location[0] + piece[1],location[1] + piece[2]]:
                                high_light_space(location[0] + piece[1],location[1] + piece[2],"red")
                                temp_move_list.append([location[0] + piece[1],location[1] + piece[2]])
    else:
        temp_move_list = middle


def high_light_space(x,y,color):
    if [x,y] in middle:
        t.color(color)
        t.pensize(2)
        t.penup()
        t.setpos(x+25,y-25)
        t.pendown()
        for i in range(0,4):
            t.left(90)
            t.forward(50)



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
    legal = 0
    selected = order_selected[len(order_selected) - 1]
    turtle_name = selected[3]
    if x == "na" and y == "na":
        fail = 1
    for test in temp_move_list:
        if test == cord:
            legal = 1
    if legal != 1:
        fail = 1
    if turn_counter % 2 != 0 and fail != 1:
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
    elif turn_counter % 2 == 0 and fail != 1:
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
        temp_move_list.clear()
        t.clear()
        turtle_name.clear()
        turtle_name.setpos(x, y)
        turtle_name.color("black")
        turtle_name.write(selected[0] + "\n", align="center",font=("Arial",7,"bold"))
        turn_counter += 1
        wn.onclick(select)
    else:
        temp_move_list.clear()
        t.clear()
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
        legal_move(selected)
        wn.onclick(move)
    else:
        temp_move_list.clear()
        t.clear()
        wn.onclick(select)


player_one = [['turtle1', 50, 100, turtle.Turtle()], ['turtle3', 100, 100, turtle.Turtle()]]
player_one_dead = []
player_two = [['turtle2', 200, 100, turtle.Turtle()], ['turtle4', 200, 150, turtle.Turtle()]]
player_two_dead = []
movement_rules = [['turtle1',[0,50],[0,-50],[50,0]], ['turtle2',[0,50],[0,-50]], ['turtle3',[0,50],[0,-50]], ['turtle4',[0,50],[0,-50]]]
temp_move_list = []
# promotion = []
order_selected = []
middle = mid()
turn_counter = 1

wn = turtle.Screen()
wn.title("Shogi")
make_board()
make_yards()
wn.register_shape("tri", ((10,-3), (10,-20),  (-10,-20), (-10,-3), (-5,10), (5,10)))
t = turtle.Turtle()
t.ht()
t.speed(0)


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
