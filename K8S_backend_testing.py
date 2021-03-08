import requests
user_id = "1"


res = open ('k8s_url.txt',"r")
read = res.read()
print (res)


res = requests.get('http://127.0.0.1:5500/user/' + user_id + '')
if res.ok:
    print(res.json())
