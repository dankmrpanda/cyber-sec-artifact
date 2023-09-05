import re
import os
import time
def checkPassword():
    os.system('cls')
    suggest = []
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", 
               "(", ")", "_", "-", "+", "=", "{", "}", 
               "[", "]", "|", "\\", ":", ";", "\"", "'", 
               "<", ">", ",", ".", "?", "/", "~", "`",]
    numbers = [str(i) for i in range(10)]

    #user input
    indexValue = 0
    password = input("Enter your password:\n")

    #checks password length
    if (len(password) > 14):
        indexValue += 15
    else:
        suggest.append("You should increase your password length")


    #checks symbol count
    symbolCount = 0
    for i in symbols:
        symbolCount += password.count(i) * 5
    
    if (symbolCount // 5 < 4):
        suggest.append("You should add more symbols")
    indexValue += symbolCount
    
    #checks number count
    numberCount = 0
    for i in numbers:
        numberCount += password.count(i) * 3
    
    if (symbolCount // 3 < 4):
        suggest.append("You should add more numbers")
    indexValue += numberCount


    #checks for mix of upper/lower
    upper = len(re.findall(r'[A-Z]', password))
    lower = len(re.findall(r'[a-z]', password))
    try:
        percent = min(upper/lower, lower/upper) * 100
        if (percent > 20):
            indexValue += 5
        else:
            suggest.append("You should mix your password up with upper and lower cases")
    except:
        suggest.append("You should mix your password up with upper and lower cases")
    
    
    #results
    if (indexValue > 12):
        print("You have a strong password!")
    elif (indexValue > 7):
        print("You have a ok password!")
    else:
        print("You have a bad password!")
    print("Your index value is " + str(indexValue))
    
    #suggestions
    if (len(suggest) > 0):
        print("We suggest to:")
        for i in suggest:
            print(i)
    input("Press Enter to continue...")

def index():
    os.system('cls')
    #index tree
    print("Password Strength Index")
    print("Length > 14: 5")
    print("Symbols: 5 per")
    print("Numbers: 3 per")
    print("Mix of upper and lowercase: 5")
    print("-----------------------------")
    print("Strong: Index > 12")
    print("Ok: Index > 7")
    print("Bad: Index < 7")
    input("Press Enter to continue...")

def main():
    while True:
        os.system('cls')
        #menu
        print("===========Password Checker===========")
        print("1-----------------------Check Password")
        print("2----------See Password Strength Index")
        print("3---------------------------------Exit")
        
        #case checker
        try:
            menuSelect = int(input())
            match menuSelect:
                case 1:
                    checkPassword()
                case 2:
                    index()
                case 3:
                    print("See you next time!")
                    break
                case _:
                    print("Invalid Input")
                    time.sleep(0.3)
        except:
            print("Invalid Input")
            time.sleep(0.3)

if __name__ == "__main__":
    main()