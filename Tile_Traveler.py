
x_pos = 1
y_pos = 1
exit_program = 0


while exit_program == 0:
    if x_pos == 1 and y_pos == 1:
        print("You can travel: (N)orth")
        move = input("Direction: ")
        if move == "n" or "N":
            y_pos += 1
            print(x_pos, y_pos)
        else: 
            print("Not a valid direction")
        continue
    elif x_pos == 1 and y_pos == 2:
        print("You can travel: (N)orth or (S)outh, (E)ast")
        move = input("Direction: ")
        if move == "n" or move == "N":
            y_pos += 1
            print(x_pos, y_pos)
        elif move == "s" or move == "S": 
            y_pos -= 1
            print(x_pos, y_pos)
        elif move == "e" or move == "E": 
            x_pos += 1
            print(x_pos, y_pos)
        else: 
            print("Not a valid direction")
        continue
    elif x_pos == 1 and y_pos == 3:
        print("You can travel: (S)outh or (E)ast" )
        move = input("Direction: ")
        if move == "s" or move == "S": 
            y_pos -= 1
            print(x_pos, y_pos)
        elif move == "e" or move == "E": 
            x_pos += 1
            print(x_pos, y_pos)
        else: 
            print("Not a valid direction")
        continue
    elif x_pos == 2 and y_pos == 1:
        print("You can travel: (N)orth" )
        move = input("Direction: ")
        if move == "n" or "N": 
            y_pos += 1
            print(x_pos, y_pos)
        else: 
            print("Not a valid direction")
        continue
    elif x_pos == 2 and y_pos == 2:
        print("You can travel: (S)outh or (W)est")
        move = input("Direction: ")
        if move == "s" or move == "S":
            y_pos -= 1
            print(x_pos, y_pos)
        elif move == "w" or move == "W":
            x_pos -= 1
            print(x_pos, y_pos)
        else: 
            print("Not a valid direction")
        continue
    elif x_pos == 2 and y_pos == 3:
        print("You can travel: (W)est or (E)ast" )
        move = input("Direction: ")
        if move == "w" or move == "W":
            x_pos -= 1
            print(x_pos, y_pos)
        elif move == "e" or move == "E":
            x_pos += 1
            print(x_pos, y_pos)
        else: 
            print("Not a valid direction")
        continue
    elif x_pos == 3 and y_pos == 2:
        print("You can travel: (N)orth or (S)outh" )
        move = input("Direction: ")
        if move == "n" or move == "N":
            y_pos += 1
            print(x_pos, y_pos)
        elif move == "s" or move == "S":
            y_pos -= 1 
            print(x_pos, y_pos)
        else: 
            print("Not a valid direction")
        continue
    elif x_pos == 3 and y_pos == 3:
        print("You can travel: (W)est or (S)outh" )
        move = input("Direction: ")
        if move == "w" or move == "W":
            x_pos -= 1
            print(x_pos, y_pos)
        elif move == "s" or move == "S":
            y_pos -= 1
            print(x_pos, y_pos)
        else: 
            print("Not a valid direction")
        continue
    elif x_pos == 3 and y_pos == 1:
        print("Victory!")
        exit_program = 1
    
    

        
    


