import pandas as pd
import numpy as np
df = pd.read_csv("datasets/imdb.csv")

# 1- Dosya hakkındaki bilgiler
print(df)
print(df.columns)

# 2- İlk 5 kaydı gösterin
print(df.head())

# 3- İlk 10 kaydı gösterin
print(df.head(10))

# 4- Son 5 kaydı gösterin
print(df.tail())

# 5- Son 10 kaydı gösterin
print(df.tail(10))

# 6- Sadece Movie_Title kolonunu alın.
print(df.Movie_Title)
 
# 7- Sadece Movie_Title kolonunu içeren ilk 5 kaydı alın.
print(df[["Movie_Title"]].head())

# 8- Sadece Movie_Title ve Rating kolonunu içeren ilk 5 kaydı alın.
print(df[["Movie_Title", "Rating"]].head())

# 9- Sadece Movie_Title ve Rating kolonunu içeren son 7 kaydı alın.
print(df[["Movie_Title", "Rating"]].tail(7))

# 10- Sadece Movie_Title ve Rating kolonunu içeren ikinci 5 kaydını alın.
print(df[5:10][["Movie_Title", "Rating"]].head())

# 11- Sadece Movie_Title ve Rating kolonunu içeren ve imdb puanı 8.0 ve üstünde
# olan kayıtlardan ilk 50 tanesini alınız.
print(df.query("Rating >= 8.0")[["Movie_Title", "Rating"]].head(50))

# 12- Yayın tarihi 2014 ile 2015 arasında olan filmlerin isimlerini getiriniz.
print(df.query("YR_Released >= 2014 & 2015 >= YR_Released")[["Movie_Title", "YR_Released"]])

# 13- Değerlendirme sayısı(Num_Reviews) 100.000 den büyük ya da imdb puanı 8 ile 9
# arasında olan filmleri listeleyinz.
print(df.query("Num_Reviews > 100000 | (Rating >= 8 & 9 >= Rating)")[["Movie_Title"]])

