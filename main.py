import re
import os
import time
import numpy as np


commonpws = [
    "password", "123456", "123456789", "guest", "qwerty", "12345678",
    "111111", "12345", "col123456", "123123", "1234567", "1234",
    "1234567890", "000000", "555555", "666666", "123321", "654321",
    "7777777", "123", "D1lakiss", "777777", "110110jp", "1111",
    "987654321", "121212", "Gizli", "abc123", "112233", "azerty",
    "159753", "1q2w3e4r", "54321", "pass@123", "222222", "qwertyuiop",
    "qwerty123", "qazwsx", "vip", "asdasd", "123qwe", "123654",
    "iloveyou", "a1b2c3", "999999", "Groupd2013", "1q2w3e", "usr",
    "Liman1000", "1111111", "333333", "123123123", "9136668099",
    "11111111", "1qaz2wsx", "password1", "mar20lt", "987654321",
    "gfhjkm", "159357", "abcd1234", "131313", "789456", "luzit2000",
    "aaaaaa", "zxcvbnm", "asdfghjkl", "1234qwer", "88888888", "dragon",
    "987654", "888888", "qwe123", "football", "3601", "asdfgh", "master",
    "samsung", "12345678910", "killer", "1237895", "1234561", "12344321",
    "daniel", "000000", "444444", "101010", "fuckyou", "qazwsxedc",
    "789456123", "super123", "qwer1234", "123456789a", "823477aA",
    "147258369", "unknown", "98765", "q1w2e3r4", "232323", "102030",
    "12341234", "147258", "shadow", "123456a", "87654321", "10203",
    "pokemon", "princess", "azertyuiop", "thomas", "baseball", "monkey",
    "jordan", "michael", "love", "1111111111", "11223344", "123456789",
    "asdf1234", "147852", "252525", "11111", "loulou", "111222",
    "superman", "qweasdzxc", "soccer", "qqqqqq", "123abc", "computer",
    "qweasd", "zxcvbn", "sunshine", "1234554321", "asd123", "marina",
    "lol123", "a123456", "Password", "123789", "jordan23", "jessica",
    "212121", "7654321", "googledummy", "qwerty1", "123654789", "naruto",
    "Indya123", "internet", "doudou", "anmol123", "55555", "andrea",
    "anthony", "martin", "basketball", "nicole", "xxxxxx", "1qazxsw2",
    "charlie", "12345qwert", "zzzzzz", "q1w2e3", "147852369", "hello",
    "welcome", "marseille", "456123", "secret", "matrix", "zaq12wsx",
    "password123", "qwertyu", "hunter", "freedom", "999999999", "eminem",
    "junior", "696969", "andrew", "michelle", "wow12345", "juventus",
    "batman", "justin", "12qwaszx", "Pass@123", "passw0rd", "soleil",
    "nikita", "Password1", "qweqwe", "nicolas", "robert", "starwars",
    "liverpool", "5555555", "bonjour", "124578"
]

dictionary = [
    "which", "their", "there", "about", "would", "these", "other", "could", "words", "first",
    "thing", "those", "people", "after", "think", "great", "still", "every", "where", "world",
    "right", "small", "large", "found", "house", "place", "while", "group", "under", "never",
    "along", "might", "among", "story", "since", "young", "thing", "point", "three", "times",
    "using", "under", "often", "known", "until", "those", "woman", "since", "where", "years",
    "before", "after", "above", "below", "along", "today", "learn", "never", "shall", "whose",
    "night", "begin", "under", "after", "above", "below", "along", "today", "learn", "never",
    "shall", "whose", "night", "begin", "while", "every", "large", "place", "along", "might",
    "house", "thing", "found", "small", "story", "right", "point", "still", "group", "world",
    "young", "three", "times", "using", "often", "known", "until", "woman", "years", "before"
]

def heuristical_keyboardProximity(str, seqcount):
    patterns = []
    str = str.lower()
    kb_numrow = '1234567890'
    kb_symbrow = '!@#$%^&*()_+'
    kb_toprow = 'qwertyuiop[]'
    kb_midrow = 'asdfghjkl;'
    kb_botrow = 'zxcvbnm,./'

    selectedrow = ''
    sequenceCount = 0
    sequenceDirection = 0
    sequenceStr = ""
    prevchar = ''
    
    for i in range(len(str)):    
        charRow = ''
        if(kb_numrow.find(str[i]) != -1):
            charRow = kb_numrow
        elif(kb_symbrow.find(str[i]) != -1):
            charRow = kb_symbrow
        elif(kb_toprow.find(str[i]) != -1):
            charRow = kb_toprow
        elif(kb_midrow.find(str[i]) != -1):
            charRow = kb_midrow
        elif(kb_botrow.find(str[i]) != -1):
            charRow = kb_botrow
        else:
            selectedrow = ''
            sequenceCount = 0
            sequenceDirection = 0
        if selectedrow == charRow:
            if sequenceDirection == 0:
                if prevchar == charRow[charRow.find(str[i])-1 % len(charRow)]: #kb l to r
                    sequenceDirection = 1
                    sequenceCount = 2
                    sequenceStr = prevchar + str[i]
                elif prevchar == charRow[charRow.find(str[i])+1 % len(charRow)]: #kb r to l
                    sequenceDirection = -1
                    sequenceCount = 2
                    sequenceStr = prevchar + str[i]
            else:
                if sequenceDirection == 1:
                    if prevchar == charRow[charRow.find(str[i])-1 % len(charRow)]:
                        sequenceCount+=1
                        sequenceStr += str[i]
                    else:
                        if(sequenceCount >= seqcount):
                            patterns.append(sequenceStr)
                        sequenceCount = 0
                        sequenceDirection = 0
                        sequenceStr = ""
                if sequenceDirection == -1:
                    if prevchar == charRow[charRow.find(str[i])+1 % len(charRow)]:
                        sequenceCount+=1
                        sequenceStr += str[i]
                    else:
                        if(sequenceCount >= seqcount):
                            patterns.append(sequenceStr)
                        sequenceCount = 0
                        sequenceDirection = 0
                        sequenceStr = ""
        else:
            selectedrow = charRow
            sequenceCount = 0
            sequenceDirection = 0
            sequenceStr = ""
        prevchar = str[i]
    if(sequenceCount >= seqcount):
        patterns.append(sequenceStr)
    return patterns

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
    if (len(password) < 14):
        suggest.append("You should increase your password length")
    else:
        indexValue += len(password)-14


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
    
    if (numberCount // 3 < 4):
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
    
    common = []
    for i in dictionary:
        if i in password:
            common.append(i)
    if len(common) > 0:
        suggest.append("You have common phrases in you password, try switching it up")
        for i in common:
            suggest.append(i)
        indexValue -= 5
    
    pattern = heuristical_keyboardProximity(password, 4)
    if (len(pattern) > 0):
        indexValue -= len(pattern) * 5
        suggest.append("You have a common pattern in you password: ")
        for i in pattern:
            suggest.append(i)


    if (password in commonpws):
        indexValue = 0
        suggest.clear()
        suggest.append("You have a common password, please change it")


    
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
    print("Length > 14: 1 per")
    print("Symbols: 5 per")
    print("Numbers: 3 per")
    print("Mix of upper and lowercase: 5")
    print("Common English Words: -5")
    print("Common Password: = 0")
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

#test cases
#ray
#raymondjiang!!!!!
#raymondjiang19191!!!!
#raymonDJIANG19191!!!!
#password
#whichtheir
#qwerty
#asdfg
#zxcvb