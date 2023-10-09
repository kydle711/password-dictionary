import csv
import sys
import time
from cryptography.fernet import Fernet



#define fields for csv file and assign csv file to variable
fields = ['website', 'username', 'password']
file = 'passwordDict.csv'

"""Function to validate a users input before adding or deleting and account"""
def validate(account_name):
    account_list = []
    with open(file) as password_file:
        reader = csv.DictReader(password_file, fieldnames=fields)
        for row in reader:
            account_list.append(row['website'])
    return account_name in account_list

#append new account info to file
def add_password():

    #take input for account info and save to a list
    website = input("Enter a website or account name: ")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    print("")
    account_info_list = [website, username, password]

    #Call validate() with first element of account_info_list, which represents website name
    #Validate needs to return False here indicating the name isnt taken and account can be added
    if validate(account_info_list[0]) == False:
        new_account = dict(zip(fields, account_info_list))
        with open(file, 'a') as password_file:
            writer = csv.DictWriter(password_file, fieldnames=fields)
            writer.writerow(new_account)
            print("Password successfully saved!\n"
                  "")

    else:
        print("It appears you already have an account saved with that name.")
        print("Consider deleting that account and updating with new info.\n"
              "")

    time.sleep(2)
    display_menu()


#take account name and remove line from file
def delete_password():
    #take input for account to delete
    deletion = input("Enter an account website to delete it: ")

    #new list for storing info to write new file without deleted account
    new_file = []

    #call validate() with user input and perform rewrite if true, else print message
    #Validate needs to return True here indicating entry exists before deleting
    if validate(deletion) == True:

        """read file and check for line matching user input to delete. append all lines to new file list except
        the line to be deleted"""
        with open(file, 'r') as password_file:
            reader = csv.DictReader(password_file, fieldnames=fields)

            for row in reader:
                if row['website'] != deletion:
                        new_file.append(row)

        # Exit 'with' context manager and open a new context manager with the file in 'write' mode
        with open(file, 'w') as password_file:
            writer = csv.DictWriter(password_file, fieldnames=fields)
            # write new list to file
            writer.writerows(new_file)
            print("Account deleted\n"
                  "")
    else:
        print("That account does not exist\n"
              "")

    time.sleep(1)
    display_menu()


#display all account info in readable format
def display_passwords():
    print("Here are your current accounts and passwords: ")
    with open(file) as password_file:
        reader = csv.DictReader(password_file, fieldnames=fields)
        for row in reader:
            print("Website: {}   Username: {}   Password: {}".format(*row.values()))
        print("")
        time.sleep(2)

    display_menu()


def display_menu():
    print("Welcome to Password Dictionary!\n"
          "\n"
          "Here are your menu options:\n"
          "display\n"
          "add\n"
          "delete\n"
          "quit\n"
          "")

    selection = input("Select an option: ").lower()
    if selection == 'display':
        display_passwords()
    elif selection == 'add':
        add_password()
    elif selection == 'delete':
        delete_password()
    elif selection == 'quit':
        sys.exit()
    else:
        print("\n"
              "Invalid entry\n"
              "")
        time.sleep(1)
        display_menu()



"""Iniliza program by calling display_menu()"""

display_menu()
