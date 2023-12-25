with open("hi.txt") as f:
    x = f.readlines()
    lst3 = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst3.append(x[i][:-1][8:])
        else:
            lst3.append(x[i][8:])

lst = []
for k in range(len(lst3)):
    if lst3[k][0] == ":":
        lst.append(lst3[k][1:])
    else:
        lst.append(lst3[k])


import re
ret = 0
for i in range(len(lst)):
    y = re.split(', |;', lst[i])
    r=g=b=0
    for j in range(len(y)):
        if 'red' in y[j]:
            z = int(y[j][:-3])
            r = max(r, z)
        elif 'green' in y[j]:
            z = int(y[j][:-5])
            g = max(g, z)
        elif 'blue' in y[j]:
            z = int(y[j][:-4])
            b = max(b, z)
    ret += r*g*b
print(ret)