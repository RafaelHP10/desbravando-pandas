#%%
import pandas as pd
# %%

data = {
    'nome':['teo','nah','lara','maria'],
    'sobrenome':['calvo','ataide','calvo','calvo'],
    'idade':[31,32,31,2]
}

# %%
data['idade'][0]

# %%
df = pd.DataFrame(data)
df

# %%
df['idade']

# %%
df['idade'].iloc[0]

# %%
df.iloc[0]

df.columns

df.info(memory_usage='deep')

df.dtypes

df.describe

# %%
df['peso'] = [80,53,65,14]

sumario = df.describe()
print(sumario)
sumario['peso']['mean']

# %%
#Top 2 da serie
df.head(2)

#As 2 ultimas da serei
df.tail(2)