import pandas as pd
import numpy as np


df = pd.read_csv('cities.csv')
city_list = df["Konum"].unique()
marka_list = df["Marka"].unique()
seri_list = df["Seri"].unique()

cond = df['Konum']=="Ankara" and df['Marka']=="Ford" and df['Seri']=="Focus"

mean_of_car = df[cond]

out = pd.to_numeric(mean_of_car['Fiyat'], errors='coerce').mean()
print(out)
