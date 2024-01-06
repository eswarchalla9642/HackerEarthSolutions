import math

t = int(input())
for _ in range(t):
    n = int(input())
    i = 1
    while i <= math.isqrt(n):
        i *= 2
    if n // i >= i // 2:
        ans = n - n // i
    else:
        ans = (n - (i // 2)) + 1
    print(ans)
