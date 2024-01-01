with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])

lst2 = []
for i in range(len(lst)):
    b = []
    x,y = lst[i].split(' ')
    y = y.split(",")
    for num in y:
        if num != ",":
            b.append(int(num))
    lst2.append([x,b])

lst = lst2.copy()
# print(lst)
def naive_method(lst_element):

    def lst_making(s):
        lst = []
        temp = 0
        for i in range(len(s)):
            if s[i] == "#":
                temp += 1
            else:
                if temp:
                    lst.append(temp)
                temp = 0
        if temp:
            lst.append(temp)
        return lst

    def recur(i, lst):
        if i < len(lst):
            temp = lst.copy()
            temp2 = lst.copy()
            if temp[i] == "?":
                temp[i] = "."
                recur(i+1, temp)
                temp2[i] = "#"
                recur(i+1, temp2)
            else:
                recur(i+1, lst)
            ret.append(temp)
            ret.append(temp2)
            ret.append(lst)



    # ret = []
    # recur(0, list(".#??###?????#??"))
    # temp = 0
    # seen = []
    # for r in ret:
    #     if r in seen:
    #         continue
    #     else:
    #         seen.append(r)
    #         if "?" not in r:
    #             print("".join(r), lst_making(r))
    #             if lst_making(r) == [1,11]:
    #                 temp += 1
    # print(temp)
            
    # final = 0
    # for i in range(len(lst)):
    #     seen = set()
    #     temp = 0
    #     x, num_lst = list(lst[i][0]), lst[i][1]
    #     ret = []
    #     recur(0, x)
    #     for r in ret:
    #         if tuple(r) in seen:
    #             continue
    #         else:
    #             seen.add(tuple(r))
    #             if "?" not in r:
    #                 n = lst_making(r)
    #                 if n == num_lst:
    #                     temp += 1
    #     final += temp

# final = []
    seen = set()
    temp = 0
    x, num_lst = list(lst_element[0]), lst_element[1] 
    ret = []
    recur(0, x)
    for r in ret:
        if tuple(r) in seen:
            continue
        else:
            seen.add(tuple(r))
            if "?" not in r:
                n = lst_making(r)
                if n == num_lst:
                    temp += 1
    final.append(temp)

# final2 = []
    seen = set()
    temp = 0
    x, num_lst = list(lst_element[0]) + ["?"] + list(lst_element[0]), lst_element[1]  * 2
    ret = []
    recur(0, x)
    for r in ret:
        if tuple(r) in seen:
            continue
        else:
            seen.add(tuple(r))
            if "?" not in r:
                n = lst_making(r)
                if n == num_lst:
                    temp += 1
    final2.append(temp)
    print("naive method")
# print(final)
# print(final2)

# res = 0
# for i in range(len(final)):
#     multiplier = final2[i] / final[i]
#     res += final[i] * multiplier ** 4
# print(res)


#PART A DOT METHOD
def dot_method(lst_element):

    def recur(ret):
        if ret[0] == -1 or tuple(ret) in seen:
            return
        else:
            seen.add(tuple(ret))
            ret[0] -= 1
            for i in range(1, len(ret)):
                temp = ret.copy()
                temp[i] += 1
                recur(temp)
                temp[i] -= 1




    # ret = []
    st, number_lst = lst_element
    number_of_dots = len(st) - sum(number_lst)
    places_for_dots = [0] * (len(number_lst) + 1)
    places_for_dots[0] = number_of_dots
    seen = set()
    recur(places_for_dots)
    seen2 = set()
    for tup in seen:
        for j in range(1, len(tup)-1):
            if tup[j] == 0:
                seen2.add(tup)
    seen3 = set()
    for tup in seen:
        if tup in seen2:
            continue
        else:
            seen3.add(tup)

    temp = 0
    for tup in seen3:
        s = ""
        i = 0
        while i < len(number_lst):
            s += "." * tup[i]
            s += "#" * number_lst[i]
            i += 1
        s += "." * tup[i]

        #comparing s with base string
        mismatch = False
        for i in range(len(s)):
            if st[i] == "?":
                continue
            elif st[i] != s[i]:
                mismatch = True
                break
        if not mismatch:
            temp += 1
    final.append(temp)





    def recur(ret):
        if ret[0] == -1 or tuple(ret) in seen:
            return
        else:
            seen.add(tuple(ret))
            ret[0] -= 1
            for i in range(1, len(ret)):
                temp = ret.copy()
                temp[i] += 1
                recur(temp)
                temp[i] -= 1




    # ret2 = []
    st, number_lst = lst_element
    st, number_lst = st + "?" + st, number_lst * 2
    print(st, number_lst)
    number_of_dots = len(st) - sum(number_lst)
    places_for_dots = [0] * (len(number_lst) + 1)
    places_for_dots[0] = number_of_dots
    seen = set()
    recur(places_for_dots)
    seen2 = set()
    for tup in seen:
        for j in range(1, len(tup)-1):
            if tup[j] == 0:
                seen2.add(tup)
    seen3 = set()
    for tup in seen:
        if tup in seen2:
            continue
        else:
            seen3.add(tup)

    temp = 0
    h = 0
    for tup in seen3:
        print(h, len(seen3))
        s = ""
        i = 0
        while i < len(number_lst):
            s += "." * tup[i]
            s += "#" * number_lst[i]
            i += 1
        s += "." * tup[i]

        #comparing s with base string
        mismatch = False
        for i in range(len(s)):
            if st[i] == "?":
                continue
            elif st[i] != s[i]:
                mismatch = True
                break
        if not mismatch:
            temp += 1
        h += 1
    final2.append(temp)
    print("dot Method")

    # print(ret)
    # print(ret2)

    # res = 0
    # for i in range(len(ret)):
    #     multiplier = ret2[i] / ret[i]
    #     res += ret[i] * multiplier ** 4
    # print(res)
        

final = []
final2 = []

for i in range(len(lst)):
    print(i)
    number_of_questions, number_of_dots = lst[i][0].count("?"), len(lst[i][0]) - sum(lst[i][1])
    if number_of_dots <= number_of_questions:
        dot_method(lst[i])
    else:
        naive_method(lst[i])
print(final, final2)

res = 0
for i in range(len(final)):
    multiplier = final2[i] / final[i]
    res += final[i] * multiplier ** 4
print(res)
    