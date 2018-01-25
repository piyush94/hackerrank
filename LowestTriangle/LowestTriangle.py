# https://www.hackerrank.com/challenges/lowest-triangle/problem

import math

b, a = map(int, input().split())

h = (a * 2) / b
print(math.ceil(h))
