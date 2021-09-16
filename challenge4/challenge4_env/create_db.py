import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy.types as types
import os

os.chdir(os.path.dirname(__file__))
engine = create_engine('sqlite:///./data/database.db', echo=False)

df = pd.DataFrame(columns=['DRE','Curso','Nome','Gênero','Data de Nascimento','Altura','Peso','CRA','Créditos Obtidos','Renda'])

df.to_sql('students', con=engine, if_exists='replace',index = False, dtype={
    'DRE' : types.Integer(),
    'Curso' : types.String(),
    'Nome' : types.String(),
    'Gênero' : types.String(),
    'Data de Nascimento' : types.Date(),
    'Altura' : types.Float(),
    'Peso' : types.Float(),
    'CRA': types.Float(),
    'Créditos Obtidos' : types.Float(),
    'Renda' : types.Float()
})
