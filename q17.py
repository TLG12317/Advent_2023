with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])

lst2 = []
for x in lst:
    temp = []
    for letter in x:
        temp.append(int(letter))
    lst2.append(temp)
lst = lst2.copy()


direction_list = ["west", "south", "east", "north"]
coords_list = [[0,-1], [1,0], [0,1], [-1,0]]

stack = [["east", [0,0], 0, 1], ["south", [0,0], 0, 1]]
dct = {}
#starting points are (0,1) east and (1,0) south

while stack:
    direction, coords, heat_value, same_direction_multiplier = stack.pop()
    if len(lst) > coords[0] >= 0 and len(lst[0]) > coords[1] >= 0:
        if (tuple(coords),direction, same_direction_multiplier) in dct:
            if heat_value < dct[(tuple(coords),direction, same_direction_multiplier)]:
                dct[(tuple(coords),direction, same_direction_multiplier)] = heat_value
            # for d in direction_list:
            #     if 
            else:
                continue
            # else:
            #     heat_value = dct[(tuple(coords),direction)]
        else:
            dct[(tuple(coords),direction, same_direction_multiplier)] = heat_value
        y = direction_list.index(direction)
        for index in range(y-1, y+2):
            if index == 4:
                index = 0
            coords2 = coords.copy()
            for i in range(len(coords)):
                coords2[i] += coords_list[index][i]
            if len(lst) > coords2[0] >= 0 and len(lst[0]) > coords2[1] >= 0:
                heat_value2 = heat_value + lst[coords2[0]][coords2[1]]
                if direction_list[index] == direction:
                    if same_direction_multiplier <= 2:
                        stack.append([direction_list[index], coords2, heat_value2, same_direction_multiplier+1])
                else:
                    stack.append([direction_list[index], coords2, heat_value2, 1])


for d in direction_list:
    for k in range(1,4):
        x = ((140,140), d, k)
        if x in dct:
            print(dct[x], d)