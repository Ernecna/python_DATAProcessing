import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")

def grab_col_names(dataframe, cat_th=10, car_th=20):
       """
       Veri setindeki kategorik, numerik ve kategorik fakat kordinal değişkenlerin isimlerini verir.
       Parameters
       ----------
       dataframe : dataframe
              değişken isimleri alınmak istenen dataframedir.
       cat_th : int, float
              numerik fakat kategorik olan değişkenle riçin sınıf eşik değeri
       car_th : int, float
              kategorik fakat kardinal değişkenler için sınıf eşik değeri
       Returns
       -------
        cat_cols: list
              Kategorik değişken listesi
       num_cols: list
              Numerik değişken listesi
       cat_but_car : list
              Kategorik görünümlü kardinal değişken listesi
       """
       # Kategorik değişkenleri yakala
       cat_cols = [col for col in df.columns if df[col].dtype in ["category", "object", "bool"]]

       # Aslında kategorik ama numeric olanları yakala
       num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtype in ["int64", "float64"]]

       # Kategorik ama anlamsız olanlar için ölçülemeyecek olan değişkenleri bulmak için kullanırız.
       cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and df[col].dtype in ["category", "object"]]

       # Kategorikleri ve num_but_cat olanları birbirlerine ekleyelim
       cat_cols = cat_cols + num_but_cat

       # Eğer cat_but_car listesinde cardinalitesi yüksek bir değişken varsa bunları çıkaralım
       cat_cols = [col for col in cat_cols if col not in cat_but_car]

       num_cols = [col for col in df.columns if df[col].dtypes in ["float64", "int64"]]

       num_cols = [col for col in num_cols if col not in cat_cols]

       print(f"Observations {dataframe.shape[0]}")
       print(f"Variables {dataframe.shape[1]}")
       print(f"catcols {len(cat_cols)}")
       print(f"numcols {len(num_cols)}")
       print(f"cat_but_car {len(cat_but_car)}")
       print(f"cat_but_car {len(num_but_cat)}")

       return  cat_cols,num_cols,cat_but_car


print(grab_col_names(df))
#çıktıları tutmak için
cat_cols, num_cols, cat_but_car =grab_col_names(df)

## daha önceden yazdığımız cat summary ve num summary fonksyonlarıyla birlikte bunları kullanıyoruz.
