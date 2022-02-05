import random
secret=random.randint(1,100)
guess=0
tries=0
print("Gues a number between 1 and 100")

while guess !=secret and tries <6:
     guess =int(input("Guess a number:"))
     if guess<secret:
            print("too low")
     elif guess >secret:
            print("Too high")

     tries =tries +1 
if guess==secret:
    print("yes, that's the number.")
else:
    print("nope, try again")
