import numbers


with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])


for row in range(len(lst)):
    for col in range(len(lst[0])):
        if lst[row][col] == "S":
            start = (row, col, 0)
            break

dct = {}
dct[(start[0], start[1])] = 0


stack = [start]

while stack:
    row, col, number = stack.pop()
    if (row, col) in dct:
        if number > dct[]
    if row == len(lst)-1:
        break
    if row-1 >= 0 and lst[row-1][col] == ".":
        start
    if row+1 < len(lst) and lst[row+1][col] == ".":
    
    if col-1>=0 and lst[row][col-1] == ".":

    if col+1 < len(lst[0]) and lst[row][col+1] == "."


print(number)