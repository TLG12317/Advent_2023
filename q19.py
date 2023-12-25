from operator import index
import weakref


with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])

# wrk_list = []
# dct2 = {}
# for condition in lst:
#     s = ""
#     lst2 = []
#     for element in condition:
#         if element in ("{", "}", ","):
#             lst2.append(s)
#             s = ""
#         else:
#             s += element
    
#     if lst2 == []:
#         continue
#     elif lst2[0] != "":
#         ins = lst2[0]
#         dct = []
#         for i in range(1, len(lst2)-1):
#             condition2, result = lst2[i].split(":")
#             dct.append((condition2, result))
#         dct.append(("last", lst2[-1]))
#         dct2[ins] = dct
#     else:       
#         s = ""
#         wrk = []
#         for j in range(1, len(condition)-1):
#             if condition[j] == ",":
#                 wrk.append(s)
#                 s = ""
#             else:
#                 s += condition[j]
#         wrk.append(s)
#         wrk_list.append(wrk)

# index_finder = ["x", "m", "a", "s"]
# ret = 0

# for worker in wrk_list:
#     curr_dict = "in" 
#     while curr_dict not in ("A", "R"):
#         for condition, result in dct2[curr_dict]:
#             if "<" in condition:
#                 index = index_finder.index(condition[0])
#                 if int(worker[index][2:]) < int(condition[2:]):
#                     curr_dict = result
#                     break
#             elif ">" in condition:
#                 index = index_finder.index(condition[0])
#                 if int(worker[index][2:]) > int(condition[2:]):
#                     curr_dict = result
#                     break  
#             else:
#                 curr_dict = result
#     temp = 0
#     if curr_dict == "A":
#         for w in worker:
#             temp += int(w[2:])
#     ret += temp
    
# print(ret)
            



dct2 = {}
for condition in lst:
    s = ""
    lst2 = []
    for element in condition:
        if element in ("{", "}", ","):
            lst2.append(s)
            s = ""
        else:
            s += element
    
    if lst2 == []:
        continue
    elif lst2[0] != "":
        ins = lst2[0]
        dct = []
        for i in range(1, len(lst2)-1):
            condition2, result = lst2[i].split(":")
            dct.append((condition2, result))
        dct.append(("last", lst2[-1]))
        dct2[ins] = dct

index_finder = ["x","m","a","s"]
stack = [("in", [[1,4000], [1,4000], [1,4000], [1,4000]])]
final_lst = []


while stack:
    curr_dict, test = stack.pop()
    if curr_dict == "R":
        continue
    elif curr_dict == "A":
        final_lst.append(test)
    else:
        for condition, result in dct2[curr_dict]:
            print(result)
            test2 = test.copy()
            if condition[1] == ">":
                index = index_finder.index(condition[0])
                if test2[index][0] > int(condition[2:]):
                    continue
                else:
                    test2[index][0] = int(condition[2:]) + 1
                    stack.append((result, test2))

            elif condition[1] == "<":
                index = index_finder.index(condition[0])
                if test2[index][1] < int(condition[2:]):
                    continue
                else:
                    test2[index][1] = int(condition[2:]) - 1
                    stack.append((result, test2))
            else:
                stack.append((result, test2))
            
print(final_lst)