import pandas as pd
import numpy as np

data = {
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,20,25],
    "Column3": ["abc", "bca", "ade", "cba", "dea"]
}

df = pd.DataFrame(data)
print(df)
print(df["Column2"].unique())
print(df["Column2"].nunique())
print(df["Column2"].value_counts())

def kareAl(x):
    return x*x

kareAl2 = lambda x: x*x

print(df["Column2"].apply(kareAl))
print(df["Column2"].apply(kareAl2))
print(df["Column2"].apply(len))



