n = int(input("enter a number of coins : "))
w = []
for i in range(n):
    g = int(input("enter a coin :"))
    w.append(g)
    w.sort(reverse = True)
    d = sum(w)
    