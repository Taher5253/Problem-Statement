import urllib3
import requests
import json
import pymongo #importing pymongo library


#Creating mongodb connection
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

#Creating database and collection object
mydb = myclient["posts"]
mycol = mydb["posts_collection"]

#facebook url GET request
url_request_facebook = requests.get("https://graph.facebook.com/v3.1/me?fields=posts.include_hidden(true).show_expired(true)%7Bfull_picture%2Clink%2Ccomments%2Cdescription%2Cwith_tags%2Cplace%2Cattachments%2Clikes%2Cicon%2Cpicture%2Ctype%7D&access_token=EAAd6TdjdprUBAC8Inew2WCZBznKDVDC58cDAZCYkyAZC1sZCdsRexIgxZCuAwT1FkmHNhgzbt8B9NCeYbbksTaXWCDD9lGgLY6ZBM0wLZCZCX5b1VvNOg6iMiESdToHIJIlvTgcJ3krv1SeM9iaQD5A2tPC2KbPYB70G8AO6DhAdBfZBLrbj9P6yy8v1hF0hmcdwhwN3cZA3Yf0gZDZD")

#creating json object
data = url_request_facebook.json()

dictionary_data = data['posts']['data']


#storing dictionary in database
mycol.insert_many(dictionary_data)



