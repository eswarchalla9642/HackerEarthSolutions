# Unlucky 13

c = {}
m = 1000000009
def ans(n):
    if n < 50000000:
        if n in c:
            return c[n]
        if n==0:
            c[n]=1
            return c[n]
        if n==1:
            c[n]=10
            return c[n]
        a = ans(n//2)
        b = ans(n//2 - 1)
        if n%2==0:
            c[n] = (a*a-b*b)%m
        else:
            z = ans(n//2+1)
            c[n]=(a*(z-b))%m
        return c[n]
    else:
        if n in c2:
            return c2[n]
        t1 = ans(n//2)
        t2 = ans(n//2-1)
        if n%2==0:
            c2[n] = (t1*t1-t2*t2)%m
        else:
            z1 = ans(n//2+1)
            c2[n]=(t1*(z1-t2))%m
        return c2[n]
N = int(input())
for i in range(N):
    n = int(input())
    c2={}
    print(ans(n))
