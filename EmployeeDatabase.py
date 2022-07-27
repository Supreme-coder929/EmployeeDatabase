
'''

NOTE!
BEFORE RUNNING THIS PROGRAM YOU MUST CREATE 2 TXT FILES
1 ORIGINAL FILE NAMED employeeDatabase.txt WHICH SHOULD BE PASTED INTO INFILE VARIABLE(Must get its full path)
AND 1 OUTPUT FILE NAMED employeeDatabase1.txt WHICH SHOULD BE WRITTEN INTO THE OUTFILE VARIABLE(Must get its full path)

You can name the txt file what ever you want but I just said one for example.


'''

import time
import sys


# Global variables
option1 = ''
optionDatabase = ''
employeeName = ''
employeelastName = ''
adminPassword = ''

# File Variables
infile = r'full path of file'
outfile = r'full path of file'

# Employee Database

employeeDatabase = open(r"full path of orgininal file not the output one", "a+")

# Admin Database
admin = {
    'admin':'admin123'
}

def strongpasswordCheck(password):
    print("Checking password...")
    if len(password) < 8 or password.lower() == password or password.upper() == password or password.isalnum()\
            or not any(i.isdigit() for i in password):
        print('Weak Password')

    else:
        print('Strong Password')

def deletefromDatabase():
    try:
        global employeeName
        global employeelastName
        print("Press CTRL-C to return to update database at anytime")
        print("This is the delete section of the database.")
        while True:
            print("Enter employee first name.")
            employeeName = input(">")
            print("Enter employee last name")
            employeelastName = input(">")
            print("Database Updated")
            try:
                delete_list = [str(employeeName), str(employeelastName)]
                with open(infile) as fin, open(outfile, "w+") as fout:
                    for line in fin:
                        for word in delete_list:
                            line = line.replace(word, "")
                        fout.write(line)
            except:
                print("No name found with that input")

    except KeyboardInterrupt:
        updateDatabase()


def addtoDatabase():
    try:
        print("Press CTRL-C to return to update database at anytime")
        while True:
        #User input 
            global employeeName
            global employeelastName
            print("Enter employee first name: ")
            employeeName = input(">")
            print("Enter employee last name: ")
            employeelastName = input(">")
        #Adding to the database
            employeeDatabase.write("\n Firstname: " + str(employeeName) + " Lastname: " + str(employeelastName))
            employeeDatabase.read()
            print("Database Updated")
    
    except KeyboardInterrupt:
        updateDatabase()
    

def updateDatabase():
    try:
        global optionDatabase
        print("Welcome to the update database")
        while True:
            print("Would you like to add or delete from database. Add/Delete ")
            optionDatabase = input(">")
            if optionDatabase == 'Add':
                addtoDatabase()
            elif optionDatabase == 'Delete':
                deletefromDatabase()
            else:
                print("Wrong Input")
    except KeyboardInterrupt:
        adminDatabase()
        

def changeAdmin():
    try:
        global adminPassword
        print("Welcome to the Admin Login configuration panel. ")
        print("Press CTRL-C to return to admin database")
        print("We also tell you if your password is weak or strong so make sure to put a secure password.")
        print("What would you like your new admin password to be.")
        adminPassword = input(">")
        strongpasswordCheck(adminPassword)
        admin['admin'] = str(adminPassword)
        time.sleep(1)
        print(admin)
    except KeyboardInterrupt:
        adminDatabase()       

#Admin Configuration Database
def adminDatabase():
    try:
        global option1
        print("Welcome Admin, you now have root privlleges to the employee database.")
        time.sleep(1)
        print("These are your options \nA- Update Database " + " \nB- Change Admin Login Password " + " \nC- Exit Program ")
        option1 = input(">")
        while True:
            if option1 == "A":
                updateDatabase()
            elif option1 == "B":
                changeAdmin()
            elif option1 == "C":
                sys.exit("Exiting Program")
    except KeyboardInterrupt:
        adminLogin()


# Login to database as admin
def adminLogin():
    print("Welcome to the Employee Database.")
    while True:
        print("Enter your username to login in as admin: ")
        usernameInput = input(">")
        if usernameInput not in admin:
            print("Wrong username for admin. Please try again")
            continue
        print("Please enter your admin password: ")
        value = admin['admin']
        password = input(">")
        if password != value:
            print("Invalid Password for Admin")
            continue
        print("Valid password for Admin")
        break
    adminDatabase()


adminLogin()
