'''Mini Project in Python - Number Guessing Game using Random Module'''
'''
import random
random_number=random.randint(1,100)
print("Game is Starting...")
while True:
    user_number=int(input("Enter Number:"))
    if(user_number == random_number):
        print("Success, You have gussed correctly")
        break
    elif(user_number > random_number):
        print("Try Again with Small Number")
    else:
        print("Try Again with larger number")
print("***GAME OVER***")

'''
'''Random Password Generator
import random
import string

pass_bucket=(string.ascii_letters + string.digits + string.punctuation)
pass_len=12
password=""
for i in range(pass_len):
    password += random.choice(pass_bucket)

print(password)'''
