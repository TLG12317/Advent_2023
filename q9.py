import tempfile


with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])

x = []
for element in lst:
    x.append(element.split(' '))
for ele in x:
    for i in range(len(ele)):
        ele[i] = int(ele[i])

final = 0
for temp in x:
    ret = 0
    k = temp[0]
    index = 1
    while temp[0] != 0 or temp[-1] != 0:
        temp2 = []
        for i in range(1, len(temp)):
            temp2.append(temp[i]-temp[i-1])
        temp = temp2.copy()
        ret += temp[0] * (-1)**index
        index += 1
    final += ret + k
print(final)