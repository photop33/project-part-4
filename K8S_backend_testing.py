import requests
import db_connector as db

print("__name__:", __name__)
print()


txt_k8s_svc_url = "k8s_url.txt"

f = open(txt_k8s_svc_url, "r")
url_base = f.read()
print(url_base)


url_test = "{url}/test".format(url = url_base)
url_tbl = "{url}/{tbl}".format(url = url_base, tbl = db.tbl_users)


url = url_test
print(url)

resp = requests.get(url)
print(resp)
if (not resp.ok):
    print("Failed to execute request - GET")

print(resp.json())
print()










import requests
user_id = "1"

res = requests.get('http://127.0.0.1:5500/user/' + user_id + '')
if res.ok:
    print(res.json())
