import re
from urllib.request import urlopen
import csv 
import json


link = "https://www.trip.com/hotels/list?city=1&countryId=1&checkin=2020/11/18&checkout=2020/11/25&optionId=1&optionType=City&directSearch=0&display=Beijing&crn=1&adult=2&children=0&searchBoxArg=t&travelPurpose=0&ctm_ref=ix_sb_dl&domestic=1"
url_data = urlopen(link)
file = url_data.read()
data_decode = file.decode("utf-8")



already_exists = []

with open('hotel.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        already_exists.append(row[2])

regex_data = re.findall(r'HOTEL=(.*)', data_decode)

response_data = regex_data[0][0:-1]
res = json.loads(response_data)

data_hotel_count = len(res['initData']['firstPageList']['hotelList']['list'])

rows = []
for i in range(data_hotel_count):
    k = ''
    li = []
    data = res['initData']['firstPageList']['hotelList']['list'][i]
    if data['base']['hotelName'] in already_exists:
        continue
    else:
        data = res['initData']['firstPageList']['hotelList']['list'][i]
        li.append(data['money']['priceNote'])
        li.append(data['base']['star'])
        li.append(data['base']['hotelName'])
        for u in range(len((data['facility']['list']))):
            k = k+data['facility']['list'][u]['name']+", "
        
        li.append(k)
        rows.append(li)

 
filename = "hotel.csv"
    

with open(filename, 'a+', newline='') as write_obj:
    csv_writer = csv.writer(write_obj)
    csv_writer.writerows(rows)
