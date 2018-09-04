n = int(input("Enter the length of the sequence: ")) # Do not change this line

a = 1
b = 2
c = 3

for i in range(1, n+1):
    if i == 1:
        print(a)
    elif i == 2:
        print(b)
    elif i == 3:
        print(c)
    else:
        d = a + b + c
        a = b
        b = c
        c = d
        print(d)
