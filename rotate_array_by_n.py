# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n, d = map(int, input().split())
#         input_list = list(map(int, input().split()))
#         while d:
#             for j in reversed(range(n - 1)):
#                 input_list[0], input_list[j + 1] = input_list[j + 1], input_list[0]
#             d -= 1
#         print(*input_list)

# -------------------------OR-------------------------------------------
if __name__ == '__main__':
    t = int(input())
    while t:
        n, d = map(int, input().split())
        input_list = list(map(int, input().split()))
        output_list = []
        for i in range(d, n):
            output_list.append(input_list[i])
        for i in range(d):
            output_list.append(input_list[i])
        print(*output_list)
        t -= 1
