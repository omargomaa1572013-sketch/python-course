n = int(input("Enter number of soldiers: "))

a = []

for i in range(n):
    h = int(input("Enter soldier height: "))
    a.append(h)

# أكبر طول
mx = max(a)

# أصغر طول
mn = min(a)

# أول مكان لأكبر طول
for i in range(n):
    if a[i] == mx:
        max_pos = i
        break

# آخر مكان لأصغر طول
for i in range(n - 1, -1, -1):
    if a[i] == mn:
        min_pos = i
        break

moves = max_pos + (n - 1 - min_pos)

# إذا مر أكبر جندي أمام أصغر جندي
if max_pos > min_pos:
    moves -= 1

print(moves)