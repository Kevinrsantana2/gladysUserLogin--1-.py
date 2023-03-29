# import io

# """
# 	Student: Kevin Ruiz Santana
# 	Module: gladysUserLogin
# 	Description: This module The function takes no arguments and asks the users for login and password, verifies that the login is valid, and then returns the users login.
# """

#imported re
import re
# regex == describes a set of str that match the pattern
#regex from email
regex =  '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
#take input
email = input("Enter you email adress: ")
password = input("Enter your password: ")

#function to logins
def login():   
    
    #check for valid email
    if(re.search(regex,email)):
#check for valid pass which is first 5 chars of email
        if (password == password ): 
            
            print("You have been looged in.")
        else:
            print("Wrong password")
    else:   
        print("Invalid Email") 

#call the fucntion
login()