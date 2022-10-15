from tokenize import Number
import requests

class SaveKeeper:
    def __init__(self):
        pass

    def __str__(self):
        message = '''
    ---------------------------------------------------------------------
    ######################### Welcome to SeaBed #########################
    ---------------------------------------------------------------------
    A place where you never need to reset a password again...

    User Guide --> 
    
    - Type (1) to view all the your accounts passwords.
    - Type (2) to view a specific account.
    - Type (3) to add account details.
    - Type (4) to edit the account details.
    - Type (5) to delete the account.
    - Type (6) to exit the program.

    **You can either enter your own password or generate one.
    ---------------------------------------------------------------------
    '''
        return message

    def exit_when_error(self):
        running = False
        return running 

    def view_accounts(self):
        get_url = 'https://api.sheety.co/c1df31f0d1175633aa5e26cb199f84f8/oop/sheet1'
        r = requests.get(get_url)
        r_json = r.json()
        if r.status_code != 200:
            return self.exit_when_error()
        else:
            return r_json["sheet1"]

    def view_account(self, social_media):
        get_url = 'https://api.sheety.co/c1df31f0d1175633aa5e26cb199f84f8/oop/sheet1'
        r = requests.get(get_url).json()

        for i in range(len(r["sheet1"])):
            if r["sheet1"][i]["socialMedia"] == social_media:
                x = r["sheet1"][i]["socialMedia"] + " --> " + "User Name: " + r["sheet1"][i]["userName"] + ", " + "Password: " + str(r["sheet1"][i]["password"])
        return (x)

    def add_account(self, social_media, user_name, password):
        post_url = 'https://api.sheety.co/c1df31f0d1175633aa5e26cb199f84f8/oop/sheet1'
        get_url = 'https://api.sheety.co/c1df31f0d1175633aa5e26cb199f84f8/oop/sheet1'
        r = requests.get(get_url).json()

        for i in range(len(r["sheet1"])):
            if r["sheet1"][i]["socialMedia"] == social_media:
                return (f"{social_media} already in your collection")
            else:
                data = {"sheet1":{'socialMedia': social_media, 'userName': user_name, 'password': password}}
                requests.post(post_url, json=data)
                return (f"{social_media} has been added to your collection successfully")

    def edit_account(self, social_media, user_name, password):
        a = self.view_accounts()
        def Id():
            dict = {}
            for i in range(len(a)):
                dict[a[i]["socialMedia"]] = a[i]["id"]
            if social_media in dict:
                return dict[social_media]
            else:
                return ("This social media does'nt exist")
        ID = Id()
        if (isinstance(ID, int) ):
            edite_url = f'https://api.sheety.co/c1df31f0d1175633aa5e26cb199f84f8/oop/sheet1/{ID}'
            data = {"sheet1": {'socialMedia': social_media, 'userName': user_name, 'password': password}}
            requests.put(edite_url, json=data)
            return "Edited successfully"
        else:
            return(" OOps! This social media doesn't exist to be modified ")

    def delete_account(self, social_media):
        a = self.view_accounts()
        def Id():
            dict = {}
            for i in range(len(a)):
                dict[a[i]["socialMedia"]] = a[i]["id"]
            if social_media in dict:
                return dict[social_media]
            else:
                return (" ")
        ID = Id()
        if (isinstance(ID, int) ):
            delete_url = f'https://api.sheety.co/c1df31f0d1175633aa5e26cb199f84f8/oop/sheet1/{ID}'
            requests.delete(delete_url)
            return f"You deleted {social_media} from your collection."
        else:
            return("OOps! This social media doesn't exist to be deleted")
     
    def exit_program(self):
        return "Thanks for using SeaBed, hope to see you soon."

password_keeper = SaveKeeper()
