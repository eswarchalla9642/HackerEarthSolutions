# Monk and Nice Strings
n = int(input())
a =[]
for i in range(n):
    a.append(input())
for i in range(n):
    c=0
    for j in range(i):
        if a[j]<a[i]:
            c+=1
    print(c)
