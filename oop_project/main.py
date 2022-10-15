# import requests
import random 

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

razan=[1,2,3,4,5,6,7,8,9]
print(razan)
print (random.shuffle(razan))
print(razan)
