from ast import Break
import random
print("NUMBER GUEESING GAME")
num=random.randint(1,9)
chances=0
print("guess a number betwwen 1 to 9")
while chances < 5:
    guess=int(input("enter your guess "))
    if guess == num:
        print("CONGRATS! YOU WON") 
        break
    elif guess <num:
        print("your guess was too low")
    else :
        print("your guess was too high")
    chances+=1
if not chances <5 :
    print("you lose!the number is ", num)