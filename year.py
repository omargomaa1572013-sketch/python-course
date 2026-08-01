x = int(input("enter a year: "))
while True:
    x +=1
    d = str(x)
    if d[0] != d[1] and d[0] != d[2] and d[0] != d[3] and d[1] != d[2] and d[1] != d[3] and d[2] != d[3]:
            print(d)
            break