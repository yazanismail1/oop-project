# import requests
import random
import array

# get_url = 'https://api.sheety.co/b7d8ad9f87b711f1445e9821751afa0e/oopProject/sheet1'
# post_url = 'https://api.sheety.co/b7d8ad9f87b711f1445e9821751afa0e/oopProject/sheet1'
# put_url = 'https://api.sheety.co/b7d8ad9f87b711f1445e9821751afa0e/oopProject/sheet1/[Object ID]'
# delete_url = 'https://api.sheety.co/b7d8ad9f87b711f1445e9821751afa0e/oopProject/sheet1/3'

# data = {"sheet1":{'socialMedia': 'Snapchat', 'userName': 'ggg', 'password': "123wfwfw245"}}

# # d = requests.delete(delete_url)
# # p = requests.put(put_url, json)
# # p = requests.post(post_url, json=data)
# r = requests.get(get_url).json()

# for i in range(len(r["sheet1"])):
#     if r["sheet1"][i]["socialMedia"] == "Facebook":
#         x =  r["sheet1"][i]["socialMedia"] + " --> " + "User Name: " + r["sheet1"][i]["userName"] + ", " + "Password: " + str(r["sheet1"][i]["password"])
#         print(x)


def Generat_Password():

    PassWord_Len = 8

    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?',
               '.', '/', '|', '~', '>', '*', '(', ')', '<']

    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    digit = random.choice(DIGITS)
    upper = random.choice(UPCASE_CHARACTERS)
    lower = random.choice(LOCASE_CHARACTERS)
    symbol = random.choice(SYMBOLS)

    Pass = digit + upper + lower + symbol

    for x in range(PassWord_Len - 4):
        Pass = Pass + random.choice(COMBINED_LIST)

        pass_list = array.array('u', Pass)
        random.shuffle(pass_list)

    password = ""
    for x in pass_list:
        password = password + x

    return password


print(Generat_Password())
