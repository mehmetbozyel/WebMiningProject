from bs4 import BeautifulSoup
from urllib.request import urlopen

import pandas as pd

import urllib3


http = urllib3.PoolManager()

url = "https://www.arabam.com/ikinci-el/otomobil?city="
#url = "https://www.sahibinden.com/otomobil/adana?"
links = []
for j in range(86):   #86 idi
    for i in range(5):  #50 idi
        print(i)
        url1 = url+str(j+1)+"&take=20&page="+str(i+1) 
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


df = df[df.Ozellik != 'None'].reset_index()
loc = df["Konum"].str.split("/", n = 1, expand = True)
df.drop(columns=["Konum"], inplace=True)

loc.drop(columns=[1],inplace=True)

#new = df["Ozellik"].str.split(":", n = 14, expand = True)
new = df["Ozellik"].str.split("    ", n = 14, expand = True)

new["Ilan_no"] = new[0].str.replace(' ??lan No: ', '')

new["Ilan_tarihi"] = new[1].str.replace('??lan Tarihi: ', '')
new["Marka"] = new[2].str.replace('Marka: ', '')
new["Seri"] = new[3].str.replace('Seri: ', '')
new["Model"] = new[4].str.replace('Model: ', '')
new["Y??l"] = new[5].str.replace('Y??l: ', '')
#new['Y??l'] = [str(x)[:5] for x in new['Y??l']]
new["Yak??t_tipi"] = new[6].str.replace('Yak??t Tipi: ', '')
new["Vites_tipi"] = new[7].str.replace('Vites Tipi: ', '')
new["Motor_hacmi"] = new[8].str.replace('Motor Hacmi: ', '')
#new["Motor_hacmi"] = new["Motor_hacmi"].str.replace("cc", "")
new["Motor_g??c??"] = new[9].str.replace('Motor G??c??: ', '')
#new['Motor_g??c??'] = [str(x)[:3] for x in new['Motor_g??c??']] 
#new['Motor_hacmi'] = [str(x)[:5] for x in new['Motor_hacmi']]
#new["Motor_g??c??"] = new["Motor_g??c??"].str.replace("hp", "")
new["Kilometre"] = new[10].str.replace('Kilometre: ', '')
new["Kilometre"] = new["Kilometre"].str.replace('.', '', regex=True)
new["Kilometre"] = new["Kilometre"].str.replace("km", "")
#new["Kilometre"] = new["Kilometre"].str.replace(",", ".")
new["Boya-de??i??en"] = new[11].str.replace('Boya-de??i??en: ', '')
new["Konum"]=loc[0]
#print(df["Fiyat"])
new["Fiyat"] = df["Fiyat"].str.replace(".", "",regex=True)
new["Fiyat"] = new["Fiyat"].str.replace("TL", "")
new["Fiyat"] = new["Fiyat"].str.replace(" ", "")
#new["Kilometre"] = new["Kilometre"].str.replace('.', '')

new.drop(columns=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14], axis=1, inplace=True)
#new
print(new["Konum"].get(1))
new.to_csv('cities.csv')

"""
#df = pd.read_csv('cities.csv')
city_list = new["Konum"].unique()
marka_list = new["Marka"].unique()
seri_list = new["Seri"].unique()

cond = new['Konum']=="Ankara" and new['Marka']=="Ford" and new['Seri']=="Focus"

mean_of_car = new[cond]

out = pd.to_numeric(mean_of_car['Fiyat'], errors='coerce').mean()
print(out)
"""
