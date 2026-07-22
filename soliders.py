x = int (input("enter a number of soliders : "))
r = []
for e in range(x):
    g = int(input("enter a tall of solider : "))
    r.append(g)
r.sort(reverse= True)
print(r)