import sys
x = input("enter a user name : ")
y = input("enter a password : ")


cars = ["bmw 1" , "bmw 2" , "bmw 3" , "bmw 4" , "bmw 5" , "ford 1", "ford 2" , "ford 3" , "ford 4" , "ford 5"]
username = ("admin")
password = ("admin 123")


    
    
  
   
if x == username and y == password:
    print(cars)
        
def resign():        
    if x !=username and y != password:
        print("wrong user name and password")
        s = input("enter a new user name : ")
        d = input("enter a new password : ")
        username = s
        password = d
w = input("enter your action (add , remove) : ")
def add ():
    if w == "add":
        v = input("enter a car : ")
        cars.append(v)
        print(cars)
def remove():
    if w == "remove":
        c = input("enter a car : ")
        cars.remove(c) 
        print(cars)
t = input("do you want to make anthor function : ")
while True:
    if t == "yes":
        print("add , remove , resign , sign")
        p = input("enter your function : ")
        if p == "add":
            add()
        elif p == "remove":
            remove()
        elif p == "resign":
            resign()
        elif p == "sign":
            x = input("enter a user name : ")
            y = input("enter a password : ")

        elif t == "no":
            sys.exit()
resign()
add ()
remove()  