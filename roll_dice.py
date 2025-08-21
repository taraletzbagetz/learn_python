import random as rnd

roll = rnd.randint(1,6)

guess = int(input("From 1-6 Take a guess..."))



if guess == roll:
    print("you are right the computer rolled: " + str(roll))
else:
    print("you are wrong the computer rolled: " + str(roll))