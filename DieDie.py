M = 10**9 + 7

def binExp(a, b):
    ans = 1
    while b > 0:
        if b & 1:
            ans = (ans * a) % M
        a = (a * a) % M
        b >>= 1
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    p = 2
    q = binExp(2, n)
    result = (p * binExp(q, M - 2)) % M
    print(result)
