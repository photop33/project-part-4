import requests
user_id = "1"


dic = open ('k8s_url.txt','r')
read = dic.read()
print (read)


res = requests.get('http://127.0.0.1:5500/user/' + user_id + '')
if res.ok:
    print(res.json())
