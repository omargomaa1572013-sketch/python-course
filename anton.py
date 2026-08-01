x = int(input("Enter a number: "))

h = []
counter = 1

for i in range(x):
    g = int(input("Enter a number: "))
    h.append(g)

for f in range(1 , x):
    if h[f] < h[f - 1]:
        break
    else:
        counter += 1

print(counter)
        