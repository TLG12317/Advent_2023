with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])



x = lst[2:]

ins = lst[0]
dct = {}
words = []
for i in range(len(x)):
    coord_from = x[i].split('=')[0][:-1]
    if coord_from[-1] == "A":
        words.append(coord_from)
    coords1, coords2 = x[i].split('=')[1][2:-1].split(",")
    coords2 = coords2[1:]
    dct[coord_from] = (coords1,coords2)


fin = []
for word in words:
    ret = i = 0
    while True:
        if word[-1] == "Z":
            break
        if i == len(ins):
            i = 0
        if ins[i] == "R":
            word = dct[word][1]
        else:
            word = dct[word][0]
        ret += 1
        i += 1
    fin.append(ret)
import math
from functools import reduce

def lcm(arr):

    l=reduce(lambda x,y:(x*y)//math.gcd(x,y),arr)
    return l

print(lcm(fin))