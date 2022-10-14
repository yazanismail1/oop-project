# import requests

# get_url = 'https://api.sheety.co/b7d8ad9f87b711f1445e9821751afa0e/oopProject/sheet1'
# post_url = 'https://api.sheety.co/b7d8ad9f87b711f1445e9821751afa0e/oopProject/sheet1'
# put_url = 'https://api.sheety.co/b7d8ad9f87b711f1445e9821751afa0e/oopProject/sheet1/3'
# delete_url = 'https://api.sheety.co/b7d8ad9f87b711f1445e9821751afa0e/oopProject/sheet1/3'

# data = {"sheet1":{'socialMedia': 'Instagram', 'userName': 'ggg', 'password': "123wfwfw245"}}

# # d = requests.delete(delete_url)
# p = requests.put(put_url, json=data)
# # p = requests.post(post_url, json=data)
# r = requests.get(get_url).json()

# for i in range(len(r["sheet1"])):
#     if r["sheet1"][i]["socialMedia"] == "Facebook":
#         x =  r["sheet1"][i]["socialMedia"] + " --> " + "User Name: " + r["sheet1"][i]["userName"] + ", " + "Password: " + str(r["sheet1"][i]["password"])
#         print(x)
