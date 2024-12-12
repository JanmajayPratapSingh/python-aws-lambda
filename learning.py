import requests
response=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
# print(response.json())
print(response.status_code)
user_details= response.json()
print(user_details[0]["id"])

for user in range(len(user_details)):
   print(user_details[user]["user"]["login"])