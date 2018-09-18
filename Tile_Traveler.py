x_pos = 1
y_pos = 1

while x_pos != 3 and y_pos != 2:
    print("You can Travel: ")
    direction = input("Direction:")
    if direction is "w" and x_pos >= 1:
        x_pos -= 1
    elif direction is "e" and x_pos <= 3:
        x_pos += 1
    elif direction is "n" and y_pos >= 3:
        y_pos += 1
    elif direction is "s" and y_pos <= 1:
        y_pos -= 1
    else: 
        break

print(x_pos)
print(y_pos)


