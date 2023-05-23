import string
import random

char = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would your password be: "))
    
    random.shuffle(char)
    
    password = []
    
    for x in range(password_length):
        password.append(random.choice(char))
        
    random.shuffle(password)
    
    password = "".join(password)
    
    print(password)
    
option = input("Do you want to generate a pasword? (Yes/No): ")

if option == "Yes" or option == "yes":
    generate_password()
    print("")
    
elif option =="No" or option == "no":
    print("Program ended")
    quit()
    
else:
    print("Invalid input")
    quit()
