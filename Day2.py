#print(len(234567))  error

print("hello"[0])
print(type(234))
print(type(True))
print(type(2.3))
print("number of letters in your name: " + str(len(input("name? "))))

print(3*2)
print(type(6/2))
print(5//3)
print(5/3)
print(2**10)

#pemdas

#bmi=kilo/boy**2

weight=float(input("weight(kg)? "))
height=float(input("height? "))
bmi=weight/height**2
print(round(bmi))
print(round(bmi,2))

score=0
score+=1
print(score)
print(f"your score is: {score}")

#tip calculator
print("welcome to the tip calc")
bill=float(input("what was the total bill? \n"))
tip=float(input("how much tip you'd like to give? 10, 12, 15?\n"))
bill+=tip*bill/100
people=int(input("how many people will spilt? \n"))
payment=round(bill/people,2)
print(f"you will each pay {payment}")
