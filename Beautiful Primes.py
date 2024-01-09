MOD = 1000000007

def fastmod(a, b):
    ans = 1
    a = a % MOD

    if a == 0:
        return 0

    while b:
        if b & 1:
            ans = (ans * a) % MOD
        b = b >> 1
        a = (a * a) % MOD

    return ans % MOD

def fermat(a):
    return fastmod(a, MOD - 2) % MOD
t = int(input())
for _ in range(t):
    n=int(input())
    primes = list(map(int, input().split()))
    powers = list(map(int, input().split()))

    ans = 1
    
    
    for i in range(n):
        ans = (ans * ((primes[i] * (fastmod(primes[i], powers[i]) - 1) % MOD) * fermat(primes[i] - 1) % MOD)) % MOD

    print(ans)
