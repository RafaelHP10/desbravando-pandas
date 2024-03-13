#%%

import pandas as pd

df_customers    = pd.read_csv("../data/customers.csv",sep=";")

df_customers

df_customers.info(memory_usage='deep')

df_customers['Points'].describe()

# %%

notas = [4.5,6,7,3.5]
for i in notas:
    if i > 5:
        print(i)

# %%

notas_novas = []

for i in notas:
    notas_novas.append(i+1)

notas_novas

# %%
#Apenas os registros com mais de 1000 pontos
condicao = df_customers['Points'] > 1000
#Filtrando apenas os registros com mais de 1000 pontos
df_customers[condicao]
# %%

#filtrando o maior registro
condicao_maior = df_customers['Points'] == df_customers['Points'].max()
def_maior = df_customers[condicao_maior]
def_maior['Name'].iloc[0]

# %%
#modo grande e não muito legal de fazer igual ao de cima
df_customers[df_customers['Points'] == df_customers['Points'].max()]['Name'].iloc[0]

# %%
#Fazendo copia do dataframe para poder alterar os dados
range = df_customers['Points'].between(1000,2000)
df_novo = df_customers[range].copy()
df_novo['Points'] = df_novo['Points'] + 1000
df_novo['Points']
# %%
df_customers[["UUID","Name"]]

colunas = df_customers.columns.tolist()
colunas.sort()

df_customers = df_customers[colunas]
df_customers
# %%
#Renomear as colunas 
df_customers = df_customers.rename(columns={"Name":"Nome",
                             "Points":"Pontos"})

df_customers
# %%
#Renomear as colunas 
df_customers.rename(columns={"ID_USUARIO":"ID"}, inplace=True)
df_customers