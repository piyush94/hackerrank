# https://www.hackerrank.com/challenges/even-odd-query/problem

n = int(input())
a = list(map(int, input().split()))
q = int(input())

def check(x):
    if (x + 1) < n:
        if a[x + 1] == 0:
            return True
    return False


for i in range(q):
    x, y = map(int, input().split())
    x = x - 1
    result = ""
    if x > y:
        result = "Odd"
    elif check(x) and (y - x) != 1:
        result = "Odd"
    elif a[x] % 10 in [0, 2, 4, 6, 8]:
        result = "Even"
    elif a[x] % 10 in [1, 3, 5, 7, 9]:
        result = "Odd"
    print(result)
