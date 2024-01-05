with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])
#Part 1

# start = ((-1,-1), (0, 1), 0)

# stack = [start] #prev coords, curr coords, steps taken
# lst2 = []
# while stack:
#     prev_coords, curr_coords, steps = stack.pop()
#     if curr_coords == (len(lst)-1, len(lst[0])-2):
#         lst2.append(steps)
#         continue
#     else:
#         next_coords = [0,0]
#         for direction in [(-1,0),(1,0),(0,1),(0,-1)]:
#             next_coords[0] = curr_coords[0] + direction[0]
#             next_coords[1] = curr_coords[1] + direction[1]
#             if 0 <= next_coords[0] < len(lst) and 0 <= next_coords[1] < len(lst[0]): 
#                 if direction[0] == -1 and lst[next_coords[0]][next_coords[1]] == "v":
#                     print(next_coords)
#                     continue
#                 elif direction[1] == -1 and lst[next_coords[0]][next_coords[1]] == ">":
#                     continue
#                 elif tuple(next_coords) != prev_coords and lst[next_coords[0]][next_coords[1]] != "#":
#                     stack.append((curr_coords, tuple(next_coords), steps + 1))

# print(lst2)
# print(max(lst2))
            
#Part 2
            
            
# from heapq import heappush, heappop
# start = (set(), (0, 1), 0)
# stack = [start] #prev coords, curr coords, steps taken

# ret = 0

# while stack:
#     prev_coords_set, curr_coords, steps = heappop(stack)
#     print(curr_coords, steps)
#     if curr_coords == (len(lst)-1, len(lst[0])-2):
#         ret = max(ret, steps)
#         continue
#     else:
#         next_coords = [0,0]
#         for direction in [(-1,0),(1,0),(0,1),(0,-1)]:
#             next_coords[0] = curr_coords[0] + direction[0]
#             next_coords[1] = curr_coords[1] + direction[1]
#             if 0 <= next_coords[0] < len(lst) and 0 <= next_coords[1] < len(lst[0]):
#                 if tuple(next_coords) in prev_coords_set:
#                     continue
#                 elif lst[next_coords[0]][next_coords[1]] != "#":
#                     prev_coords_set.add(curr_coords)
#                     heappush(stack, (prev_coords_set.copy(), tuple(next_coords), steps + 1))

# print(ret)
    
#connector theory
# from collections import defaultdict

# start = ((0,1), set(), (0, 1), 0)
# stack = [start] #prev coords, curr coords, steps taken
# ret = 0
# dct = defaultdict(lambda:set())

# while stack:
#     prev_connector, prev_coords_set, curr_coords, steps = stack.pop()
#     print(curr_coords, steps)
#     if curr_coords == (len(lst)-1, len(lst[0])-2):
#         ret = max(ret, steps)
#         continue
#     else:
#         next_coords = [0,0]
#         k = 0
#         for direction in [(-1,0),(1,0),(0,1),(0,-1)]:
#             next_coords[0] = curr_coords[0] + direction[0]
#             next_coords[1] = curr_coords[1] + direction[1]
#             if 0 <= next_coords[0] < len(lst) and 0 <= next_coords[1] < len(lst[0]):
#                 if tuple(next_coords) in prev_coords_set:
#                     k += 1
#                     continue
#                 elif lst[next_coords[0]][next_coords[1]] != "#":
#                     k += 1
#         if k >= 3:
#             next_coords = [0,0]
#             for direction in [(-1,0),(1,0),(0,1),(0,-1)]:
#                 next_coords[0] = curr_coords[0] + direction[0]
#                 next_coords[1] = curr_coords[1] + direction[1]
#                 if 0 <= next_coords[0] < len(lst) and 0 <= next_coords[1] < len(lst[0]):
#                     if tuple(next_coords) in prev_coords_set:
#                         continue
#                     elif lst[next_coords[0]][next_coords[1]] != "#":
#                         prev_coords_set.add(curr_coords)
#                         dct[prev_connector].add((steps, curr_coords))
#                         dct[curr_coords].add((steps, prev_connector))
#                         stack.append((curr_coords, prev_coords_set.copy(), tuple(next_coords), 0)) 
#         else:
#             next_coords = [0,0]
#             for direction in [(-1,0),(1,0),(0,1),(0,-1)]:
#                 next_coords[0] = curr_coords[0] + direction[0]
#                 next_coords[1] = curr_coords[1] + direction[1]
#                 if 0 <= next_coords[0] < len(lst) and 0 <= next_coords[1] < len(lst[0]):
#                     if tuple(next_coords) in prev_coords_set:
#                         continue
#                     elif lst[next_coords[0]][next_coords[1]] != "#":
#                         prev_coords_set.add(curr_coords)
#                         stack.append((prev_connector, prev_coords_set.copy(), tuple(next_coords), steps + 1))


# dct2 = defaultdict(lambda:[])

# for key, value in dct.items():
#     if key == (0,1): 
#         dct2[key].append((15, (5,3)))
#     else:
#         for v in value:
#             if (0,1) not in v:
#                 dct2[key].append(v)

# print(dct2)

# stack2 = [(-1, set(), (0,1))]
# ret = 0

# while stack2:
#     steps, prev_coords, coords = stack2.pop()
#     if coords in prev_coords:
#         continue
#     else:
#         if coords == (len(lst)-4, len(lst[0])-4):
#             ret = max(ret, steps)
#         prev_coords.add(coords)
#         for next_step, next_coord in dct[coords]:
#             stack2.append((steps+next_step+1, prev_coords.copy(), next_coord))
    
# print(dct2)
# print(ret)

# start = (set(), (19,19), 0)
# stack = [start] #prev coords, curr coords, steps taken

# q = shortest(start, stack)

# print(ret + q)


#find all the connection points
#Use global seen in order to find connections without loop ***
#Local seen does not work



points = set()
points.add((len(lst)-1, len(lst[0])-2))


for row in range(len(lst)):
    for col in range(len(lst[0])):
        if lst[row][col] != "#":
            k = 0
            for direction in [(-1,0),(1,0),(0,1),(0,-1)]:
                if 0 <= row + direction[0] < len(lst) and 0 <= col + direction[1] < len(lst[0]):
                    if lst[row+direction[0]][col+direction[1]] != "#":
                        k += 1
            if k >= 3:
                points.add((row, col))
from collections import defaultdict
from tkinter.messagebox import RETRY

graph = defaultdict(lambda:{})
seen = set()

start = (0,1)
stack = [[start, start, 0]] #coords, steps

while stack:
    prev_conn, coords, steps = stack.pop()
    if coords in seen:
        if coords in points:
            if coords != prev_conn:
                graph[prev_conn][coords] = steps
                graph[coords][prev_conn] = steps
        else:
            continue
    else:
        if coords in points:
            graph[prev_conn][coords] = steps
            graph[coords][prev_conn] = steps
            prev_conn = coords
            steps = 0
        seen.add(coords)
        row, col = coords
        for direction in [(-1,0),(1,0),(0,1),(0,-1)]:
            if 0 <= row + direction[0] < len(lst) and 0 <= col + direction[1] < len(lst[0]):
                    if lst[row+direction[0]][col+direction[1]] != "#":  
                        stack.append([prev_conn, (row+direction[0],col+direction[1]), steps + 1])

stack = [(set(), (0,1), 0)]

end = (len(lst)-1, len(lst[0])-2)
ret = 0


while stack:
    seen, coord2, step2 = stack.pop()
    print(coord2, step2)
    if coord2 in seen:
        continue
    else:
        seen.add(coord2)
        if coord2 == end:
            ret = max(ret, step2)
            print(ret)
            continue
        else:
            for nxt_coord in graph[coord2]:
                print(nxt_coord, len(seen), len(stack))
                stack.append((seen.copy(), nxt_coord, step2+graph[coord2][nxt_coord]))


print(ret)

#4674 too low
#6302 too low
#6494 GArbage brute force.


# start = ((-1,-1), (0, 1), 0)

# stack = [start] #prev coords, curr coords, steps taken
# lst2 = []
# while stack:
#     prev_coords, curr_coords, steps = stack.pop()
#     if curr_coords == (len(lst)-1, len(lst[0])-2):
#         lst2.append(steps)
#         continue
#     else:
#         next_coords = [0,0]
#         for direction in [(-1,0),(1,0),(0,1),(0,-1)]:
#             next_coords[0] = curr_coords[0] + direction[0]
#             next_coords[1] = curr_coords[1] + direction[1]
#             if 0 <= next_coords[0] < len(lst) and 0 <= next_coords[1] < len(lst[0]): 
#                 if direction[0] == -1 and lst[next_coords[0]][next_coords[1]] == "v":
#                     print(next_coords)
#                     continue
#                 elif direction[1] == -1 and lst[next_coords[0]][next_coords[1]] == ">":
#                     continue
#                 elif tuple(next_coords) != prev_coords and lst[next_coords[0]][next_coords[1]] != "#":
#                     stack.append((curr_coords, tuple(next_coords), steps + 1))

# print(lst2)
# print(max(lst2))
            



