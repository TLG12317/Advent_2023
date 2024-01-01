import numbers


with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])




# def recur(stri, numbers):
#     res = 0
#     if numbers == []:
#         if "#" in stri:
#             return 0
#         return 1
#     if stri == "":
#         return 0
#     if stri[0] in "?.":
#         res += recur(stri[1:], numbers)
#     if stri[0] in "?#":
#         if len(stri) > numbers[0]: 
#             if "." not in stri[:numbers[0]] and stri[numbers[0]] in ".?":
#                 res += recur(stri[numbers[0]+1:], numbers[1:])
#         elif len(stri) == numbers[0]: 
#             if "." not in stri:
#                 res += recur("", numbers[1:])
#     return res

# ret = 0
# for i in range(len(lst)):
#     stri, numbers = lst[i].split(" ")
#     numbers = numbers.split(",")
#     for j in range(len(numbers)):
#         numbers[j] = int(numbers[j])
#     ret += recur(stri, numbers)
# print(ret)



def recur(stri, numbers):
    res = 0
    if numbers == []:
        if "#" in stri:
            return 0
        return 1
    if stri == "":
        return 0
    if (stri, tuple(numbers)) in dct:
        return dct[(stri, tuple(numbers))]
    if stri[0] in "?.":
        res += recur(stri[1:], numbers)
    if stri[0] in "?#":
        if len(stri) > numbers[0]: 
            if "." not in stri[:numbers[0]] and stri[numbers[0]] in ".?":
                res += recur(stri[numbers[0]+1:], numbers[1:])
        elif len(stri) == numbers[0]: 
            if "." not in stri:
                res += recur("", numbers[1:])
    dct[(stri, tuple(numbers))] = res
    return res

ret = 0
for i in range(len(lst)):
    dct = {}
    stri, numbers = lst[i].split(" ")
    numbers = numbers.split(",")
    for j in range(len(numbers)):
        numbers[j] = int(numbers[j])
    stri2 = (stri + "?") * 4 + stri 
    numbers2 = numbers * 5
    ret += recur(stri2, numbers2)
print(ret)