import psycopg2
import pandas as pd
import pymongo
from sqlalchemy import create_engine

cadena_postgresql = 'postgres://euokdekd:w_e5e-bVjrvUIMsU_Q1sTPwh3eROJQTy@ruby.db.elephantsql.com:5432/euokdekd'
cadena_mongo = 'mongodb+srv://admin:toor@cluster0-uzjjh.mongodb.net/pokemones?retryWrites=true&w=majority'

def one(id):
    try:
        client = pymongo.MongoClient(cadena_mongo)
        p = client.pokemones.pokemon.find_one({"id": id})
        p['_id'] = str(p['_id'])
    except Exception as e:
        return {'ok': False, 'code':504, 'msj': 'Error al conectarse con Mongo', 'error':str(e)}
    return {'ok':True,'pokemon':p}


def all():
    try:
        engine = create_engine(cadena_postgresql)
        df = pd.read_sql_query('select * from pokemon', con=engine)
    except Exception as e:
        return {'ok': False, 'code':504, 'msj': 'Error al conectarse con Elephant', 'error':str(e)}
    return {'ok':True, 'pokemones':df.to_dict('records')}

def find(filters):
    client = pymongo.MongoClient(cadena_mongo)
    res = client.pokemones.pokemon.find(filters)
    ps = []
    for r in res: ps.append(r)
    for p in ps:  p['_id'] = str(p['_id'])
    return {'ok': True, 'pokemones': ps}