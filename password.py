import re

def passwordChecker(passw):
    passOK = 0
    while True:   
        if (len(passw)<8): 
            passOK = -1
            break
        elif not re.search("[a-z]+[A-Z]", passw): 
            passOK = -1
            break
        elif not re.search("[0-9]", passw): 
            passOK = -1
            break
        else: 
            passOK = 0
            return True
    
        if alright ==-1:
            return False

def main():
    password = input("type your password: ")
    if(passwordChecker(password)):
        print("good password, you're ok to continue")
    else:
        print("bad password, try again putting at least one uppercase, one number and more than 8 digits")
        
main()