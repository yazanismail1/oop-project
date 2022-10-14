import requests

get_url = 'https://api.sheety.co/b7d8ad9f87b711f1445e9821751afa0e/oopProject/sheet1'
post_url = 'https://api.sheety.co/b7d8ad9f87b711f1445e9821751afa0e/oopProject/sheet1'
put_url = 'https://api.sheety.co/b7d8ad9f87b711f1445e9821751afa0e/oopProject/sheet1/[Object ID]'
delete_url = 'https://api.sheety.co/b7d8ad9f87b711f1445e9821751afa0e/oopProject/sheet1/3'

data = {"sheet1":{'socialMedia': 'Snapchat', 'userName': 'ggg', 'password': "123wfwfw245"}}

d = requests.delete(delete_url)
# p = requests.put(put_url, json)
# p = requests.post(post_url, json=data)
# g = requests.get(get_url).json()
# for i in range(len(g["sheet1"])):
#     if g["sheet1"][i]["socialMedia"] == "Insta":
#         print(g["sheet1"][i])
print(d)