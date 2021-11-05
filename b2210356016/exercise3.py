import random

number=random.randint(1,30)   #generate random number in an interval of coder's choice
x=int(input("pick a number between 1 and 30:"))  #get value from user

while x!=number:   #iterate if x does not equal to number
    if x>number:
        x=int(input("decrease your number:"))  #give feedback to user
        continue  #after getting new input start iterating from the beginning

    elif x<number:
        x=int(input("increase your number:"))  #give feedback to user

print("your guess was",x,"the number was",number,"congrats!")
