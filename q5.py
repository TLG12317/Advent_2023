with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])



def list_splitter(lst, m):
    #takes in lst of seeds, and map
    #returns (original_lst, altered list)

    temp1 = [] #back to old
    temp2 = [] # new
    if lst[0] >= m[0] + m[2]:
        temp1.append(lst)
    elif m[0] <= lst[0] <= m[0] + m[2] - 1:
        if  lst[0] + lst[1] - 1 >= m[0] + m[2]:
            r = lst[0] + lst[1] - m[0] - m[2]
            new_lst1, new_lst2 = [lst[0] - (m[0] - m[1]), lst[1] - r], [m[0] + m[2], r]
            temp1.append(new_lst1)
            temp2.append(new_lst2)
            #new_lst1 goes back to lst, new_lst2 goes to new temp
        else:   
            new_lst = [lst[0] - (m[0] - m[1]), lst[1]]
            temp2.append(new_lst)
            #goes to temp
    else:
        if lst[0] + lst[1] - 1 < m[0]:
            temp1.append(lst)
        elif m[0] + m[2] - 1 >= lst[0] + lst[1] - 1 >= m[0]:
            r = lst[0] + lst[1] - m[0]
            new_lst1, new_lst2 = [lst[0],lst[1]-r], [m[0]- (m[0]-m[1]),r]
            temp1.append(new_lst1)
            temp2.append(new_lst2)
            #new_lst1 goes back to lst, new_lst2 goes to new temp
        else:
            x, y = m[0] - lst[0], lst[0] + lst[1] - m[0]-m[2]
            new_lst1 = [lst[0], x]
            new_lst2 = [m[1],lst[1] - x - y]
            new_lst3 = [m[0] + m[2], y]
            temp1.append(new_lst1)
            temp1.append(new_lst3)
            temp2.append(new_lst2)
    return temp1, temp2


# lst = [[79,14], [55,13]]
# m = [[52, 50, 48], [50, 98, 2]] #swtich m[0] and m[1]
# #if no more mapping, transfer all lst to ret


def check(xi, ma):
    ret = []
    for i in range(len(ma)):
        temp = []
        ma[i] = [ma[i][1], ma[i][0], ma[i][2]]
        while xi:
            x = xi.pop()
            lst1, lst2 = list_splitter(x, ma[i])
            for a in lst1:
                temp.append(a)
            for b in lst2:
                ret.append(b)
        xi = temp.copy()
    ret.extend(temp)
    return ret

seeds2 = [768975, 36881621, 56868281, 55386784, 1828225758, 1084205557, 2956956868, 127170752, 1117192172, 332560644, 357791695, 129980646, 819363529, 9145257, 993170544, 70644734, 3213715789, 312116873, 3107544690, 59359615]
seeds = []

for i in range(1, len(seeds2), 2):
    seeds.append([seeds2[i-1], seeds2[i]])

m = []
for i in range(3, len(lst)):
    hi = lst[i].split(" ")
    if m and (lst[i] == "" or ":" in lst[i]):
        seeds = check(seeds, m)
        m = []
    elif len(hi) == 3:
        m.append([int(hi[0]), int(hi[1]), int(hi[2])])

seeds = check(seeds, m)
# print(seeds)

ret = float('inf')
for j in range(len(seeds)):
    ret = min(ret, seeds[j][0])
print(ret)