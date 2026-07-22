x = int (input("enter a number of soliders : "))
r = []
for y in range(x):
    f = int(input("Enter soldier tall : "))
    r.append(f)
taller = max(r)
shorter = min(r)
taller == r[0]
shorter == r[-1]

steps = taller + (x - 1 - shorter)
print(steps)