import sys
sys.setrecursionlimit(2000)

# with open("hi.txt") as f:
#     x = f.readlines()
#     lst = []
#     for i in range(len(x)):
#         if i != len(x)-1:
#             lst.append(x[i][:-1])
#         else:
#             lst.append(x[i])

# dct = {"|":["up","down"], 
#        "-":["left", "right"], 
#        "L":["up", "right"], 
#        "J":["up", "left"],
#        "7":["left","down"],
#        "F":["right","down"],
#        "S":["up", "down", "left", "right"],
#        ".":[]
#        }


# for row in range(len(lst)):
#     for col in range(len(lst[0])):
#         if lst[row][col] == "S":
#             initial_position = [row,col]
# #let x be coords of S
# #x[0] is row, x[1] is col
# direction = ""
# x = initial_position.copy()
# ret = 0
# print(lst[x[0]][x[1]], ret)
# while lst[x[0]][x[1]] != "S" or ret == 0:
#     row, col = x
#     if row+1 < len(lst) and direction != "up" and "up" in dct[lst[row+1][col]] and "down" in dct[lst[row][col]]:
#         row += 1
#         direction = "down"
#     elif row-1 >= 0 and direction != "down" and "down" in dct[lst[row-1][col]] and "up" in dct[lst[row][col]]:
#         direction = "up"
#         row -= 1
#     elif col - 1 >= 0 and direction != "right" and "right" in dct[lst[row][col-1]] and "left" in dct[lst[row][col]]:
#         direction = "left"
#         col -= 1
#     elif col+1 < len(lst[0]) and direction != "left" and "left" in dct[lst[row][col+1]] and "right" in dct[lst[row][col]]:
#         direction = "right"
#         col += 1
#     x = [row, col].copy()
#     ret += 1
# print(ret/2, lst[x[0]][x[1]])




with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])

dct = {"|":["up","down"], 
       "-":["left", "right"], 
       "L":["up", "right"], 
       "J":["up", "left"],
       "7":["left","down"],
       "F":["right","down"],
       "S":["up", "down", "left", "right"],
       ".":[],
       "O":[],
       "I":[],
       "*":[]
       }







for row in range(len(lst)):
    for col in range(len(lst[0])):
        if lst[row][col] == "S":
            initial_position = [row,col]
#let x be coords of S
#x[0] is row, x[1] is col
direction = ""
x = initial_position.copy()
ret = 0


seen2 = set()
seen2.add(tuple(x))

# print(lst[x[0]][x[1]], ret)
while lst[x[0]][x[1]] != "S" or ret == 0:
    row, col = x
    if row+1 < len(lst) and direction != "up" and "up" in dct[lst[row+1][col]] and "down" in dct[lst[row][col]]:
        row += 1
        direction = "down"
    elif row-1 >= 0 and direction != "down" and "down" in dct[lst[row-1][col]] and "up" in dct[lst[row][col]]:
        direction = "up"
        row -= 1
    elif col - 1 >= 0 and direction != "right" and "right" in dct[lst[row][col-1]] and "left" in dct[lst[row][col]]:
        direction = "left"
        col -= 1
    elif col+1 < len(lst[0]) and direction != "left" and "left" in dct[lst[row][col+1]] and "right" in dct[lst[row][col]]:
        direction = "right"
        col += 1
    x = [row, col].copy()
    seen2.add(tuple(x))
    ret += 1

for i in range(len(lst)):
    lst[i] = list(lst[i])

for row in range(len(lst)):
    for col in range(len(lst[0])):
        if (row, col) in seen2:
            continue
        else:
            lst[row][col] = "."


change = 0


new_lst = [[] for _ in range(len(lst))]
for row in range(len(lst)):
    for col in range(len(lst[0])):
        new_lst[row].append(lst[row][col])
        new_lst[row].append("*")

for row in range(len(new_lst)):
    for col in range(1, len(new_lst[0])-1):
        if new_lst[row][col] == "*":
            if "right" in dct[new_lst[row][col-1]] and "left" in dct[new_lst[row][col+1]]:
                new_lst[row][col] = "-"
                change += 1


x = list(map(list, zip(*new_lst)))

new_lst2 = [[] for _ in x]
for row in range(len(x)):
    for col in range(len(x[0])):
        new_lst2[row].append(x[row][col])
        new_lst2[row].append("*")
new_lst = list(map(list, zip(*new_lst2))).copy()

for row in range(len(new_lst)):
    for col in range(len(new_lst[0])):
        if new_lst[row][col] == "*" and row+1 != len(new_lst):
            if "down" in dct[new_lst[row-1][col]] and "up" in dct[new_lst[row+1][col]]:
                new_lst[row][col] = "|"
                change += 1

for row in (0,-1):
    for col in range(len(new_lst[0])):
        if new_lst[row][col] in ("*", "."):
            new_lst[row][col] = "0"
for row in range(len(new_lst)):
    for col in (0,-1):
        if new_lst[row][col] in ("*", "."):
            new_lst[row][col] = "0"


for row in range(1, len(new_lst)):
    for col in range(1, len(new_lst[0])):
        if new_lst[row][col] in ("*", "."):
            if new_lst[row-1][col] == "0":
                new_lst[row][col] = "0"
            elif new_lst[row][col-1] == "0":
                new_lst[row][col] = "0"


#flash fill
def flash_fill(x, row, col):
    if row >= 0 and col  >= 0 and row < len(new_lst) and col < len(new_lst[0]):
        if (row, col) in seen or new_lst[row][col] not in ("*", ".", "0"):
            return
        if x == 1900:
            return
        new_lst[row][col] = "0"
        seen.add((row,col))
        flash_fill(x+1, row-1,col)
        flash_fill(x+1, row, col-1)
        flash_fill(x+1, row, col+1)
        flash_fill(x+1, row+1, col)

for row in range(len(new_lst)):
    seen = set()
    for col in range(len(new_lst[0])):
        if new_lst[row][col] == "0":
            print(row,col)
            flash_fill(0, row,col)

seen = set()
for row in range(len(new_lst)):
    for col in range(len(new_lst[0])):
        if new_lst[row][col] == "0":
            print(row,col)
            flash_fill(0, row,col)


seen = set()
for row in range(len(new_lst)):
    for col in range(len(new_lst[0])):
        if new_lst[row][col] == "0":
            print(row,col)
            flash_fill(0, row,col)


#end flash fill


        
# for row in new_lst:
#     print("".join(row))

ret2 = 0
for row in range(len(new_lst)):
    for col in range(len(new_lst[0])):
        if new_lst[row][col] == ".":
            ret2 += 1

print(ret2)

