with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])



# print(lst)

# seen = set()
# blockage = set()
# for row in range(len(lst)):
#     for col in range(len(lst[0])):
#         if lst[row][col] == "S":
#             seen.add((row, col))
#         elif lst[row][col] == "#":
#             blockage.add((row,col))

# step = 0

# while step < 64:
#     seen2 = set()
#     while seen:
#         row_curr, col_curr = seen.pop()
#         lst = [(row_curr+1, col_curr), (row_curr-1, col_curr), (row_curr, col_curr+1), (row_curr, col_curr-1)]
#         for coord in lst:
#             if coord in blockage:
#                 continue
#             else:
#                 seen2.add(coord)
#     seen = seen2.copy()
#     step += 1

# print(len(seen))


#part 2
            
#I DID NOT DO THIS GO FUCK YOURSELF
            
matrix = list()
start = tuple()

def fillmap(starting_step,frame,steps):
    global matrix
    global start
    pos = set()
    pos.add(start)

    for i in range(steps):
        print(i, steps)
        npos = set()
        for p in pos:
            x = p[0]
            y = p[1]
            for xm,ym in zip((-1,0,1,0),(0,-1,0,1)):
                if matrix[(y+ym)%len(matrix)][(x+xm)%len(matrix[0])] == '.':
                    npos.add((x+xm,y+ym))				
        pos = npos

        if i%frame == starting_step-1:
            print(len(pos))
            yield len(pos)
    return

def main(input_file,steps):
    global matrix
    global start
    matrix = list()
    start = tuple()
    with open(input_file) as f:
        for y,line in enumerate(f.readlines()):
            matrix.append(list())
            for x,char in enumerate(line.rstrip()):
                if char == 'S':
                    start = (x,y)
                    matrix[y].append('.')
                else:
                    matrix[y].append(char)

    dim = len(matrix)
    a = list()

    for res in fillmap(dim//2,dim,dim*2+dim//2+1):
        a.append(res)
    i = dim
    s = a[1]-a[0] 
    r = a[2]-a[1]
    d = r - s
    res = a[1]

    while i != steps-dim//2:
        i += dim
        res += r
        r += d
    return res

if __name__ == "__main__":
    print(main("hi.txt",26501365))