with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])


lst2 = []
ret = 0
temp_lst = []
for element in lst:
    temp = 0
    winning_numbers, picked_numbers = element.split(':')[1].split('|')
    winning_numbers = winning_numbers.split(' ')
    wins = set()
    for win in winning_numbers:
        if win != "":
            wins.add(int(win))
    picked_numbers = picked_numbers.split(' ')
    for pick in picked_numbers:
        if pick != "":
            if int(pick) in wins:
                temp += 1
    print(temp)
    temp_lst.append(temp)

from collections import Counter
dct = Counter()
print(temp_lst)
for i in range(len(lst)):
    dct[i] = 1
i = 0
while i < len(lst):
    for j in range(i+1, i+temp_lst[i]+1):
        if j == len(lst):
            break
        dct[j] += dct[i]   
    i += 1
print(sum(dct.values()))