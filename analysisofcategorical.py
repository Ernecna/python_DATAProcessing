import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")

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

# Şu anda buradaki tüm değişkenler kategorik değişkenlerdir
print(df[cat_cols].head())

# Doğrulamak için
print(df[cat_cols].nunique())

# Fonksiyon haline getirmek
def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))

# Örnek olarak 'sex' sütunu için özet çıktısı
cat_summary(df, "sex")

# Tüm kategorik sütunlar için özet çıktısı
for col in cat_cols:
    cat_summary(df, col)
