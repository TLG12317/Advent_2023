with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])
x = ('A', 'K', 'Q', 'T', '9', 8, 7, 6, 5, 4, 3, 2, 'J')
dct = {}
dct3 = {}
for i in range(len(x)):
    dct[str(x[i])] = i
    dct3[i] = [str(x[i])]
from collections import Counter
lst2 = [[] for _ in range(7)]
for i in range(len(lst)):
    hand, bid = lst[i].split(' ')
    dct2 = Counter()
    for j in range(len(hand)):
        dct2[dct[hand[j]]] += 1
    lst5 = []
    for key, value in dct2.items():
        if key == dct["J"]:
            continue
        else:
            lst5.append([key,value])
    lst5 = sorted(lst5, key = lambda x: (-x[1], x[0]))
    if lst5 == []:
        lst5.append([12,5])
    elif 12 in dct2: #Highest count, highest strength
        lst5[0][1] += dct2[12]
    list_of_values = [x[1] for x in lst5]
    if list_of_values[0] == 5: #five of a kind
        lst2[0].append((hand,bid))
    elif 4 in list_of_values: #four of a kind
        lst2[1].append((hand,bid))
    elif 3 in list_of_values:
        if 2 in list_of_values: #full house
            lst2[2].append((hand,bid))
        else: #three of a kind
            lst2[3].append((hand,bid))
    elif list_of_values.count(2) == 2:#two pair
        lst2[4].append((hand,bid))
    elif list_of_values.count(2) == 1:
        lst2[5].append((hand,bid))
    else:
        lst2[6].append((hand,bid))
ret = []

for i in range(len(lst2)):
    if lst2[i]:
        temp = [lst2[i][0]]
        for j in range(1, len(lst2[i])):
            hand, bid = lst2[i][j]
            k = 0
            inserted = False
            while k < len(temp) and not inserted:
                for z in range(5):
                    if dct[temp[k][0][z]] > dct[hand[z]]: #temp less powerful
                        temp.insert(k, (hand, bid))
                        inserted = True
                        break
                    elif dct[temp[k][0][z]] == dct[hand[z]]:
                        continue
                    else:
                        k += 1
                        break
            if k == len(temp) and not inserted:
                temp.append((hand,bid))
        lst2[i] = temp.copy()
ret = []
for i in range(len(lst2)):
    for j in range(len(lst2[i])):
        ret.append(lst2[i][j])
ret = ret[::-1]

ans = 0
for i in range(len(ret)):
    ans += int(ret[i][1]) * (i+1)
print(ret, len(ret))
print(ans)