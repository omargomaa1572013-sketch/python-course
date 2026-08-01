x = int(input("enter a number of magnets: "))
y = input("enter information of magnet 1: ")

counter = 1
counter1 = 1
while counter < x:
    a = input("enter information of magnet: ")
    if y[1] != a[0]:
        counter1 += 1
    y = a
    counter += 1
print(f"counter1 = {counter1}")


