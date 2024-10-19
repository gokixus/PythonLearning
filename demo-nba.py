import pandas as pd

df = pd.read_csv("datasets/nba.csv")

# 1- İlk 10 kaydı getiriniz.
print(df.head(10))

# 2- Toplam kaç kayıt var ?
print(f"Toplam kayit = {len(df.index)}")

# 3- Tüm oyuncuların toplam maaş ortalaması?
print(f"Tüm oyuncuların toplam maaş ortalaması = {df["Salary"].mean()}")

# 4- En yüksek maaşı ne ?
print(f"En yüksek maaş = {df["Salary"].mean()}")

# 5- En yüksek maaşı alan oyuncu kim?
print(f"En yüksek maaşı alan oyuncu = {df[df["Salary"]==df["Salary"].max()]["Name"].iloc[0]}")

# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımı azalan şekilde sıralı
print(df[(df["Age"] >= 20) & (df["Age"] < 25)][["Name", "Team", "Age"]].sort_values("Age", ascending=False))

# 7- john holland isimli oyuncunun oynadığı takım ?
print(df[df["Name"] == "John Holland"]["Team"].iloc[0])

# 8- Takımlara göre oyuncuların ortalama maaş bilgisi
print(df.groupby("Team")["Salary"].mean())

# 9- kaç farklı tkaım mevcut ?
print(len(df.groupby("Team")))

# 10- her takımda kaç oyuncu oynamakta ?
print(df["Team"].value_counts())

# 11- ismi içinde and geçen kayıtları bulunuz.
df = df.dropna()
print(df[df["Name"].str.contains("and", case=False)])

