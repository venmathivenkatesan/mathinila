n=int(input())
m=list(map(int,input().split()))
a=m.index(min(m))
b=m.index(max(m))
print(a+1,b+1)
