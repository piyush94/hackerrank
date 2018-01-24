def SieveOfEratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:

        # If prime[p] is not changed, then it is a prime
        if prime[p]:

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    return prime


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        prime_n = SieveOfEratosthenes(n)
        for j in range(2, n):
            if prime_n[j] and prime_n[n - j]:
                print(j, n - j)
                break
