if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        input_list = list(map(int, input().split()))
        for j in range(n):
            input_list[j] += (input_list[input_list[j]]%n)*n
        for j in range(n):
            input_list[j] //= n
        print(*input_list)