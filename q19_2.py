with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])



dct = {}

for i in range(len(lst)):
    condition, x = lst[i].split("{")
    check = x.split(",")
    dct[condition] = []
    for j in range(len(check)-1):
        condition2, next_location = check[j].split(":")
        dct[condition].append([condition2, next_location])
    final_location = check[-1][:-1]
    dct[condition].append(["x>-1", final_location])

temp = [["in"] + [[[1,4000] for _ in range(4)]]]

indices = ["x", "m", "a", "s"]
ret = []

while temp:
    initial_location, xmas_lst = temp.pop()
    if initial_location == "R":
        continue
    elif initial_location == "A":
        ret.append(xmas_lst)
    else:
        for i in range(len(dct[initial_location])):
            gah = []
            for j in range(len(xmas_lst)):
                gah.append(xmas_lst[j].copy())
            condition, next_location = dct[initial_location][i]
            print(condition, next_location)
            ind = indices.index(condition[0])
            if condition[1] == ">":
                gah[ind][0] = max(int(condition[2:])+1, gah[ind][0])
                xmas_lst[ind][1] = min(int(condition[2:]), xmas_lst[ind][1]) 
            else:
                gah[ind][1] = min(int(condition[2:])-1, gah[ind][1])
                xmas_lst[ind][0] = max(int(condition[2:]), xmas_lst[ind][0]) 
            temp.append([next_location, gah])

res = 0
for i in range(len(ret)):
    temp = 1
    for j in range(len(ret[i])):
        temp *= (ret[i][j][1] - ret[i][j][0] + 1) 
    res += temp
print(res)