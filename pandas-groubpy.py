import pandas as pd
import numpy as np

personeller = {
    "Çalışan": ["Ahmet Yılmaz", "Can Ertürk", "Hasan Korkmaz", "Cenk Saymaz", "Ali Furkan", "Gökdeniz Yılmaz"],
    "Departman": ["İnsan Kaynakları", "Bilgi İşlem", "Muhasebe", "İnsan Kaynakları", "Bilgi İşlem", "Muhasebe"],
    "Yaş": [30,25,45,50,23,21],
    "Semt": ["Kadıköy", "Tuzla", "Maltepe", "Tuzla", "Maltepe", "Tuzla"],
    "Maaş": [5000, 3000, 4000, 3500, 2850, 6500]  
}

df = pd.DataFrame(personeller)
print(df)
print(df["Maaş"].sum())
print(df.groupby("Departman"))
print(df.groupby("Departman").groups)


for name, group in df.groupby("Semt"):
    print(name)
    print(group)
    

print(df.groupby("Semt").get_group("Kadıköy"))
print(df.groupby("Semt")["Yaş"].max())
print(df.groupby("Semt")["Çalışan"].count())
print(df.groupby("Departman")["Maaş"].max()["Muhasebe"])
print( df.groupby("Departman")[["Yaş", "Maaş"]].agg(np.mean))


