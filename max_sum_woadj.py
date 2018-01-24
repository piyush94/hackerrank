# code
def maxSum(arr, size):
    incl = 0
    excl = 0
    for i in range(0, size):
        new_excl = (incl if incl > excl else excl)
        incl = excl + arr[i]
        excl = new_excl
        print(new_excl, incl, excl)
    print(incl if incl > excl else excl)


t = int(input())
for i in range(0, t):
    size = int(input())
    arr = list(map(int, input().split()))
    maxSum(arr, size)
