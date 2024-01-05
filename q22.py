with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])


# 1) Use else statements to help see if there are any missing cases
# in this case it was the case when x1==x2, y1==y2 and z1==z2

# import re

# for i in range(len(lst)):
#     lst[i] = re.split('~|,', lst[i])
#     for j in range(len(lst[i])):
#         lst[i][j] = int(lst[i][j])

# lst = sorted(lst, key=lambda x:x[2])
# lst2 = []
# seen = {}

# for k in range(len(lst)):
#     x1,y1,z1,x2,y2,z2 = lst[k]
#     if z1 == 1:
#         for x in range(x1, x2+1):
#             seen[(x, y1, z1)] = k
#         for y in range(y1, y2+1):
#             seen[(x1, y, z1)] = k
#         for z in range(z1, z2+1):
#             seen[(x1,y1,z)]  = k
#         lst2.append((x1,y1,z1,x2,y2,z2)) 
#     elif x1 != x2:
#         x = x1
#         while True:
#             if z1==1 or (x, y1, z1-1) in seen:
#                 break
#             elif x == x2:
#                 z1 -= 1
#                 z2 -= 1
#                 x = x1
#             else:
#                 x += 1
#         for x in range(x1, x2+1):
#             seen[(x, y1, z1)]=k
#         lst2.append((x1,y1,z1,x2,y2,z2)) 
#     elif y1 != y2:
#         y = y1
#         while True:
#             if z1==1 or (x1, y, z1-1) in seen:
#                 break
#             elif y == y2:
#                 z1 -= 1
#                 z2 -= 1
#                 y = y1
#             else:
#                 y += 1
#         for y in range(y1, y2+1):
#             seen[(x1, y, z1)]=k
#         lst2.append((x1,y1,z1,x2,y2,z2)) 
#     else:
#         while True:
#             if z1==1 or (x1,y1,z1-1) in seen:
#                 break
#             else:
#                 z1 -= 1
#                 z2 -= 1
#         for z in range(z1, z2+1):
#             seen[(x1, y1, z)]=k
#         # seen[(x1,y1,z2)] = k
#         lst2.append((x1,y1,z1,x2,y2,z2))

# unremovable = set()
# for block in lst2:
#     kuh = set()
#     x1,y1,z1,x2,y2,z2 = block
#     if x1 != x2:
#         for x in range(x1, x2+1):
#             if (x, y1, z1-1) in seen:
#                 kuh.add(seen[(x, y1, z1-1)])
#     elif y1 != y2:
#         for y in range(y1, y2+1):
#             if (x1, y, z1-1) in seen:
#                 kuh.add(seen[(x1, y, z1-1)])
#     else:
#         if (x1, y1, z1-1) in seen:
#             kuh.add(seen[(x1, y1, z1-1)])
#     # print(block, kuh)
#     if len(kuh) == 1:
#         unremovable.add(kuh.pop())
# # print(seen)
# # print(len(lst))
# # print(len(lst2))
# # print(lst2)
# # print(unremovable)
# # print(len(unremovable))
# print(len(lst) - len(unremovable))
            
#Part 2

from email.policy import default
import re

for i in range(len(lst)):
    lst[i] = re.split('~|,', lst[i])
    for j in range(len(lst[i])):
        lst[i][j] = int(lst[i][j])

lst = sorted(lst, key=lambda x:x[2])
lst2 = []
seen = {}

for k in range(len(lst)):
    x1,y1,z1,x2,y2,z2 = lst[k]
    if z1 == 1:
        for x in range(x1, x2+1):
            seen[(x, y1, z1)] = k
        for y in range(y1, y2+1):
            seen[(x1, y, z1)] = k
        for z in range(z1, z2+1):
            seen[(x1,y1,z)]  = k
        lst2.append((x1,y1,z1,x2,y2,z2)) 
    elif x1 != x2:
        x = x1
        while True:
            if z1==1 or (x, y1, z1-1) in seen:
                break
            elif x == x2:
                z1 -= 1
                z2 -= 1
                x = x1
            else:
                x += 1
        for x in range(x1, x2+1):
            seen[(x, y1, z1)]=k
        lst2.append((x1,y1,z1,x2,y2,z2)) 
    elif y1 != y2:
        y = y1
        while True:
            if z1==1 or (x1, y, z1-1) in seen:
                break
            elif y == y2:
                z1 -= 1
                z2 -= 1
                y = y1
            else:
                y += 1
        for y in range(y1, y2+1):
            seen[(x1, y, z1)]=k
        lst2.append((x1,y1,z1,x2,y2,z2)) 
    else:
        while True:
            if z1==1 or (x1,y1,z1-1) in seen:
                break
            else:
                z1 -= 1
                z2 -= 1
        for z in range(z1, z2+1):
            seen[(x1, y1, z)]=k
        # seen[(x1,y1,z2)] = k
        lst2.append((x1,y1,z1,x2,y2,z2))

from collections import defaultdict
graph = defaultdict(lambda: [])
graph2 = defaultdict(lambda: [])
unremovable = set()
for block in lst2:
    kuh = set()
    x1,y1,z1,x2,y2,z2 = block
    if x1 != x2:
        for x in range(x1, x2+1):
            if (x, y1, z1-1) in seen:
                kuh.add(seen[(x, y1, z1-1)])
    elif y1 != y2:
        for y in range(y1, y2+1):
            if (x1, y, z1-1) in seen:
                kuh.add(seen[(x1, y, z1-1)])
    else:
        if (x1, y1, z1-1) in seen:
            kuh.add(seen[(x1, y1, z1-1)])
    graph2[seen[block[:3]]].append(kuh)
    for element in kuh:
        graph[element].append(seen[block[:3]])
    if len(kuh) == 1: #one thing in kuh supporting curr element
        elem = kuh.pop()
        kuh.add(elem)
        unremovable.add(elem)
# print(seen)
# print(len(lst))
# print(len(lst2))
# print(lst2)
# print(unremovable)
# print(len(unremovable))
# print(len(lst) - len(unremovable))
        
#value sits on key
# print(len(graph))
dct = {}
def recur(x, element):
    x.add(element)
    # if element in dct:
    #     return dct[element]
    lst = []
    for sitting_on_top in graph[element]:
        flag = True
        for se in graph2[sitting_on_top]:
            for below in se:
                if below in x:
                    continue
                else:
                    flag = False
                    break
        if flag:
            lst.append(sitting_on_top)
            x.add(sitting_on_top)
    for l in lst:
        h = recur(x,l)
        if h:
            for k in h:
                x.add(k)
    # dct[element] = x
    return x

# print(graph2)
# #what if the thing that collapses actually has anotber brick besides?


#graph is value on key
#graph2 is key on value

res = step = 0
for remove in unremovable:
    step += 1
    hi = recur(set(), remove)
    if hi:
        res += len(hi)
    print(remove, res)
print(res - len(unremovable))