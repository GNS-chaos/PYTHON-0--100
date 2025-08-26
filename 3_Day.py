print("welcome to th rollercoaster")
height=int(input("your height:? \n"))

if height>=120:
    print("come on!!")
else:
    print("aw schade")

#modulo=%, shows the remainder

number=int(input("whats your number? \n"))

if number%2==1:
    print("you picked an odd number.")
else:
    print("you picked an even number")

#python pizza
print("welcome to the pizza deliveries!")
size= input("s, m, l ")
pepperoni=input("y or n: ")
ext=input("y or n: ")

bill=0

if size=="s":
    bill+=15
    if pepperoni=="y":
        bill+=2

elif size=="m":
    bill+=20
    if pepperoni=="y":
        bill+=3
else:
    bill+=20

if ext=="y":
        bill+=1

print(f"your bill is: {bill}")

#treasure island

print("welcome to the treasure island")
first=input("your mission is to find the treasure. you are at a cross road. R or L: ").lower()

if first=="l":
    sec=input("swim or wait? ").lower()
    if sec=="wait":
        tri=input("which door? r, b, y ")
        if tri=="y":
            print("you WONN!")
        else:
            print("gg.")

    if sec=="swim":
        print("gg:(")
else:
    print("try again later")
