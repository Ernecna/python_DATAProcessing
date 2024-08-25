import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Veri setini yükleme
df = pd.read_csv("breast_cancer.csv")
df = df.iloc[:, 1:-1]  # İlk ve son sütunu çıkardınız, kontrol edin.

# Sayısal sütunları tespit et
num_cols = [col for col in df.columns if df[col].dtype in ["int64", "float64"]]

# Sayısal olmayan sütunları çıkar
df = df[num_cols]

# Korelasyon matrisini hesaplama
corr = df.corr()

# Isı haritası
sns.set(rc={'figure.figsize': (12, 12)})
sns.heatmap(corr, cmap="RdBu", annot=True)  # annot=True ile korelasyon değerlerini göster
plt.show()

## YÜKSEK KORELASYONLULARIN SİLİNMESİ
# Korelasyon matrisi
cor_matrix = df.corr().abs()

# Üst üçgensel matrisi al (kendi kendine korelasyonu önlemek için)
upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))

# Eşik değerine göre yüksek korelasyonlu sütunları tespit et (örn: 0.8)
threshold = 0.9
to_drop = [column for column in upper_triangle_matrix.columns if any(upper_triangle_matrix[column] > threshold)]

# Yüksek korelasyonlu sütunları çıkar
df.drop(to_drop, axis=1, inplace=True)


def high_correlated_cols(dataframe, plot=False, corr_th=0.90):
    corr=dataframe.corr()
    cor_matrix=corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))
    to_drop = [column for column in upper_triangle_matrix.columns if any(upper_triangle_matrix[column] > threshold)]
    if plot:
        import  seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={'figure.figsize': (15, 15)})
        sns.heatmap(corr,cmap="RdBu")
        plt.show()
        return to_drop
