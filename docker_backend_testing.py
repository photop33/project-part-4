import requests
import pymysql
user_id= "8"


res = requests.get('http://127.0.0.1:5000/user/'+ user_id +'', json={"user_name": ""+ user_name +""})
if res.ok:
    print(res.json())



    
