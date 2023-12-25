with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])

import numpy as np

ret = 0
for i in range(len(lst)):
    coords, speed = lst[i].split("@")
    x1,y1,z1 = coords.split(',')
    v1,v2,v3 = speed.split(',')
    for j in range(i+1, len(lst)):
        coords2, speed2 = lst[j].split("@")
        x2,y2,z2 = coords2.split(',')
        w1,w2,w3 = speed2.split(',')

        coord_diff = [int(x1)-int(x2), int(y1)-int(y2)]
        first_speed = [-int(v1), -int(v2)]
        second_speed = [int(w1), int(w2)]
        A = np.array([second_speed, first_speed])
        A = A.transpose()
        B = np.array(coord_diff)
        try:
            C = np.linalg.solve(A,B)
        except np.linalg.LinAlgError:
            pass
        if C[0] >= 0 and C[1] >= 0:
            #both C must be non-negative
            x = C[0]*int(w1) + int(x2)
            y = C[0]*int(w2) + int(y2)
            if  200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
                ret += 1
print(ret)