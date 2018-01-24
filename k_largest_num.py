if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        input_list = list(map(int, input().split()))
        output_list = []
        while k:
            output_list.append(max(input_list))
            input_list.remove(max(input_list))
            k -= 1
        print(*output_list)
