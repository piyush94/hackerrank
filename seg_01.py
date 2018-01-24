if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        input_list = list(map(int, input().split()))
        for j in range(len(input_list)):
            if input_list[j] == 0:
                input_list.pop(j)
                input_list.insert(0, 0)
        print(*input_list)
