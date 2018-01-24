if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        m1 = list(map(int, input().split()))
        m2 = list(map(int, input().split()))
        m3 = [x + y for x, y in zip(m1, m2)]
        print(*m3)
