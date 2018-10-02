import urllib3
import requests
import json
import pymongo

#pythonsg.ex('test')

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

mydb = myclient["posts"]
mycol = mydb["posts_collection"]

print(mydb)
print(mycol)

attenders = requests.get("https://graph.facebook.com/v3.1/me?fields=posts.include_hidden(true).show_expired(true)%7Bfull_picture%2Clink%2Ccomments%2Cdescription%2Cwith_tags%2Cplace%2Cattachments%2Clikes%2Cicon%2Cpicture%2Ctype%7D&access_token=EAAd6TdjdprUBAC8Inew2WCZBznKDVDC58cDAZCYkyAZC1sZCdsRexIgxZCuAwT1FkmHNhgzbt8B9NCeYbbksTaXWCDD9lGgLY6ZBM0wLZCZCX5b1VvNOg6iMiESdToHIJIlvTgcJ3krv1SeM9iaQD5A2tPC2KbPYB70G8AO6DhAdBfZBLrbj9P6yy8v1hF0hmcdwhwN3cZA3Yf0gZDZD")
attenders_json = attenders.json()
json1_data = attenders_json['posts']['data']
print(json1_data)
#data  = json.loads(attenders_json)

mycol.insert_many(json1_data)

#y = json.loads(attenders_json)

#print(attenders_json)
print(type(attenders_json))


