x = int(input("enter a number of soliders : "))
r = []
for i in range(x):
    t = int(input("Enter soldier tall : "))
    r.append(t)
r.sort(reverse = True)
print(r)