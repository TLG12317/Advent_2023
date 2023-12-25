from urllib.parse import _NetlocResultMixinStr


with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    temp = []
    for i in range(len(x)):
        if len(x[i]) == 1:
            lst.append(temp)
            temp = []
        elif i != len(x)-1:
            temp.append(x[i][:-1])
        else:
            temp.append(x[i])
    lst.append(temp)



def reflection(pattern):
    lst = []
    for i in range(len(pattern)-1):
        left = i
        right = i + 1
        while left >= 0 and right < len(pattern):
            if pattern[left] == pattern[right]:
                left -= 1
                right += 1
            else:
                break
        if left == -1 or right == len(pattern):
            lst.append(i+1)
    return lst
        

for i in range(len(lst)):
    for j in range(len(lst[i])):
        lst[i][j] = list(lst[i][j])

ret = 0
for pattern in lst:
    vertical_pattern = list(map(list, zip(*pattern)))
    left_to_avoid = reflection(vertical_pattern)
    up_to_avoid = reflection(pattern)

    left_to_avoid = left_to_avoid[0] if left_to_avoid else None
    up_to_avoid = up_to_avoid[0] if up_to_avoid else None
    print(left_to_avoid, up_to_avoid)

    for row in range(len(pattern)):
        for col in range(len(pattern[0])):
            if pattern[row][col] == ".":
                pattern[row][col] = "#"
            else:
                pattern[row][col] = "."
            vertical_pattern = list(map(list, zip(*pattern)))
            left = reflection(vertical_pattern)
            up = reflection(pattern)
            for l in left:
                if l and l != left_to_avoid:
                    print(l, row, col)
                    ret += l
            for u in up:
                if u and u != up_to_avoid:
                    print(u, row, col)
                    ret += u*100
            if pattern[row][col] == ".":
                pattern[row][col] = "#"
            else:
                pattern[row][col] = "."
print(ret/2)