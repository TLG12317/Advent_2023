with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])

from collections import deque, defaultdict

lst2 = []
for i in range(len(lst)):
    inn, out = lst[i].split("->")
    out = out.split(", ")
    out[0] = out[0][1:]
    lst2.append([inn,out])
dct = {}

for i in range(len(lst2)):
    dct[lst2[i][0][:-1]] = lst2[i][1]

status = {}
status["output"] = "off"
for element in dct:
    if element[0] == "%":
        status[element[1:]] = "off"

conjunction_module_inputs = defaultdict(lambda:[])
dct["&rx"] = []
for key, values in dct.items():
    for value in values:
        if "&"+value in dct:
            conjunction_module_inputs[value].append([key[1:], "low"])

print(dct)
# print(status, conjunction_module_inputs)

from collections import deque

# def button():
#     queue = deque([["broadcaster", "low", "button", conjunction_module_inputs]])

#     low_pulse = high_pulse = 0


#     while queue:
#         receiver, pulse, sender, c = queue.popleft()
#         # print(sender, pulse, receiver, c)
#         if pulse == "low":
#             low_pulse += 1
#         else:
#             high_pulse += 1


#         if receiver == "broadcaster":
#             for element in dct[receiver]:
#                 queue.append([element, pulse, receiver, c.copy()])
        

#         elif "%" + receiver in dct:
#             if pulse == "high":
#                 continue
#             else:
#                 if status[receiver] == "off":
#                     #sends high
#                     status[receiver] = "on"
#                     for element in dct["%" + receiver]:
#                         queue.append([element, "high", receiver, c.copy()])
#                 else:
#                     #sends low
#                     status[receiver] = "off"
#                     for element in dct["%" + receiver]:
#                         queue.append([element, "low", receiver, c.copy()])


#         elif "&" + receiver in dct:
#             for i in range(len(conjunction_module_inputs[receiver])):
#                 if conjunction_module_inputs[receiver][i][0] == sender: 
#                     conjunction_module_inputs[receiver][i][1] = pulse
#                     break
            
#             flag = "high"
#             for j in range(len(conjunction_module_inputs[receiver])):
#                 if conjunction_module_inputs[receiver][j][1] == "low":
#                     flag = "low"
#                     break


#             if flag == "high":
#                 for element in dct["&" + receiver]: 
#                     queue.append([element,"low",receiver, c.copy()])
#             else:
#                 for element in dct["&" + receiver]: 
#                     queue.append([element,"high",receiver, c.copy()])


#     return low_pulse, high_pulse


def button():
    queue = deque([["broadcaster", "low", "button"]])

    low_pulse = high_pulse = 0
    s = 1
    if conjunction_module_inputs["qz"][0][1] == "low" and s == 2:
        print("hi")
        return False
    s += 1
    # if conjunction_module_inputs["qz"]
    while queue:
        receiver, pulse, sender = queue.popleft()
        if pulse == "low":
            low_pulse += 1
        else:
            high_pulse += 1
        if receiver[1:] == "rx":
            print('d')
        if pulse == "low" and receiver[1:] == "rx":
            return False 
        
        if receiver == "broadcaster":
            for element in dct[receiver]:
                queue.append([element, pulse, receiver])
        

        elif "%" + receiver in dct:
            if pulse == "high":
                continue
            else:
                if status[receiver] == "off":
                    #sends high
                    status[receiver] = "on"
                    for element in dct["%" + receiver]:
                        queue.append([element, "high", receiver])
                else:
                    #sends low
                    status[receiver] = "off"
                    for element in dct["%" + receiver]:
                        queue.append([element, "low", receiver])


        elif "&" + receiver in dct:
            for i in range(len(conjunction_module_inputs[receiver])):
                if conjunction_module_inputs[receiver][i][0] == sender: 
                    conjunction_module_inputs[receiver][i][1] = pulse
                    break
            
            flag = "high"
            for j in range(len(conjunction_module_inputs[receiver])):
                if conjunction_module_inputs[receiver][j][1] == "low":
                    flag = "low"
                    break


            if flag == "high":
                for element in dct["&" + receiver]: 
                    queue.append([element,"low",receiver])
            else:
                for element in dct["&" + receiver]: 
                    queue.append([element,"high",receiver])


    return low_pulse, high_pulse


#part 1
# low_pulse = high_pulse = 0
# n = 1000

# while n:
#     x, y = button()   
#     low_pulse += x
#     high_pulse += y
#     n -= 1
#     print("step")

# print(low_pulse, high_pulse)
# print(low_pulse * high_pulse)


#part 2
# n = 0
# x = True
# while x:
#     x = button()
#     n += 1
#     print(n)
# print(n)


def searching(str):
    n = 0
    lst = [False for _ in conjunction_module_inputs[str]]
    while True:
        #search for the moment all of the conjunction modules are filled 
        button()
        n += 1
        # lst = []
        # for i in range(len(conjunction_module_inputs[str])):
        #     module, val = conjunction_module_inputs[str][i] 
        #     lst.append(val)
        #     print(lst[i], conjunction_module_inputs[str][i][1])
        #     if lst[i] == False and conjunction_module_inputs[str][i][1] == "high":
        #         lst[i] = n
        # print(lst, n)
        # if "low" not in lst:
        #     break
        for i in range(len(conjunction_module_inputs[str])):
            module, val = conjunction_module_inputs[str][i] 
            # print(lst[i], conjunction_module_inputs[str][i][1])
            if lst[i] == False and conjunction_module_inputs[str][i][1] == "high":
                lst[i] = n
        # print(lst, n)
        if False not in lst:
            break

    return lst



# print(conjunction_module_inputs["rx"])


# print(conjunction_module_inputs["rx"])
# print(conjunction_module_inputs["qn"])
# print(conjunction_module_inputs["tt"])
# print(conjunction_module_inputs["mt"])


# print(conjunction_module_inputs["qn"])
# print(conjunction_module_inputs["jx"])
# print(conjunction_module_inputs["zd"])


# print(conjunction_module_inputs["qn"])
# print(conjunction_module_inputs["cq"])
# print(conjunction_module_inputs["kx"])



print(conjunction_module_inputs["qn"])
# print(conjunction_module_inputs["qz"])
# print(conjunction_module_inputs["zq"])


# searches for all of the num_lst of conjunction module connected to flip flop modules
# print(searching("mt"))
# print(searching("zd"))
# print(searching("kx"))
# print(searching("zq"))

def recur(s):
    from math import lcm
    ret = 1 
    for module, val in conjunction_module_inputs[s]:
        if module not in conjunction_module_inputs:
            lst = searching(s)
            temp = 1 
            while True:
                flag = True
                for num in lst:
                    if (temp // num) % 2 == 0:
                        #even
                        flag = False
                        break
                if flag:
                    break
                temp += 1
            ret = lcm(ret, temp)
            print(temp)
            break
        else:
            ret = lcm(ret, recur(module))
    return ret

k = recur('rx')
print(k)

# num_lst = [1024,64,1,512,256,2,4,2048]
# num_lst1 = [1024, 16, 2048, 1, 4, 256, 128, 512, 32]
# num_lst2 = [1, 2048, 64, 256, 512, 2, 1024]
# num_lst3 = [8, 256, 2, 2048, 512, 16, 1024, 64, 1]


# n = 1
# while True:
#     flag = True
#     for num in num_lst:
#         if (n // num) % 2 == 0:
#             #even
#             flag = False
#             break
#     if flag:
#         print(n)
#         break
#     n += 1


# ret = 1
# from math import lcm
# final = [3911, 4021, 3907, 3931]

# for num in final:
#     ret = lcm(ret, num)

# print(ret)





