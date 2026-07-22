a = int(input("enter a value of number : "))
q = int(input("enter a number of lines : "))
for t in range(q):
    x = input("enter a sign :" )
    if x in ["--x" , "x--",]:
        a = a - 1
    if x in ["++x" , "x++"]:
        a = a + 1
print(a)

