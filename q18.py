with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])

# mat = [["." for _ in range(750)] for _ in range(500)] 

# lst2 = []
# for l in lst:
#     lst2.append(l.split(" "))

# directions = ["R", "L", "U", "D"]
# movement = [(0,1), (0,-1), (-1,0), (1,0)]

# pos = [250,250]
# mat[250][250] = "#"

# for i in range(len(lst2)):
#     direct = lst2[i][0]
#     for k in range(int(lst2[i][1])):
#         for j in range(len(pos)):
#             pos[j] += movement[directions.index(direct)][j]
#         mat[pos[0]][pos[1]] = "#"

# stack = [[0,0]]

# while stack:
#     x = stack.pop()
#     if x[0] < 0 or x[1] < 0 or x[0] >= len(mat) or x[1] >= len(mat[0]):
#         continue
#     elif mat[x[0]][x[1]] in ("#", "!"):
#         continue
#     else:
#         mat[x[0]][x[1]] = "!"
#         for move in movement:
#             pos2 = x.copy()
#             for j in range(len(pos2)):
#                 pos2[j]+= move[j]
#             stack.append(pos2)

# for m in mat:
#     print("".join(m))

# exclaim = 0
# for row in range(len(mat)):
#     for col in range(len(mat[0])):
#         if mat[row][col] in ("!"):
#             exclaim += 1
# total = len(mat) * len(mat[0])

# print(total - exclaim)
            



lst2 = []
for l in lst:
    lst2.append(l.split(" "))

directions = ["R", "L", "U", "D"]
movement = [(0,1), (0,-1), (-1,0), (1,0)]

pos = [250,250]
boundary = set()

miny = minx = float("inf")
maxy = maxx = 0

for i in range(len(lst2)):
    direct = lst2[i][0]
    for k in range(int(lst2[i][1])):
        for j in range(len(pos)):
            pos[j] += movement[directions.index(direct)][j]
        x,y = pos
        minx = min(x, minx)
        maxx = max(x, maxx)
        miny = min(y, miny)
        maxy = max(y, maxy)
        boundary.add(tuple(pos))



ret = 0
for row in range(minx, maxx+1):
    points_intersected = []
    for bound in boundary:
        if bound[0] == row:
            points_intersected.append(bound)
    points_intersected.sort(key= lambda x: x[1])
    print(points_intersected)
    i = 1
    inside = True
    while i < len(points_intersected):
        diff = points_intersected[i][1] - points_intersected[i-1][1]
        if diff == 1:
            ret += 1
        else:
            if inside:
                inside = False
                ret += diff + 1
            else:
                inside = True
        i += 1
    ret += 1 
    print(ret)

    # for i in range(1,len(points_intersected)):
    #     ret += points_intersected[i][1] - points_intersected[i-1][1]
    # ret += 1
    # print(ret)

print(len(boundary), minx, miny, maxx, maxy)
print(ret)
