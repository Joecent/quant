import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://Joe:sjjgtjytz@localhost:3306/quant')
sql_query = 'select * from user;'
df_read = pd.read_sql_query(sql_query, engine)
test = df_read.to_json(orient='records')
print(test)