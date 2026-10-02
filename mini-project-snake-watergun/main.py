import random


def game_win(user, computer):
    if user==computer:
        return None

    if user=="s" and computer=="w":
        return True
    if user=="w" and computer=="s":
            return True

    if user=="w" and computer=="g":
            return True
    if user=="g" and computer=="w":
            return True

    if user=="g" and computer=="s":
            return True
    if user=="s" and computer=="g":
            return True

    

rand_no = random.randint(1,3)

print("computer's turn: snake(s) , water(w),gun(g)")

if rand_no == 1:
    computer ="s"
elif rand_no == 2:
    computer ="w" 
else:
    computer ="g"

user = input("your turn: snake(s) , water(w),gun(g)\n"  ).lower()

result = game_win(user, computer)
print(f"\n you choose: {user}")
print(f"\n computer choose: {computer}")

if result is None:
      print("you Draw")
elif(result):
    print("you win")
else:
    print("you lose")