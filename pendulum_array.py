if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        m1 = list(map(int, input().split()))
        m2 = []
        m2.append(min(m1))
        minnum = min(m1)
        m1.remove(minnum)
        while len(m1) > 0:
            minnum = min(m1)
            m2.append(minnum)
            m1.remove(minnum)
            if len(m1) == 0:
                break
            minnum = min(m1)
            m2.insert(0, minnum)
            m1.remove(minnum)
        print(*m2)
