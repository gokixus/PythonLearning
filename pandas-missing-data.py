import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)
df = pd.DataFrame(data, index=["A", "C", "E", "F", "H"], columns=["Column1", "Column2", "Column3"])
df = df.reindex(["A","B","C","D","E","F","G","H"])
print(df)
print(df.drop("Column1", axis= 1))
print(df.drop("A", axis= 0))
print(df.drop(["A","B","H"], axis= 0))
print(df.isnull())
print(df.notnull())
print(df.isnull().sum())
print(df["Column1"].isnull().sum())

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["Column4"] = newColumn
print(df)
print(df[df["Column1"].isnull()])

print(df.dropna())
print(df.dropna(axis=1))

