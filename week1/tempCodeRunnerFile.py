import random
number=random.randint(1,100)
attempts=0
while True:
    guess=int(input(("Guess the number : ")))
    if guess==number:
        print("Your guess is correct")
        break
    elif guess<number:
        print("Too low")
        attempts+=1
    else:
        print("Too high")
        attempts+=1
    if attempts>10:
        print("Your chance is over")
        break