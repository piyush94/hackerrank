def check_list(temp):
    for x in temp:
        if x != 0:
            return False
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        m1 = list(map(int, input().split()))
        m2 = list(map(int, input().split()))
        m3 = [x - y for x, y in zip(m1, m2)]
        if check_list(m3):
            print("Yes")
        else:
            print("No")
