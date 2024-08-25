import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df=pd.read_excel("miuul_gezinomi.xlsx")
df.head()

## unique değerler ve frekansları

df["SaleCityName"].nunique()
df["SaleCityName"].value_counts()

## unique concept
df["ConceptName"].unique()
## hangi konseptten kaç satış gerçekleşmiş
df["ConceptName"].value_counts()

## şehirlere göre satışlardan toplam ne kadar kazanıldı ?
## Şehir kırılımına göre dediği için  şehiri alıyoruz onunla gropu by yapıyoruz.
df.groupby("SaleCityName").agg({"Price":"sum"})

## concept türlerine göre kazanç
df.groupby("ConceptName").agg({"Price":"sum"})
## şehirlere göre price ortalaması
df.groupby("SaleCityName").agg({"Price":"mean"})
## conceptlere göre price ortalaması
df.groupby("ConceptName").agg({"Price":"mean"})
## Şehir konsept kırılımında    price ortalamaları nedir
df.groupby(["SaleCityName","ConceptName"]).agg({"Price":"mean"})

## 2
## satis_checkin_day_diff  değişkenini  EB_score adında yeni bir kategorik değişkene çevirmeliyiz.
bins=[-1,7,30,90,df["SaleCheckInDayDiff"].max()]
labels=["Last Minuters","Potential Planners","Planners","Early Bookers"]

df["EB_Score"]=pd.cut(df["SaleCheckInDayDiff"], bins=bins, labels=labels)
df.head(50).to_excel("eb_scorew.xlsx",index=False)

