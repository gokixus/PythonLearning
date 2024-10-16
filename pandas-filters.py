import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns=["Colunm1","Colunm2","Colunm3","Colunm4","Colunm5"])
print(df)
print(df.columns)
print(df.head()) #ilk 5 satırı ele alır.
print(df.head(10)) #10 yazdığımız için ilk 10 satırı ele alır.
print(df.tail()) #son 5 satırı ele alır.
print(df.tail(10)) #10 yazdığımız için son 15 satırı ele alır.
print(df["Colunm4"].head())
print(df.Colunm1.head())
print(df[["Colunm1", "Colunm2"]].tail())
print(df[5:15][["Colunm1", "Colunm2"]].head()) #5-10 arasındakileri yazdırır
print(df[df["Colunm1"]> 50][["Colunm1", "Colunm2"]]) #kolon1deki 50ten büyük olan sayıları bulunan satırları yazdırır
print(df.query("Colunm1 >= 50 & Colunm1 % 2 == 0"))




