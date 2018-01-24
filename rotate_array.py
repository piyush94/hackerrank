if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        input_list = list(map(int, input().split()))
        for j in range(n - 1):
            input_list[0], input_list[j + 1] = input_list[j + 1], input_list[0]
        print(input_list)
