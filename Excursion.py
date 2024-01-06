for _ in range(int(input())):
    n,m,k = map(int, input().split())
    c=0
    if n+m>0:
        while(n>0):
            c=c+1
            n=n-k
        while(m>0):
            c=c+1
            m=m-k
        print(c)
    else:
        print(0)
