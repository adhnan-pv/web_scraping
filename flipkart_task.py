from urllib.request import Request
from urllib import request
from bs4 import BeautifulSoup
import json

url="https://www.flipkart.com/"
single_url="https://www.flipkart.com/apple-iphone-15-pro-black-titanium-256-gb/p/itm2731066ffb3cc?pid=MOBGTAGPHKDJXZJA&lid=LSTMOBGTAGPHKDJXZJAZIBNQ5&marketplace=FLIPKART&q=iphone+15+pro&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_OrganicAutoSuggest_3_9_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_3_9_na_na_na&fm=neo%2Fmerchandising&iid=7e26d641-a6c4-4ed8-8d1a-de986396b0d6.MOBGTAGPHKDJXZJA.SEARCH&ppt=clp&ppn=the-big-billiondays-2023-top-deals-from-house-of-apple-12gfd-store&ssid=xyo1y2e4sg0000001696334532024&qH=c9de95b3b911a866"
request_site=Request(single_url)
html_data=request.urlopen(request_site).read()
soup=BeautifulSoup(html_data,'html.parser')
#print(soup)

def getprodInfo():
    titleclass=soup.find('div')
    title=titleclass.find('span',{"class":"B_NuCI"}).text
    boxclass=soup.find('div',{"class":"_1UhVsV _3AsE0T"})
    box=boxclass.find('li',{'class':"_21lJbe"}).text
    priceclass=soup.find('div',{'class':"_30jeq3 _16Jk6d"}).text
    ratingclass=soup.find('div',{'class':"_3LWZlK"}).text
    sellerclass=soup.find('div',{"class":"_1RLviY"})
    seller=sellerclass.find('span').text





    return title,box,priceclass,ratingclass,seller



title,box,priceclass,ratingclass,seller=getprodInfo()
print('product:',title)
print('in box:',box)
print('price:',priceclass)
print('rating:',ratingclass)
print('seller:',seller)


