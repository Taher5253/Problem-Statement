from bs4 import BeautifulSoup # importing BeautifulSoup package
import requests
import pymongo                  # importing pymongo library


#fecthing url
source = requests.get('http://coreyms.com').text

#parsing data 
soup = BeautifulSoup(source, 'lxml')


#creating lists
list1= []
list2= []
list3= []
list4= []




#parsing images from webpage 
for img in soup.findAll('img'):
        images=(img.get('src'))
        images='https:'+images
        list2.append(images)      
        

#parsing data, videolinks, summary, headline
for article in soup.find_all('article'):
    headline = article.h2.a.text     
    list1.append(headline)
    
    summary = article.find('div', class_='entry-content').p.text
    list3.append(summary)


    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
        list4.append(yt_link)
        
    except Exception as e:
        yt_link = None
        list4.append(yt_link)
        


#converting lists to string
str_headline =', '.join(map(str,list1))
str_images =', '.join(map(str,list2))
str_yt_link =', '.join(map(str,list4))
str_summary =', '.join(map(str,list3))


#creating and storing data in dictionary
dictionary_collection={"images":str_images, "headline":str_headline, "summary":str_summary, "yt_link":str_yt_link}


#Creating mongodb connection
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

#Creating database and collection object
mydb = myclient["web_scrap_one"]
mycol = mydb["webscrapone_collection"]


#storing dictionary in database
mycol.insert_one(dictionary_collection)


