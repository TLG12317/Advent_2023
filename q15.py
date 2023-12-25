with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])

# lst = lst[0].split(",")
# ret = 0
# for hesh in lst:
#     temp = 0
#     for letter in hesh:
#         temp = ((temp + ord(letter)) * 17) % 256
#     print(temp)
#     ret += temp    
# print(ret)

lst = lst[0].split(",")
lens = [[] for _ in range(256)]
for hesh in lst:
    box_number = 0
    if "=" in hesh:
        for letter in range(len(hesh)-2):
            box_number = ((box_number + ord(hesh[letter])) * 17) % 256
        found = False
        for l in lens[box_number]:
            if hesh[:-2] == l[0]:
                l[1] = int(hesh[-1])
                found = True
        if not found:
            lens[box_number].append([hesh[:-2], int(hesh[-1])])

    elif "-" in hesh:
        for letter in range(len(hesh)-1):
            box_number = ((box_number + ord(hesh[letter])) * 17) % 256
        for i in range(len(lens[box_number])):
            if lens[box_number][i][0] == hesh[:-1]:
                lens[box_number].pop(i)
                break

ret = 0
for i in range(len(lens)):
    for j in range(len(lens[i])):
        ret += (i+1) * (j+1) * lens[i][j][1]
print(ret)