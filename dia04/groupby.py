#%%
import pandas as pd
import datetime

df = pd.read_excel("../data/transactions.xlsx")
df
# %%
#Somando os pontos de 1 usuario em especifico
condicao = df["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df_user = df[condicao]
df_user["Points"].sum()
# %%
df_sumary = df.groupby(["IdCustomer"])["Points"].sum()
df_sumary.reset_index()
# %%
(df.groupby(["IdCustomer"])
    .agg({"Points":'sum',
          "UUID":'count',
          "DtTransaction":'max',
          })
    .reset_index()
    .rename(columns= {
            "Points":'Valor',
            "UUID":'Frequencia',
            "DtTransaction":"UltimaData"

            })
)
# %%
data1 = df["DtTransaction"][0]

now = datetime.datetime.now()
now
diference = now - data1
diference.days
# %%
condicao = df["IdCustomer"] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df_user = df[condicao]

def recencia(x):
    diff = datetime.datetime.now() - x.max()
    return diff.days

(df.groupby(["IdCustomer"])
    .agg({"Points":'sum',
          "UUID":'count',
          "DtTransaction": recencia,
          })
    .reset_index()
    .rename(columns= {
            "Points":'Valor',
            "UUID":'Frequencia',
            "DtTransaction":"Recencia"

            })
)