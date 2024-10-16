import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(3,3), index=["A", "B", "C"], columns=["Column1", "Column2", "Column3"])
print(df)
print(df["Column1"])
print(type(df["Column1"]))
print(df.loc["A"])