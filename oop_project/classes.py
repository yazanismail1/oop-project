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

    - Type (1) to view all the your accounts passwords.
    - Type (2) to view a specific account.
    - Type (3) to add account details.
    - Type (4) to edit the account details.
    - Type (5) to delete the account.
    - Type (6) to exit the program.
    ---------------------------------------------------------
    '''
        return message

    def view_accounts(self):
        # get_url = 'https://api.sheety.co/b7d8ad9f87b711f1445e9821751afa0e/oopProject/sheet1'
        get_url = f'https://api.sheety.co/f2fe1789e9008afa182a1e94b12229f3/seabed/sheet1'

        r = requests.get(get_url).json()
        return r["sheet1"]

    def view_account(self, social_media):
        get_url = 'https://api.sheety.co/b7d8ad9f87b711f1445e9821751afa0e/oopProject/sheet1'
        r = requests.get(get_url).json()

        for i in range(len(r["sheet1"])):
            if r["sheet1"][i]["socialMedia"] == social_media:
                x = r["sheet1"][i]["socialMedia"] + " --> " + "User Name: " + \
                    r["sheet1"][i]["userName"] + ", " + \
                        "Password: " + str(r["sheet1"][i]["password"])
        return (x)

    def add_account(self, social_media, user_name, password):
        post_url = 'https://api.sheety.co/b7d8ad9f87b711f1445e9821751afa0e/oopProject/sheet1'
        data = {"sheet1": {'socialMedia': social_media,
            'userName': user_name, 'password': password}}
        requests.post(post_url, json=data)
        return (f"{social_media} has been added to your collection successfully")
##################################################################################
    def edite_account(self, social_media, user_name, password):

        a = self.view_accounts()
        def Id():
            for i in a:
                for (key, value) in i.items():
                    if value == social_media:
                        return i["id"]
                    else:
                        return ("This social media does'nt exist")

        ID = Id()
        if (isinstance(ID, int) ):
            # edit_url = f'https://api.sheety.co/b7d8ad9f87b711f1445e9821751afa0e/oopProject/sheet1/{ID}'
            edite_url = f'https://api.sheety.co/f2fe1789e9008afa182a1e94b12229f3/seabed/sheet1/{ID}'

            data = {"sheet1": {'socialMedia': social_media,
                'userName': user_name, 'password': password}}

            requests.put(edite_url, json=data)
            return "Edited successfully"
        
        
        
        
        else:
            return(" OOps! This social media does'nt exist to be modified ")

        
#######################################################################################
    def delete_account(self, social_media):
        a = self.view_accounts()

        def Id():
            for i in a:
                for (key, value) in i.items():
                    if value == social_media:
                        return i["id"]
                    else:
                        return (" ")


        ID = Id()
        
        if (isinstance(ID, int) ):
            delete_url = f'https://api.sheety.co/f2fe1789e9008afa182a1e94b12229f3/seabed/sheet1/{ID}'

            #delete_url = f"https://api.sheety.co/b7d8ad9f87b711f1445e9821751afa0e/oopProject/sheet1/{ID}"
            requests.delete(delete_url)
            return f"You deleted {social_media} from your collection."
        
        else:
            return(" OOps! This social media does'nt exist to be deleted")
     
     
    def exit_program(self):
        return "Thanks for using SeaBed, hope to see you soon."
    
razan=SaveKeeper()
# print(razan.delete_account("snapchat"))
print(razan.edite_account("cebook","Tttest",0))
print(razan.delete_account("cebook",))

#######
# print(razan.view_accounts())
