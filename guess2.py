from ast import If
import random
secret=random.randint(1,100)
guess=0
tries=0
print("Gues a number between 1 and 100")

while guess !=secret and tries <6:
     guess =int(input("Guess a number:"))
    
     if guess<secret:
         if guess<(secret-10):
            print("Go much higher")  
         else:
            print("Go higher")            
     elif guess >secret:
         if guess>(secret-10):
            print("Go much lower")
         else:
            ("To low")
                
     tries =tries +1 
if guess==secret:
    print("yes, that's the number.")
else:
    print("nope, try again")
