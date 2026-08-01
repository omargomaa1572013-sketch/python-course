n = int(input("Enter a number of children : "))
m = int(input("Enter a number of puzzles : "))
f = []
t = []
for i in range(m):
    x = int(input("Enter the number of pieces in puzzle : "))
    f.append(x)
for d in range(m):
    f.sort()
    q = f[0] - f[-1]
    t.append(q)
    f.pop(0)
    f.pop(-1)
print(t[n])
