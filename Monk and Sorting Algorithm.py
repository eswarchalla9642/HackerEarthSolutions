#Code Monk Sorthing Algorithm
MOD = 1000000007
ll = int

n = int(input())
A = list(map(ll, input().split()))

x = max(A)
I = 1
while x // I:
    A = sorted(A, key=lambda num: (num // I) % 100000)
    
    for num in A:
        print(num, end=" ")
    print("")

    I *= 100000
