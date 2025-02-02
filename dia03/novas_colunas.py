#%%
import pandas as pd
import numpy as np 

# %%
df = pd.read_csv("../data/customers.csv",";")
df
# %%

df["Points_double"] = df["Points"] *2
df
# %%

df["Points_ratio"] = df["Points_double"] / df["Points"]
df
# %%

df["Constante"] = 1
df
# %%
df["Points_log"] = np.log(df["Points"])
df
# %%

np.log(df[["Points","Points_double","Points_ratio"]])


# %%
df["Nome_Alta"] = df["Name"].str.upper()
df
# %%

def get_first(nome:str):
    nome = nome.upper()
    return nome.split('_')[0]

df["Primeiro_nome"] = df["Name"].apply(get_first)
df
# %%
#função lambda

get_f = lambda nome: nome.split('_')[0]

get_f("Téo")
# %%
df["Nome_f"] = df["Name"].apply(lambda x: x.split("_")[0])
df

# %%

def intervalo_pontos(pontos):
    if pontos < 2500:
        return 'baixo'
    elif pontos < 3500:
        return 'medio'
    else:
        return 'alto'
    
df["Faixa_pontos"] = df['Points'].apply(intervalo_pontos)
df
# %%
#Coluna com os 3 ultimos digitos
df["UUID_menor"] = df["UUID"].apply(lambda x: x[-3:])
df
# %%
data = {
        "nome": ["Teo", "Nah", "Maria", "Lara"],
        "recencia": [1,30,10,45],
        "valor":[100,2000, 15, 500],
        "frequencia":[2, 5, 1, 15]
}
df_crm = pd.DataFrame(data)
df_crm
# %%
def rfv(row):
    nota = 0
    
    if row['recencia'] <= 10:
        nota += 10
    elif 10 < row['recencia'] <= 30:
        nota += 5
    elif row['recencia'] > 30:
        nota += 0

    if row['valor'] > 1000:
        nota += 10
    elif 100 <= row['valor'] <= 1000:
        nota += 5
    elif row['valor'] < 100:
        nota +=0

    if row['frequencia'] > 10:
        nota += 10
    elif 5 <= row['frequencia'] < 10:
        nota +=5
    elif row['frequencia'] < 5:
        nota +=0

    return nota

df_crm["RFV"] = df_crm.apply(rfv, axis=1)
df_crm