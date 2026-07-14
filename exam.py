n = int(input("enter a number ≤ 3: "))
if  n  > 3:
    print("Invalid input. Please enter a number ≤ 3.")
    n = int(input("enter a number ≤ 3: "))

m = int(input("enter a number ≤ 50: "))
if m > 50:
    print("Invalid input. Please enter a number ≤ 50.")
    m = int(input("enter a number ≤ 50: "))
for i in range(n):
    for x in range(m):
        if i == 1 or i %2 == 1:
            print("###")
        else:
            if x == m - 1:
                print("#")
            else:
                print(".")
        i += 1
        if x == m - 1:
            print("#")
x += 1