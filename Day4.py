#randomization

import random

random_integer=random.randint(1,10)
print(random_integer)

rndm_0to1=random.random()*10
print(rndm_0to1)

random_float=random.uniform(1,10)
print(random_float)

#heads and tails game
ht=random.randint(0,1)
if ht==0:
    print("heads")
else:
    print("tails")

#lists

states=["delaware", "pensilvanya", "bostoncum"]
print(states[1])
print(states[-1])
#print(states[-4]) error xd
states.append("la") #ekleme yapıyor sona
print(states)
states.extend(["la", "chicago"])
print(states)

#banker roulette
import random
friends=["alice", "fred", "penny", "sheldon"]
print(random.choice(friends))

who=random.randint(0,3)
print(friends[who])

#rock paper scissors game
your_move=int(input("0:rock, 1:paper, 2: scissors"))
list=["rock", "paper", "scissors"]
pc_move=random.randint(0,2)
print(f"your move is: {list[your_move]}")
print(f"pc move is: {list[pc_move]}")
if your_move>=3 or your_move<0:
    print("invalid number")
elif your_move==0 and pc_move==2:
    print("you WONN!")
elif your_move==2 and pc_move==0:
    print("you losee!")
elif pc_move > your_move==0:
    print("you lost.")
elif your_move > pc_move==0:
    print("you won.")
elif your_move==pc_move:
    print("draw")

