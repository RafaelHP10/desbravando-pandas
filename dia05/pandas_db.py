#%%
import pandas as pd
import sqlalchemy
# %%

engine = sqlalchemy.create_engine("sqlite:///../data/database.db")
# %%
transaction_cart = pd.read_sql_table("transactions_cart", engine)
transaction_cart
# %%

query = '''
select *
  from customers as t1
  left join transactions as t2
    on t1.UUID = t2.IdCustomer
    limit 10'''
df_customers = pd.read_sql_query(query,engine)
df_customers
# %%
data_01 = {
    "id":[1,2,3,4],
    "nome":["teo","mat","nah","mah"],
    "idade":[31,31,32,32]
}
df_01 = pd.DataFrame(data_01)
df_01
# %%

data_02 = {
    "id": [5,6,7,8],
    "nome":["jose","nathan","arnaldo","mario"],
    "idade":[23,33,19,21]
}
df_02 = pd.DataFrame(data_02)
df_02
# %%
df_01.to_sql("tb_df",engine,index=False)
# %%
df_02.to_sql("tb_df",engine, index=False, if_exists='append')
# %%
pd.read_sql("tb_df",engine)