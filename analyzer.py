import pandas as pd
import locale

locale.setlocale(locale.LC_ALL, 'en_US')
df = pd.read_csv('cities.csv')
city_list = df["Konum"].unique()
marka_list = df["Marka"].unique()
markalar = {}
seri_list = df["Seri"].unique()
progress = 0

for i in marka_list:
    markalar_df = df[df['Marka']==i]["Seri"].unique()
    markalar[i] = markalar_df


last = pd.DataFrame(columns =['City', 'Marka','Seri','Average Price(TL)']) 
for city in city_list:
    for marka in markalar.keys():
        for seri in markalar[marka]:

            cond = df[(df['Konum']==city) & (df['Marka']==marka) & (df['Seri']==seri)]
            
            """cond1 = df['Konum']=="ADANA "
            temp1 = df[cond1]
            print(temp1)
            cond2 = df['Marka']==marka
            temp2 = df[cond2]
            #print(temp2)
            cond3 = df['Seri']==seri
            temp3 = df[cond3]
            #print(city,marka,seri)
            print(temp3)"""
            if not cond.empty:

                mean = pd.to_numeric(cond['Fiyat'], errors='coerce').mean()
                last = last.append(dict(zip(last.columns, [city, marka, seri, int(mean)])), ignore_index=True)
                #print(cond)
                #print(last)
                progress +=1
                print(progress)

          
print(last)

last.to_csv('output.csv')
