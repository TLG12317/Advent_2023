with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])

# import numpy as np

# ret = 0
# for i in range(len(lst)):
#     coords, speed = lst[i].split("@")
#     x1,y1,z1 = coords.split(',')
#     v1,v2,v3 = speed.split(',')
#     for j in range(i+1, len(lst)):
#         coords2, speed2 = lst[j].split("@")
#         x2,y2,z2 = coords2.split(',')
#         w1,w2,w3 = speed2.split(',')

#         coord_diff = [int(x1)-int(x2), int(y1)-int(y2)]
#         first_speed = [-int(v1), -int(v2)]
#         second_speed = [int(w1), int(w2)]
#         A = np.array([second_speed, first_speed])
#         A = A.transpose()
#         B = np.array(coord_diff)
#         try:
#             C = np.linalg.solve(A,B)
#         except np.linalg.LinAlgError:
#             pass
#         if C[0] >= 0 and C[1] >= 0:
#             #both C must be non-negative
#             x = C[0]*int(w1) + int(x2)
#             y = C[0]*int(w2) + int(y2)
#             if  200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
#                 ret += 1
# print(ret)
            

#Part 2
            

#LEARNT HOW TO USE SYMPY
# 1) sympy.symbols (small s) will accept a list of symbols
# 2) sympy.solve will taken in equations = 0 and solve em
# 3) Use t as the constant (between the rock thrown and the objects collided with), as well as same collision location. (2 constants)
            


import re
from sympy.solvers import solve
from sympy import symbols


for i in range(len(lst)):
    lst[i] = re.split(",|@", lst[i])
    for j in range(len(lst[i])):
        lst[i][j] = int(lst[i][j])
x,y,z,v1,v2,v3 = symbols("x,y,z,v1,v2,v3")
lst3 = []
for i in range(len(lst)):
    x1,y1,z1,p1,p2,p3 = lst[i]
    a = (z-z1)*(p2-v2) - (y-y1)*(p3-v3)
    b = (y-y1)*(p1-v1) - (x-x1)*(p2-v2)
    lst3.append(a)
    lst3.append(b)

answer = solve(lst3)
print(answer)
print(answer[0][x] + answer[0][y] + answer[0][z])