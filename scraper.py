from bs4 import BeautifulSoup
from urllib.request import urlopen

import pandas as pd
import numpy as np
import urllib3

http = urllib3.PoolManager()

url = "https://www.arabam.com/ikinci-el/otomobil?city="
#url = "https://www.sahibinden.com/otomobil/adana?"
links = []
for j in range(1):   #86 idi
    for i in range(1):  #50 idi
        print(i)
        url1 = url+str(j+1)+"&take=50&page="+str(i+1) 
        #url1 = url+"&pagingSize=50&pagingOffset="+str(i*50)
        print("url1= " + url1)

        #http = urllib3.PoolManager()
        r = http.request('GET', url1)
        htmlSource = r.data

        soup = BeautifulSoup(htmlSource, "html.parser")
        #print(soup)
        href = [div.a.get('href') for div in soup.find_all(class_='pr10 fade-out-content-wrapper')]
        #print(href)
        links.append(href)

links = [j for sub in links for j in sub]

link = []
for i, value in enumerate(links):
    get_url = "https://www.arabam.com/" + value
    #print(get_url)
    link.append(get_url)  

#print(link \n)

fiyat = []
konum = []
ozellik = []
for i, value in enumerate(link):
    print(i)

    #link_html = urlopen(value)
    
    link_html = http.request('GET', value).data
    #print(link_html)

    link_soup = BeautifulSoup(link_html, "html.parser")
    #print(link_soup)

    #fiyat
    price = link_soup.find("span", {"class" : "color-red4 font-semi-big bold fl"})
    if price == None:
        price = link_soup.find("span", {"class" : "color-red4 font-semi-big bold fl w66"})
        if price == None:
            fiyat.append("None")
        else:
            fiyat.append(price.text) 
    else:
        fiyat.append(price.text)

    #konum
    location = link_soup.find(class_ = "one-line-overflow font-default-minus pt4 color-black2018 bold")
    if location == None:
        konum.append("None")
    else:
        konum.append(location.text)
    #arac ozellikleri
    info = link_soup.find("ul",{"class":"w100 cf mt16"})
    if info == None:
        ozellik.append("None")
    else:
        ozellik.append(info.text)
    


df = pd.DataFrame(list(zip(fiyat, konum, ozellik)), 
               columns =['Fiyat', 'Konum','Ozellik']) 
print(df.get())
