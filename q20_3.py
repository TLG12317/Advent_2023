with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])

from collections import deque, defaultdict

def initialise():
    #reset the status, dictionary, and conjunctions to default states
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
    dct["&" + output] = []
    for key, values in dct.items():
        for value in values:
            if "&"+value in dct:
                conjunction_module_inputs[value].append([key[1:], "low"])
    return status, dct, conjunction_module_inputs


def button(dct, status, conjunction_module_inputs):

    #Essentially the main function
    #Handles the logic of how modules interact with each other
    #Updates the status of each button (on and off) and the pulses received and sent per button press   

    queue = deque([["broadcaster", "low", "button"]])

    while queue:
        receiver, pulse, sender = queue.popleft()
        if pulse == "low" and receiver[1:] == output:
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



def searching(str):
    #finds the cycle of flip flops such that the conjunction will output ["True", ...., "True"]
    n = 0
    status, dct, conjunction_module_inputs = initialise() #sets the dct, statuses and conjunction modules to default states
    lst = [False for _ in conjunction_module_inputs[str]]
    while True:
        #search for the moment all of the conjunction modules are filled 
        button(dct, status, conjunction_module_inputs)
        n += 1
        for i in range(len(conjunction_module_inputs[str])):
            if lst[i] == False and conjunction_module_inputs[str][i][1] == "high":
                lst[i] = n
        if False not in lst:
            break
    return lst

def recur(s): 
    #Given a conjunction module (&), inputted by a buncha flip flops (%), 
    #Find the cycle number of the flip flop modules
    #finds LCM of the cycle numbers (if all conjunctions connected to rx are True, rx will be True)
    from math import lcm
    ret = 1 
    for module, val in conjunction_module_inputs[s]:
        if module not in conjunction_module_inputs:
            lst = searching(s)
            temp = 1 
            #cycle number finder
            #finds the lowest number that can return a list of ["True", "True", ... ,"True"]
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
            break
        else:
            ret = lcm(ret, recur(module))
    return ret

output = "rx"
dct, status, conjunction_module_inputs = initialise() #sets the dct, statuses and conjunction modules to default states
res = recur(output) #rx is the output module that has to be returned
#recur calls searching which calls button

print(res)