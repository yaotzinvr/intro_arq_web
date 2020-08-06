import jwt
from datetime import timedelta
from . import config

token_semilla = config.get_variables_entorno()['token_semilla']
token_tiempo_expiracion = timedelta(hours=8)
token_tiempo_delay = timedelta(minutes=5)

def validate_token(token):
    try:
        res=jwt.decode(token, token_semilla, leeway=token_tiempo_delay, algorithms=['HS256'])
    except Exception as e:
        return {'ok': False, 'code': 401, 'msj': 'Token invalido', 'error': str(e)}
    return {'ok':True,'msj':'Token valido','payload':res['payload']}