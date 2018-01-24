def permute(a, l, r):
    if l == r:
        results.append(''.join(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]


if __name__ == '__main__':
    t = int(input())
    while t:
        input_str = input()
        results = []
        permute(list(input_str), 0, len(input_str) - 1)
        results.sort()
        print(*results)
        t -= 1
