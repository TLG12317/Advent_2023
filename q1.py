with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])

dct = {}
x = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
for i in range(len(x)):
    dct[x[i]] = str(i+1)

ret = 0
for st in lst:
    lst2 = []
    for i in range(len(st)):
        for j in range(i, i+6):
            if st[i:j] in ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'):
                lst2.append((i, st[i:j]))
    for j in range(len(st)):
        if st[j] in ('1','2','3','4','5','6','7','8','9'):
            lst2.append((j, st[j]))
    lst2.sort()
    a,b = lst2[0][1], lst2[-1][1]
    if a in dct:
        a = dct[a]
    if b in dct:
        b = dct[b]
    ret += int(a+b)
print(ret)
    
