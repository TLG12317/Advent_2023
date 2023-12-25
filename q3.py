with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1] + ".")
        else:
            lst.append(x[i] + ".")

y = set(('1','2','3','4','5','6','7','8','9','0'))

ret = 0
for row in range(len(lst)):
    for col in range(len(lst[row])):
        if lst[row][col] == "*":
            numbers = set()
            for a in range(-1,2):
                for b in range(-1,2):
                    if lst[row+a][col+b] in y:
                        numbers.add((row+a,col+b))
            targets = set()
            while numbers:
                target = []
                row1,col1 = numbers.pop()    
                target.append(col1)
                s = lst[row1][col1]
                left = col1 - 1
                right = col1+1 
                while left >= 0 and lst[row1][left] in y:
                    s = lst[row1][left] + s
                    target.append(left)
                    left -= 1
                while right < len(lst[0]) and lst[row1][right] in y:
                    s = s + lst[row1][right]
                    target.append(right)
                    right += 1
                target.sort()
                target = tuple(target)
                print(target, s)
                targets.add((target, s))
            print(targets, len(targets))
            if len(targets) == 2:
                temp = 1
                for target in targets:
                    temp *= int(target[1]) 
                ret += temp
print(ret)