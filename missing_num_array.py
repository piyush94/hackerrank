if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        m1 = list(map(int, input().split()))
        ap_sum = (n * (n + 1)) / 2
        print(int(ap_sum) - sum(m1))
