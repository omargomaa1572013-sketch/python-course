s = input("enter your word")

hello = "hello"
i = 0

for x in s:
    if x == hello[i]:
        i += 1

        if i == 5:
            break

if i == 5:
    print("YES")
else:
    print("NO")