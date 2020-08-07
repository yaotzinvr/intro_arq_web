from datetime import timedelta,datetime
import jwt
import pandas as pd
import pymongo
from sqlalchemy import create_engine
from . import config
from . import authorization

cadena_postgresql = config.get_variables_entorno()['cadena_postgresql']
cadena_mongo = config.get_variables_entorno()['cadena_mongo']

token_semilla = config.get_variables_entorno()['token_semilla']
token_tiempo_expiracion = timedelta(hours=8)
token_tiempo_delay = timedelta(minutes=5)

def one(id,token):
    try:
        res = authorization.validate_token(token)
        if not res['ok']: return res

        client = pymongo.MongoClient(cadena_mongo)
        p = client.pokemones.pokemon.find_one({"id": id})
        p['_id'] = str(p['_id'])
    except Exception as e:
        return {'ok': False, 'code':504, 'msj': 'Error al conectarse con Mongo', 'error':str(e)}
    return {'ok':True,'pokemon':p}


def all(token):
    print(cadena_postgresql)
    try:
        res = authorization.validate_token(token)
        if not res['ok']: return res

        engine = create_engine(cadena_postgresql)
        df = pd.read_sql_query('select * from pokemon', con=engine)
    except Exception as e:
        return {'ok': False, 'code':504, 'msj': 'Error al conectarse con Elephant', 'error':str(e)}
    return {'ok':True, 'pokemones':df.to_dict('records')}

def find(filters,token):
    res = authorization.validate_token(token)
    if not res['ok']: return res

    client = pymongo.MongoClient(cadena_mongo)
    res = client.pokemones.pokemon.find(filters)
    ps = []
    for r in res: ps.append(r)
    for p in ps:  p['_id'] = str(p['_id'])
    return {'ok': True, 'pokemones': ps}


def login(usuario,password):
    print(token_semilla)
    try:
        if usuario not in ['yao','admin']:
            return {'ok': False, 'code': 400, 'msj': 'Usuario no existe'}
        if password != 'password_yao':
            return {'ok': False, 'code': 400, 'msj': 'Contraseña incorrecta'}
        token = jwt.encode({'payload':
                                {'nombre': 'Yaotzin',
                                 'usuario': 'yao',
                                 'correo': 'yaotinvr@gmail.com',
                                 'id' : 5
                                 },
                            'exp': datetime.utcnow() + token_tiempo_expiracion}, token_semilla, algorithm='HS256')
    except Exception as e:
        return {'ok': False, 'code': 500, 'msj': 'Error en el metodo login', 'error': str(e)}
    return {'ok': True, 'token': token.decode('utf-8')}


