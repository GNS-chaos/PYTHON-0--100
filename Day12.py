#scope


enemies=1

def increas_enemies():
    enemies=2
    print(f"enemies inside function: {enemies}")

increas_enemies()

print(f"enemies outside function: {enemies}")

#local scope
def drink_potion():
    potion_strenght=2
    print(potion_strenght)
drink_potion()
#print(position_strenght)

#when you create a varieble in a fuction, that is defined only in tht function
#you can use it when youre inside that funciton because it has local scope

#global scope: top levelda açıklayınca kodun her yerinde tanımlı oluyor.
#there is no block scope in python

import math

def is_prime(num):
    dividers=[]
    square_root=round(math.sqrt(num))
    if num == 2:
        return True
    if num == 1:
        return False
    for i in range(2, square_root):
        if i!=0:
            if num%i==0:
                dividers.append(i)
    if dividers==[]:
        return True
    else:
        return False
            
print(is_prime(74))
print(is_prime(2))

#avoid modifying global scope

"""print başlık
generate a random num between 0-100
choose diff
print açklama
take the guess
num-guess is pos, print too low
if neg,print too high

her tahmn de hakkı sçilen dife göre düşür.
if bilemezse oynu bititr, tekrar sor ister misin diye
if bilir say tebirks ve ak again
ve her tahminde kaç hakkı kaldığını göster
"""
import random

def play_number_guessing():
    print("Welcome to the Number Guessing Game!")
    number = random.randint(1, 100)
    difficulty = input("I'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        attempt = 10
    elif difficulty == "hard":
        attempt = 5
    else:
        print("Invalid input. Defaulting to 'hard'.")
        attempt = 5

    while attempt > 0:
        print(f"\nYou have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == number:
            print(f"You got it! The number was {number}.")
            break
        elif guess < number:
            print("Too low.")
        else:
            print("Too high.")
        attempt -= 1

    if attempt == 0 and guess != number:
        print(f"\nYou've run out of guesses. The number was {number}.")
    print("Game over!")

# 🔁 TEKRAR OYNAMA DÖNGÜSÜ:
while True:
    play_number_guessing()
    tekrar = input("\nTekrar oynayalım mı? (evet/hayır): ").lower()
    if tekrar != "evet":
        print("Görüşmek üzere!")
        break
    print("\n" * 2)  # biraz boşluk bırakalım
