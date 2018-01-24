import re

t = int(input())

for i in range(0, t):
    size = int(input())
    totalSize = size * size
    m1 = list(map(int, re.sub(' +', ' ', input()).split(' ')))
    print(m1)
    m3 = [0] * totalSize
    temp = 0
    for i in range(0, totalSize):
        if temp > totalSize - 1:
            temp = temp - totalSize + 1
        m3[temp] = m1[i]
        temp += size
    print(' '.join([str(x) for x in m3]))
