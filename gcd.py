if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        if a % b == 0:
            print(b)
        else:
            gcd = min(a, b)
            while gcd > 0:
                if a % gcd == 0 and b % gcd == 0:
                    break
                else:
                    gcd -= 1;
            print(gcd)
