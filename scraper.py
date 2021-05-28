from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = "https://www.arabam.com/ikinci-el/otomobil?city="
links = []
for j in range(1):   #86 idi
    for i in range(1):  #50 idi
        print(i)
        url1 = url+str(j+1)+"&take=50&page="+str(i+1)
        html = urlopen(url1)
        soup = BeautifulSoup(html, "html.parser")  
        href = [div.a.get('href') for div in soup.find_all(class_='pr10 fade-out-content-wrapper')]
        links.append(href)

links = [j for sub in links for j in sub]

link = []
for i, value in enumerate(links):
    get_url = "https://www.arabam.com" + value
    link.append(get_url)  

#print(link \n)

fiyat = []
konum = []
ozellik = []
for i, value in enumerate(link):
    link_html = urlopen(value)
    link_soup = BeautifulSoup(link_html, "html.parser")
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
print(df)