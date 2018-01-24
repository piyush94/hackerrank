import time

if __name__ == '__main__':
    start_time = time.time()
    t = int(input())
    for i in range(t):
        n = int(input())
        temp = 1
        for j in range(n):
            print(*range(temp, temp + j + 1))
            temp += j + 1
    print("\n", time.time() - start_time)
