import sys, csv, hashlib

def main():
    decision = input("""
                        --------Make a decision!--------
                        1. Create an account
                        2. Quit
                        What do you want to do: """)
  
    if decision == "1":
        newAccount()
    elif decision == "2":
        sys.exit()
    else:
        exit()

def newAccount():
    print("--------Account Creation--------")
    username = input("Username: ")
    password = input("Password: ")
    passwordConfirm = input("Confirm password: ")
    
    if (password == passwordConfirm):
        with open('users.csv', mode='a') as user_file:
            file_writer = csv.writer(user_file)
            file_writer.writerow([username, hashPassword(password)])
            main()
        print("--------Account setup completed--------")
    else:
        print("--------Passwords don't match--------")
        sys.exit()
            
def hashPassword(password):
    hash_object = hashlib.sha512(str.encode(password))
    return (hash_object.hexdigest())
    

main()