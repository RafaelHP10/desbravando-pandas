#%%
import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")

df
# %%
df.shape
# %%

df.head(5)
# %%
df.tail(5)
# %%
colunas = ["UUID",
           "Points",
           "IdCustomer",
           "DtTransaction"]

df = df[colunas]

df
# %%

df.info(memory_usage='deep')