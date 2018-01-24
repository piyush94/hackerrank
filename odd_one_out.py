if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        m1 = list(map(int, input().split()))
        m2 = []
        for x in m1:
            if x in m2:
                m2.remove(x)
            else:
                m2.append(x)
        print(*m2)
