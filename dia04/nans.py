#%%
import pandas as pd
import numpy as np

data = {
    "nome":["Téo", "Nah", "Lah", "Mah", "Jo"],
    "idade":[31,32,34,12,np.nan],
    "renda":[np.nan,3245,357,12432,np.nan],
}

df = pd.DataFrame(data)
df
# %%
#Contando os NaN
df["idade"].isna().sum()
# %%
#Contando de todos os campos do DataFrame
df.isna().sum()
# %%
df.isna().mean()
# %%
#Preencher o campo NaN com algo
df.fillna(0)
# %%
#Preencher o campo NaN com a média de outros campos
df.fillna({
          "idade":df["idade"].mean(),
          "renda":df["renda"].mean(),
})
# %%
#Dropa o registro inteiro que tem NaN
df.dropna()
# %%
#Dropa apenas se todas as colunas do registro estiver NaN
df.dropna(how='all')
# %%
#Dropa o registro inteiro se as ambas colunas selecionadas tiver NaN
df.dropna(subset=["idade","renda"],how='all')
# %%
#Dropa o registro inteiro se alguma das colunas selecionadas tiver NaN
df.dropna(subset=["idade","renda"],how='any')
# %%
#Dropa a coluna que tiver NaN
df.dropna(axis=1,how='any')
# %%
#Defini um limite de registros que não são NaN para dropar a coluna (4), caso tenha menos registros ele dropa a coluna.
df.dropna(axis=1,thresh=4)
# %%
