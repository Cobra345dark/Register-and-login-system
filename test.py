
def Registration():
    print("Please choose what you would like to do.")
    choice = int(input("\nFor Registration Type 1 and For login  Type 2: "))
    if choice == 1:
        return getdetails()
    elif choice == 2:
        return loginExisting()
    else:
        return "TypeError"

def IsEmailFile(email):
    f = open("REGISTRATION.txt", "r")
    writer = f.read()
    if email in writer:
        f.close()
        return True
    else:
        f.close()
        return False

def Emaildetails():
    import re
    Email = input("EMAIL: ")
    check = "^[a-z-\S]*[a-z0-9]+@[a-z]+(\.[a-z]{2,3})+"
    if re.fullmatch(check, Email):
        if IsEmailFile(Email):
            print("email is already exist")

            Emaildetails()
        else:
            return Email
    else:

        Emaildetails()

def Passworddetails():
    Password = input("PASSWORD: ")

    L, U, SP, D = 0, 0, 0, 0
    capitalalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallalphabets = "abcdefghijklmnopqrstuvwxyz"
    digits = "1234567890"
    specialcher = "~`!@#$%^&*()_-+=|\}]{[':;?/>.<,*-+."
    A = " \" "
    special = specialcher + A
    if (len(Password) >= 5):
        for i in Password:
            if (i in smallalphabets):
                L += 1
            if (i in capitalalphabets):
                U += 1
            if (i in digits):
                D += 1
            if (i in special):
                SP += 1
        if (L >= 1 and U >= 1 and SP >= 1 and D >= 1 and L + U + SP + D == len(Password)):
            S=True
        if S:
            Password2 = input(("CONFIRM PASSWORD: "))
            if (Password != Password2):
                print("CONFIRM PASSWORD DOES NOT MATCH ....")
                Passworddetails()

            else:
                print("REGISTRATION SUCCESSFULLY")
                return Password
        else:
            print("Must have minimum one special character,one digit,one uppercase, one lowercase character")
            Password
    else:
        print("Invalid Password")
        print("minimum 5 cher enter")
        Password


def getdetails():
    f = open("REGISTRATION.txt", "r")
    print("\nREGISTRATION\n")
    print("-"*20)
    print("Enter Your Details")
    print("-" * 20)
    Email=Emaildetails()
    Password=Passworddetails()
    e = []
    f = []

    for line in f:
        a,b= line.split(",")
        b=b.strip()
        e.append(a[0])
        f.append(b[1])
    f=open("REGISTRATION.txt","a")
    #writer = writer+"\n"+Email+" "+Password
    f.write(Email+" "+Password+"\n")


def loginExisting():
    userDataEntry = open('REGISTRATION.txt', 'r')
    listLines = userDataEntry.readlines()
    userDataEntry.close()

    userDict = {}

    for eachLine in listLines:
        entry = eachLine.split()
        username = entry[0]
        password = entry[1]
        userDict[username] = password

    choose = 1
    while(choose == 1):
        print("\n-----------------  LOGIN  --------------------\n\n")
        usernameInput = input("Please enter your username: ")

        if(usernameInput in userDict):
            passwordInput = input("Please enter your password: ")
            if(userDict[usernameInput] == passwordInput):
                print("\nLogin successful!\nWelcome back, ", usernameInput)
                checker = 3

            else:
                print("Password is incorrect. Try again.")
                print("\n1)  CONTINUE\n2)  FOGET PASSWORD")
                choose = int(input(" "))
                if choose==2:
                    NewPassword = input("PASSWORD: ")
                    S=False
                    L, U, SP, D = 0, 0, 0, 0
                    capitalalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    smallalphabets = "abcdefghijklmnopqrstuvwxyz"
                    digits = "1234567890"
                    specialcher = "~`!@#$%^&*()_-+=|\}]{[':;?/>.<,*-+."
                    A = " \" "
                    special = specialcher + A
                    if (len(NewPassword) < 5):
                        print("Create Password with length between more then 5 an 16, Try Again")
                        loginExisting()
                    if (len(NewPassword) >= 5):
                        for i in NewPassword:
                            if (i in smallalphabets):
                                L += 1
                            if (i in capitalalphabets):
                                U += 1
                            if (i in digits):
                                D += 1
                            if (i in special):
                                SP += 1
                        if (L >= 1 and U >= 1 and SP >= 1 and D >= 1 and L + U + SP + D == len(NewPassword)):
                            S = True
                        if S:
                            Password2 = input(("CONFIRM PASSWORD: "))
                            while (NewPassword != Password2):
                                print("CONFIRM PASSWORD DOES NOT MATCH ....")
                                print("PLEASE TRY AGAIN....")
                                Password2 = input(("CONFIRM PASSWORD: "))
                        else:
                            print("Must have minimum one special character,one digit,one uppercase, one lowercase character")
                            loginExisting()

                        print(".......Password changed.......")
                        f = open("REGISTRATION.txt", "w")
                        f.write( usernameInput + " " + NewPassword+"\n" )
                        f.close()
        else:
            print("Username does not exist. Try again.\n")
            a=int(input("\nWould you like to:\n1.) Try Again\n2.) Registration\n\n"))
            if (a == 1):
                loginExisting()

            if (a == 2):
                print("\nReturning to Registration...\n")
                print(" ")
                Registration()

            choose = 1

    nextStep = int(input("\nWould you like to:\n1.) Exit\n2.) Log out and return to menu\n\n"))
    if(nextStep == 1):
        print("\nGoodbye!")

    if(nextStep == 2):
        print("\nReturning to menu...\n")
        print(" ")
        Registration()

Registration()

