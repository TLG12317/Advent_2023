with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])

for i in range(len(lst)):
    lst[i] = list(lst[i])

def north(lst):
    for col in range(len(lst[0])):
        up = nxt = 0
        while nxt < len(lst):
            while lst[up][col] == "O":
                up += 1
                nxt = up 
                if nxt >= len(lst):
                    break
            if nxt >= len(lst):
                break
            if lst[nxt][col] == "O":
                lst[nxt][col], lst[up][col] = lst[up][col], lst[nxt][col]
            elif lst[nxt][col] == "#":
                up = nxt + 1
                nxt = up 
            else:
                nxt += 1
    return lst

def cycle(lst):
    north(lst) #all goes north
    lst = [list(reversed(col)) for col in zip(*lst)]
    north(lst) #all goes west
    lst = [list(reversed(col)) for col in zip(*lst)]
    north(lst) #all goes south
    lst = [list(reversed(col)) for col in zip(*lst)]
    north(lst) #all goes east
    lst = [list(reversed(col)) for col in zip(*lst)]
    return lst

# i = 1
# while i < 1000:
#     lst = cycle(lst) #one cycle
#     i += 1

#     m = len(lst)
#     ret = 0
#     for row in range(len(lst)):
#         ret += (m-row) * lst[row].count("O")
#     print(ret, i)
#     if ret == 90592:
#         print(i)

print((10**9-1000)//34)

print(10**9 - 29411735 * 34-34)
# print((10**9-993)/7)
# print(142857001 * 7)
# for i in range(len(lst)):
#     print("".join(lst[i]))
