import requests
url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'
response = requests.get(url)
info = response.json()
for pr_title in range(len(info)):
    print(f'User {info[pr_title]["user"]["login"]} has created: {info[pr_title]["title"]} as pr')
    # print(info[issue_title]["user"]["login"])
    # print(info[issue_title]["user"]["id"])