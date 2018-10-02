from bs4 import BeautifulSoup # importing BeautifulSoup package
import requests
import pymongo              #importing pymongo library


#fecthing indiamart url
source = requests.get('https://www.indiamart.com/abhaytelecomservices/products.html').text

#parsing data 
soup = BeautifulSoup(source, 'lxml')

#creating lists
list1= []
list2= []
list3= []
list4= []
list5= []






#parsing vendor name
title = soup.find('div', class_='ds1 vr1 fnt1 bo1 clr1 w3').text


#parsing product name
for p_name in soup.find_all('h2', class_='comp-titl ps2 fnt36_mn clr15_sh txl bo1 m5_mn'):
    product_name = p_name.a.text
    list1.append(product_name)
    


#parsing product price 
for p_price in soup.find_all('p', class_='ds1'):
    product_price = p_price.text
    list2.append(product_price)
    

#parsing order quantity details
for p_quantity in soup.find_all('p', class_='cntntTulTip'):
    product_quantity = p_quantity.text
    list3.append(product_quantity)
    

#parsing warranty and color
for p_wc in soup.find_all('table', class_='b27_mm ds2 w14_mn'):
    product_wc = p_wc.text
    list4.append(product_wc)
    

#parsing product features
for features in soup.findAll('div', class_='w6_sh m1 ds m4_mn'):
    for feature_details in features.find_all('ul'):
        product_feature = feature_details.text
        list5.append(product_feature)
        
  

#parsing vendor address
vendor_address=soup.find('p', class_='contact-nam fl m33')
address=vendor_address.text

#Creating mongodb connection
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

#Creating database and collection object
mydb = myclient["web_scrap_two"]
mycol = mydb["webscraptwo_collection"]


#storing corresponding product details using dictionary
for i in range(len(list1)):
 
    str_name =''.join(map(str,list1[i]))

    str_price =''.join(map(str,list2[i]))

    str_quantity =''.join(map(str,list3[i]))

    dict_collection={"Product_name":str_name, "Price":str_price, "Order_Quantity":str_quantity}


        
#storing vendor address
dict_collection_address={"Address":address}
mycol.insert_one(dict_collection_address)

#storing vendor name
dict_collection_vendorname={"Vendor Name":title}
mycol.insert_one(dict_collection_vendorname)


#converting lists to string
str_pname =', '.join(map(str,list1))

str_pprice =', '.join(map(str,list2))

str_pquantity =', '.join(map(str,list3))

str_warranty_color =''.join(map(str,list4))

str_features =', '.join(map(str,list5))


#storing features and other details
dict_collection_productspecification={"Product_Name":str_pname, "Product_Price":str_pprice, "Minimum_quantity":str_pquantity, "Warranty_color":str_warranty_color, "Features":str_features}
mycol.insert_one(dict_collection_productspecification)




