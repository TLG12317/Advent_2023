with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])

#Learning outcomes
# 1. Use coordinates to represent direction instead of using NSEW
# 2. Usage of a heap to find weighted min path
# 3. use the seen set to remove loops


# from heapq import heappush, heappop

# queue = [(0,0,0,0,0,0)]
# seen = set()

# #each element records the heat loss at the point,
# #direction the heat loss came from, coords.

# while queue:
#     heat_loss, x, y, direction_x, direction_y, n = heappop(queue)
#     if (x,y,direction_x, direction_y, n) in seen:
#         continue
#     else:
#         seen.add((x,y,direction_x, direction_y, n))
#         print(x,y, heat_loss)
#         if x ==  len(lst)-1 and y == len(lst[0])-1:
#             print(heat_loss)
#             break

#         if n < 3: #same direction
#             if 0 <= x+direction_x < len(lst) and 0 <= y+direction_y < len(lst[0]):
#                 heappush(queue, (heat_loss + int(lst[x+direction_x][y + direction_y]), x+direction_x, y + direction_y, direction_x, direction_y, n+1))

#         for dx, dy in [(-1,0), (1,0), (0,1), (0,-1)]:
#             if (dx, dy) in ((direction_x, direction_y), (-direction_x, -direction_y)):
#                 continue
#             else:
#                 if 0 <= x+dx < len(lst) and 0 <= y+dy < len(lst[0]):
#                     heappush(queue, (heat_loss + int(lst[x+dx][y+dy]), x+dx, y + dy, dx, dy, 1))


# Part 2

from heapq import heappush, heappop

queue = [(0,0,0,0,1,0), (0,0,0,1,0,0)]
seen = set()

#each element records the heat loss at the point,
#direction the heat loss came from, coords.

while queue:
    heat_loss, x, y, direction_x, direction_y, n = heappop(queue)
    if (x,y,direction_x, direction_y, n) in seen:
        continue
    else:
        seen.add((x,y,direction_x, direction_y, n))
        print(x,y, heat_loss, lst[x][y])
        if x ==  len(lst)-1 and y == len(lst[0])-1:
            print(heat_loss)
            break

        if n < 10: #same direction
            if 0 <= x+direction_x < len(lst) and 0 <= y+direction_y < len(lst[0]):
                heappush(queue, (heat_loss + int(lst[x+direction_x][y + direction_y]), x+direction_x, y + direction_y, direction_x, direction_y, n+1))
        if 4 <= n:
            for dx, dy in [(-1,0), (1,0), (0,1), (0,-1)]:
                if (dx, dy) in ((direction_x, direction_y), (-direction_x, -direction_y)):
                    continue
                else:
                    if 0 <= x+dx < len(lst) and 0 <= y+dy < len(lst[0]):
                        heappush(queue, (heat_loss + int(lst[x+dx][y+dy]), x+dx, y + dy, dx, dy, 1))
