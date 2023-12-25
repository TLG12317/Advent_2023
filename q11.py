with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])

# x = []
# for row in lst:
#     x.append(row)
#     if row.count("#") == 0:
#         x.append(row)

# lst = list(map(list, zip(*x)))

# x = []
# for col in lst:
#     x.append(col)
#     if col.count("#") == 0:
#         x.append(col)

# lst = list(map(list, zip(*x)))
# x = []
# for row in lst:
#     x.append("".join(row))
# lst = x.copy()

# star = []
# for row in range(len(lst)):
#     for col in range(len(lst[0])):
#         if lst[row][col] == "#":
#             star.append((row,col))
# print(star)
# ret = 0
# for i in range(len(star)-1):
#     for j in range(i+1, len(star)):
#         ret += abs(star[i][0] - star[j][0])
#         ret += abs(star[i][1] - star[j][1])



# print(ret)



rows = []
for row in range(len(lst)):
    if lst[row].count("#") == 0:
        rows.append(row)

lst2 = list(map(list, zip(*lst)))

cols = []
for col in range(len(lst2)):
    if lst2[col].count("#") == 0:
        cols.append(col)

stars = []
for row in range(len(lst)):
    for col in range(len(lst[0])):
        if lst[row][col] == "#":
            stars.append((row,col))

ret = 0
for i in range(len(stars)-1):
    for j in range(i, len(stars)):
        (x1,y1),(x2,y2) = stars[i], stars[j]
        if x2 > x1:
            x1, x2 = x2, x1
        if y2 > y1:
            y1, y2 = y2, y1
        for row in rows:
            if x2 < row < x1:
                ret += 1000000 - 1
        for col in cols:
            if y2 < col < y1:
                ret += 1000000 - 1
        ret += x1 + y1 - x2 - y2
print(ret)