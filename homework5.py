def feeling():
    x = int(input("enter a feeling number: "))

    if x == 1:
        print("i hate it")
    elif x == 2:
        print("I hate that I love it")
    elif x == 3:
        print("I hate that I love that I hate it")

    while True:
        x = int(input("enter a feeling number: "))
        if x in {1, 2, 3}:
            break
    else:
        x = int(input("Invalid feeling number. Please enter a valid feeling number (1, 2, or 3): "))
feeling()    