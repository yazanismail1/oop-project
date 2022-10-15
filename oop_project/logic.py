import random
import array
from oop_project.classes import password_keeper

def generate_password():
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
    digit = random.choice(DIGITS)
    digit2 = random.choice(DIGITS)
    upper = random.choice(UPCASE_CHARACTERS)
    upper2 = random.choice(UPCASE_CHARACTERS)
    lower = random.choice(LOCASE_CHARACTERS)
    lower2 = random.choice(LOCASE_CHARACTERS)
    symbol = random.choice(SYMBOLS)
    symbol2 = random.choice(SYMBOLS)
    Pass = digit + upper + lower + symbol+digit2+upper2+lower2+symbol2
    pass_list = array.array('u', Pass)
    random.shuffle(pass_list)
    password = ""
    for x in pass_list:
        password = password + x
    return password


def add_edit_account(method):
    social_media = input("Enter a social media name: ").title()
    user_name = input("Enter a user name: ")
    password_entry = input("Do you want to auto generate a password (Y/N)? \n> ").upper()
    if password_entry == "N":
        password = input("Enter a password: ")
        print(method(social_media, user_name, password))
    elif password_entry == "Y":
        password = generate_password()
        print(method(social_media, user_name, password))
    else:
        password = input("Invalid input.. kindly enter a password: ")
        print(method(social_media, user_name, password))

def error_message():
        print("There is something wrong from our side...Please try again later...Bye")

def start_application():
    running = True
    while running == True:
        print(password_keeper.__str__())
        user_input = input("> ")
        if user_input == "1":
            if password_keeper.view_accounts() == False:
                error_message()
                running = False
                return running
            else:
                print(password_keeper.view_accounts())
        elif user_input == "2":
            if password_keeper.view_accounts() == False:
                error_message()
                running = False
                return running
            else:
                try:
                    social_media = input("Enter a social Media name: ").title()
                    print(password_keeper.view_account(social_media))
                except UnboundLocalError:
                    print(f"Can't find {social_media}")

        elif user_input == "3":
            if password_keeper.view_accounts() == False:
                error_message()
                running = False
                return running
            else:
                add_edit_account(password_keeper.add_account)
        elif user_input == "4":
            if password_keeper.view_accounts() == False:
                error_message()
                running = False
                return running
            else:
                add_edit_account(password_keeper.edit_account)
        elif user_input == "5":
            if password_keeper.view_accounts() == False:
                error_message()
                running = False
                return running
            else:
                social_media = input("Enter a social Media name: ").title()
                print(password_keeper.delete_account(social_media))
        elif user_input == "6":
            print(password_keeper.exit_program())
            running = False
            return running
        else: 
            print("Invalid entry...")
            run_again = input("Kindly enter (Y) to view the starter guide or (E) to exit: ").upper()
            if run_again == "Y":
                pass
            elif run_again == "E":
                print(password_keeper.exit_program())
                running = False
                return running
            else:
                print("Wrong entry.. ")
                print(password_keeper.exit_program())
                running = False
                return running
