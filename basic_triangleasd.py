int_num = list(map(int,input().split()))
a,s,d = sorted(int_num)
if a**2+s**2==d**2:
    print("yes")
else:
    print("no")
