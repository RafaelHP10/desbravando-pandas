#%%
import pandas as pd

df = pd.read_csv("../data/customers.csv",sep=";")

# %%
df.sort_values(by=["Points","Name"], ascending=[False,True]).tail(10)
# %%
df = (df.sort_values(by=["Points","Name"],
                        ascending=[False,True])
                        .tail(10))
df