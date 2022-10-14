import requests

class SaveKeeper:
    def __init__(self):
        pass

    def __str__(self):
        message = '''
    ---------------------------------------------------------
    ################### Welcome to SeaBed ###################
    ---------------------------------------------------------
    A place where you never need to reset a password again...

    User Guide --> 
    
    - Type (view) to view all the your accounts passwords.
    - Type (view - account name) to view 
    - Type (add) to add account details.
    - Type (edit - account name) to edit the account details.
    - Type (delete - account name) to delete the account.
    - Type (exit) to exit the program.
    ---------------------------------------------------------
    '''
        return message

    def view_accounts(self):
        get_url = 'https://api.sheety.co/b7d8ad9f87b711f1445e9821751afa0e/oopProject/sheet1'
        r = requests.get(get_url).json()
        return r["sheet1"]

    def view_account(self, social_media):
        get_url = 'https://api.sheety.co/b7d8ad9f87b711f1445e9821751afa0e/oopProject/sheet1'
        r = requests.get(get_url).json()

        for i in range(len(r["sheet1"])):
            if r["sheet1"][i]["socialMedia"] == social_media:
                return (r["sheet1"][i])

    def add_account(self, social_media, user_name, password):
        post_url = 'https://api.sheety.co/b7d8ad9f87b711f1445e9821751afa0e/oopProject/sheet1'
        data = {"sheet1":{'socialMedia': social_media, 'userName': user_name, 'password': password}}
        p = requests.post(post_url, json=data)
        return p.json()

    def edit_account(self, social_media, user_name, password):
        edit_url = 'https://api.sheety.co/b7d8ad9f87b711f1445e9821751afa0e/oopProject/sheet1/[Object ID]'
        
    
    def delete_account(self, social_media):
        delete_url = "https://api.sheety.co/b7d8ad9f87b711f1445e9821751afa0e/oopProject/sheet1/[Object ID]"
        

    def exit_program(self):
        return "Thanks for using SeaBed, hope to see you soon."