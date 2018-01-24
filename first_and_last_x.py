if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        input_list = list(map(int, input().split()))
        x = int(input())
        try:
            print(input_list.index(x), end=' ')
            input_list.reverse()
            print(n - input_list.index(x) - 1, end='\n')
        except ValueError as ex:
            print('-1')
        t -= 1
