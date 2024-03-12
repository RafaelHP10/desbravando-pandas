#%%
import pandas as pd



# %%

idades = [30, 42, 90, 34]

idades


# %%
"""Calculo de média"""
media = sum(idades) / len(idades)
media

# %%
"""Calculo de variancia"""
total = 0

for i in idades:
    total += (media - i)**2

variancia = total / (len(idades) - 1)

variancia



# %%
"""Transformando a lista em series do pandas"""
series_idades = pd.Series(idades)

#Média do pandas
series_idades.mean()

#Variancia do pandas
series_idades.var()

#Variancia do pandas
series_idades.median()

#Descrição do pandas
series_idades.describe()


series_idades.shape

##colocando indice na tupla
series_idades.index = ['t','e','o','c']

##Pegando o valor da celula pelo indice
series_idades['c']

##Alterando novamente o indice
series_idades.index = [40,10,30,20]

##Buscando o valor pelo indice novo
series_idades[30]

##Buscando o valor pelo primeiro indice indpendente do nome do indice
#Do primeiro ao ultimo
series_idades.iloc[0:series_idades.count()]

##Buscando o valor pelo nome do indice
series_idades.loc[40]
# %%

series_idades.name = 'idades'

series_idades


# %%

series_idades = pd.Series(idades, name='idades')
series_idades