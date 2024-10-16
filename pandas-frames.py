import pandas as pd

s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,7,2])

data = dict(apples = s1, oranges = s2)

df1 = pd.DataFrame(data)
print(df1)

df2 = pd.DataFrame([["Ahmet", 50], ["Ali", 60], ["Yağmur", 70], ["Çınar", 80]])
print(df2)

data2 = [["Ahmet", 50], ["Ali", 60], ["Yağmur", 70], ["Çınar", 80]]
df3 = pd.DataFrame(data2, index=[1,2,3,4], columns=["Name", "Grade"])
print(df3)

data3 = {"Name": ["Ahmet", "Ali", "Yağmur", "Çınar"], "Grade": [50, 60, 70, 80]}
df4 = pd.DataFrame(data3, index=["212", "232", "236", "456"])
print(df4)