def first_name(first_name_last_name):
    for place_in_name in range(1, len(first_name_last_name)):
        if first_name_last_name[place_in_name] == " ":
            return first_name_last_name[0:place_in_name]


def last_name(first_name_last_name):
    fin = 0
    found = 0
    first_space = 0
    second_space = 0
    for place_in_name in range(1, len(first_name_last_name)):
        if fin == 1 and first_name_last_name[place_in_name] == " ":
            second_space = place_in_name
            found = 1
        elif first_name_last_name[place_in_name] == " ":
            first_space = place_in_name
            fin = 1
    if found == 0:
        second_space = len(first_name_last_name)
    return first_name_last_name[first_space+1:second_space]


promt = ["The Friend List", "", "1. Add a new friend to the end", "2. Insert a new friend in a specific index location",
         "3. Delete a friend by index or name", "4. Print a numbered list of friends to the screen",
         "5. Sort the list alphabetically", "6. Save the list to a file (files)", "7. Load a list from a file",
         "8. Exit"]
for i in promt:
    print(i)
friend_list = []

command = int(input("Command: "))
while command != 8:
    counter_main = 0

    if command == 1:
        name_in = input("Name: ")
        f_name = first_name(name_in)
        l_name = last_name(name_in)
        email = input("Email: ")
        phone = input("Phone Number: ")
        person = [f_name, l_name, email, phone]
        friend_list.append(person)
        command = int(input("Command: "))

    elif command == 2:
        name_in = input("Name: ")
        f_name = first_name(name_in)
        l_name = last_name(name_in)
        email = input("Email: ")
        phone = input("Phone Number: ")
        location = int(input("Place: "))
        person = [f_name, l_name, email, phone]
        friend_list.insert(location, person)
        command = int(input("Command: "))

    elif command == 3:
        num = input("Index or Name: ")
        if 30 <= ord(num[0]) <= 39:
            del friend_list[int(num) - 1:int(num)]
        else:
            f_name = first_name(num)
            l_name = last_name(num)
            for x in friend_list:
                if f_name == x[0] and l_name == x[1]:
                    friend_list.remove(x)
        command = int(input("Command: "))

    elif command == 4:
        reff = friend_list[0:5]
        done = 0
        done_prep = 0
        while done != 1:
            for i in reff:
                counter_main += 1
                print(str(counter_main) + ".", str(i[0]) + " " + str(i[1]))
            if done_prep == 1 or len(friend_list) < 5:
                done = 1
            else:
                cont = input("Continue(c) or Stop(any other key): ")
                if cont == "c":
                    if counter_main + 5 < len(friend_list):
                        reff = friend_list[counter_main:counter_main + 5]
                    else:
                        reff = friend_list[counter_main:len(friend_list)]
                        done_prep = 1
                else:
                    done = 1
        command = int(input("Command: "))

    elif command == 5:
        l_o_f = int(input("First Name(1) or Last Name(2): "))
        first_or_last = []
        if l_o_f == 1:
            for q in friend_list:
                first_or_last.append(q[0])
        elif l_o_f == 2:
            for q in friend_list:
                first_or_last.append(q[1])
        for i in range(1, len(friend_list)):
            for index_in_list in range(1, len(first_or_last)):
                name_one = first_or_last[index_in_list - 1]
                name_two = first_or_last[index_in_list]
                done = 0
                if ord(name_one[1]) > ord(name_two[1]):
                    reff = friend_list[:]
                    reff_n = first_or_last[:]
                    del friend_list[index_in_list - 1]
                    del first_or_last[index_in_list - 1]
                    friend_list.insert(index_in_list, reff[index_in_list - 1])
                    first_or_last.insert(index_in_list, reff_n[index_in_list - 1])
                elif ord(name_one[1]) == ord(name_two[1]):
                    for place in range(2, min(len(name_one), len(name_two))):
                        if ord(name_one[place]) > ord(name_two[place]):
                            reff = friend_list[:]
                            reff_n = first_or_last[:]
                            del friend_list[index_in_list - 1]
                            del first_or_last[index_in_list - 1]
                            friend_list.insert(index_in_list, reff[index_in_list - 1])
                            first_or_last.insert(index_in_list, reff_n[index_in_list - 1])
                            done += 1
                    if done == 0:
                        if len(name_one) > len(name_two):
                            reff = friend_list[:]
                            reff_n = first_or_last[:]
                            del friend_list[index_in_list - 1]
                            del first_or_last[index_in_list - 1]
                            friend_list.insert(index_in_list, reff[index_in_list - 1])
                            first_or_last.insert(index_in_list, reff_n[index_in_list - 1])
        command = int(input("Command: "))

    elif command == 6:
        name = input("Name: ")
        file = open(name, "w")
        for i in friend_list:
            counter_main += 1
            file.write(str(counter_main) + ". ")
            for n in i:
                file.write(n + " ")
            file.write("\n")
        file.close()
        command = int(input("Command: "))

    elif command == 7:
        name = input("Name: ")
        read = open(name, "r")
        line_in_one = str(read.readline())
        line_in = line_in_one[0:len(line_in_one) - 1] + " "
        while line_in != " ":
            person = []
            start = 0
            check = 0
            done = 0
            search = 0
            for dot in range(0, len(line_in)):
                if done != 1:
                    if line_in[dot] == ".":
                        start = dot + 2
                        search = dot + 1
                        done = 1
            for i in range(start, len(line_in)):
                if line_in[i] == " ":
                    person.append(line_in[search + 1:i])
                    search = i
            for q in friend_list:
                if q[1] == person[1] and q[0] == person[0]:
                    check = 1
            if check != 1:
                friend_list.append(person)
            line_in_one = str(read.readline())
            line_in = line_in_one[0:len(line_in_one) - 1] + " "
        read.close()
        command = int(input("Command: "))

    else:
        command = int(input("Command: "))
