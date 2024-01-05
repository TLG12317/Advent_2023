with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])



print(lst)

seen = set()
blockage = set()
for row in range(len(lst)):
    for col in range(len(lst[0])):
        if lst[row][col] == "S":
            seen.add((row, col))
        elif lst[row][col] == "#":
            blockage.add((row,col))


seen = set()
blockage = set()
for row in range(len(lst)):
    for col in range(len(lst[0])):
        if lst[row][col] == "S":
            seen.add((row, col))
        elif lst[row][col] == "#":
            blockage.add((row,col))

    step = 1
    seen2 = set()
    while seen:
        row_curr, col_curr = seen.pop()
        lst2 = [(row_curr+1, col_curr), (row_curr-1, col_curr), (row_curr, col_curr+1), (row_curr, col_curr-1)]
        for coord in lst2:
            x, y = coord
            if (x % len(lst), y % len(lst[0])) in blockage:
                continue
            else:
                seen2.add((x % len(lst), y % len(lst[0])))
    seen = seen2.copy()
    step += 1

