with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])


# stack = [['down', [0,0]]] #change this

# dct = {"up":[-1,0], "down":[1,0], "left":[0,-1], "right":[0,1]}
# indices = ["up", "down", "left", "right"]

# dct2 = {
#     "|":[["up"], ["down"], ["up", "down"], ["up", "down"]],
#     "-":[["left", "right"], ["left", "right"], ["left"], ["right"]],
#     "/":[["right"], ["left"], ["down"], ["up"]],
#     "\\": [["left"], ["right"], ["up"], ["down"]]
# }

# seen = set()

# while stack:
#     x = stack.pop()
#     direction, coords = x[0], x[1]
#     if (direction, tuple(coords)) in seen or coords[0] < 0 or coords[1] < 0 or coords[0] >= len(lst) or coords[1] >= len(lst[0]):
#         continue
#     else:
#         seen.add((direction, tuple(coords)))
#         print(coords, direction)
#         for i in range(len(coords)):
#             coords[i] += dct[direction][i] 
#         if coords[0] < 0 or coords[1] < 0 or coords[0] >= len(lst) or coords[1] >= len(lst[0]):
#             continue
#         elif lst[coords[0]][coords[1]] in dct2:
#             y = indices.index(direction)
#             for new_direction in dct2[lst[coords[0]][coords[1]]][y]:
#                 stack.append([new_direction, coords.copy()])
#         else:
#             stack.append([direction, coords])

# seen2 = set()
# for s in seen:
#     seen2.add(s[1])

# print(len(seen2))
            
def checker(stack):
    seen = set()

    while stack:
        x = stack.pop()
        direction, coords = x[0], x[1]
        if (direction, tuple(coords)) in seen or coords[0] < 0 or coords[1] < 0 or coords[0] >= len(lst) or coords[1] >= len(lst[0]):
            continue
        else:
            seen.add((direction, tuple(coords)))
            # print(coords, direction)
            for i in range(len(coords)):
                coords[i] += dct[direction][i] 
            if coords[0] < 0 or coords[1] < 0 or coords[0] >= len(lst) or coords[1] >= len(lst[0]):
                continue
            elif lst[coords[0]][coords[1]] in dct2:
                y = indices.index(direction)
                for new_direction in dct2[lst[coords[0]][coords[1]]][y]:
                    stack.append([new_direction, coords.copy()])
            else:
                stack.append([direction, coords])

    seen2 = set()
    for s in seen:
        seen2.add(s[1])

    return len(seen2)



dct = {"up":[-1,0], "down":[1,0], "left":[0,-1], "right":[0,1]}
indices = ["up", "down", "left", "right"]

dct2 = {
    "|":[["up"], ["down"], ["up", "down"], ["up", "down"]],
    "-":[["left", "right"], ["left", "right"], ["left"], ["right"]],
    "/":[["right"], ["left"], ["down"], ["up"]],
    "\\": [["left"], ["right"], ["up"], ["down"]]
}

stack = [['right', [0,0]]] #change this

res = 0

for i in range(len(lst)):
    stack = []
    if lst[i][0] in dct2:
        y = indices.index("right")
        for new_direction in dct2[lst[i][0]][y]:
            stack.append([new_direction, [i,0].copy()])
    else:
        stack.append(["right", [i,0].copy()])
    print(stack)
    res = max(res, checker(stack))

for i in range(len(lst)):
    stack = []
    if lst[i][len(lst)-1] in dct2:
        y = indices.index("left")
        for new_direction in dct2[lst[i][len(lst)-1]][y]:
            stack.append([new_direction, [i,len(lst)-1].copy()])
    else:
        stack.append(["left", [i,len(lst)-1].copy()])
    print(stack)
    res = max(res, checker(stack))

for i in range(len(lst[0])):
    stack = []
    if lst[0][i] in dct2:
        y = indices.index("down")
        for new_direction in dct2[lst[0][i]][y]:
            stack.append([new_direction, [0,i].copy()])
    else:
        stack.append(["down", [0,i].copy()])
    print(stack)
    res = max(res, checker(stack))

for i in range(len(lst[0])):
    stack = []
    if lst[len(lst[0])-1][i] in dct2:
        y = indices.index("up")
        for new_direction in dct2[lst[len(lst[0])-1][i]][y]:
            stack.append([new_direction, [len(lst[0])-1,i].copy()])
    else:
        stack.append(["up", [len(lst[0])-1,i].copy()])
    print(stack)
    # "right", lst[i][0], "left", lst[i][-1]
    res = max(res, checker(stack))


print(res)