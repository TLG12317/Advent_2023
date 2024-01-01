with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])

# 1. shoelace formula
# 2. Pick's theorem



# for i in range(len(lst)):
#     lst[i] = lst[i].split(" ")
#     lst[i] = [lst[i][0], int(lst[i][1])]

# coords = [(0,0)]

# dct = {"U":(-1,0), "D":(1,0), "L":(0,-1), "R":(0,1)}
# ext_points = 0

# for i in range(len(lst)):
#     r,c = coords[-1]
#     dr, dc = dct[lst[i][0]]
#     multiplier = lst[i][1]
#     ext_points += multiplier
#     dr *= multiplier
#     dc *= multiplier
#     coords.append((r+dr, c+dc))
# A=B=0
# for j in range(1, len(coords)):
#     A += coords[j][1] * coords[j-1][0]
#     B += coords[j][0] * coords[j-1][1]
# area = abs(A-B) // 2
# interior_points = area - ext_points//2 + 1
# print(interior_points+ext_points)
            

dct = {"0":"R", "1":"D", "2":"L", "3":"U"}

for i in range(len(lst)):
    lst[i] = lst[i].split(" ")[2]
    lst[i] = [dct[lst[i][7]], int(lst[i][2:7], 16)]

coords = [(0,0)]

dct = {"U":(-1,0), "D":(1,0), "L":(0,-1), "R":(0,1)}
ext_points = 0

for i in range(len(lst)):
    r,c = coords[-1]
    dr, dc = dct[lst[i][0]]
    multiplier = lst[i][1]
    ext_points += multiplier
    dr *= multiplier
    dc *= multiplier
    coords.append((r+dr, c+dc))
A=B=0
for j in range(1, len(coords)):
    A += coords[j][1] * coords[j-1][0]
    B += coords[j][0] * coords[j-1][1]
area = abs(A-B) // 2
interior_points = area - ext_points//2 + 1
print(interior_points+ext_points)