a = int(input("enter a number of Qualified : "))
k = int(input("enter a candidates' scores : "))
s = []
for i in range(a):
    p = int(input("enter Qualified candidates' scores : "))

    if p <= k:
        s.append(p)
print(s)

