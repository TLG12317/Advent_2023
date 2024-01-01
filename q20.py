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
    if lst2[i][0] == "broadcaster ":
        lst2[i][0] = ".broadcaster "
    dct[lst2[i][0][:-1]] = lst2[i][1]

status = {}
status["output"] = False
for element in dct:
    if element != ".broadcaster":
        if element[0] == "%":
            status[element[1:]] = False
status["broadcaster"] = False

conjunction_module_inputs = defaultdict(lambda:[])

for key, values in dct.items():
    for value in values:
        if "&"+value in dct:
            conjunction_module_inputs[value].append([key[1:], False])


def button():
    high_pulse = low_pulse = 0
    queue = deque([".broadcaster"])
    while queue:
        x = queue.popleft()
        if x == "&output":
            continue
        elif "&" == x[0]:
            flag = True
            for element, pulse in conjunction_module_inputs[x[1:]]:
                flag = flag and pulse
            if flag == True:
                low_pulse += 1
                for element in dct[x]:
                    if status[element] == False:
                        status[element] = True
                    else:
                        status[element] = False
                    if "%"+element in dct:
                        queue.append("%"+element)
                    else:
                        queue.append("&"+element)
            else:
                high_pulse += 1
                for element in dct[x]:
                    if "&"+element in dct:
                        queue.append("&"+element)
        else:
            for output in dct[x]:
                if "%" + output in dct:
                    if status[x[1:]] == False:
                        low_pulse += 1
                        if status[output] == True:
                            status[output] = False
                        else:
                            status[output] = True
                        queue.append("%"+output)
                    else:
                        high_pulse += 1
                elif "&" + output in dct:
                    for q in range(len(conjunction_module_inputs[output])):
                        if conjunction_module_inputs[output][q][0] == x[1:]:
                            if status[x[1:]] == True:
                                high_pulse += 1
                            else:
                                low_pulse += 1
                            conjunction_module_inputs[output][q][1] = status[x[1:]]
                            queue.append("&"+output)
                            break
    return high_pulse, low_pulse

high_pulse = low_pulse = 0

n = 0
while n < 1000:
    x,y = button()
    high_pulse += x
    low_pulse += y+1
    n += 1

print(high_pulse, low_pulse)
print(high_pulse*low_pulse)