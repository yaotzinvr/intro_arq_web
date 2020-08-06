import os

def get_variables_entorno():
    return {
        'token_semilla': os.environ['TOKEN_SEMILLA'] if 'TOKEN_SEMILLA' in os.environ else 'semilla_prueba',
        'cadena_mongo': 'mongodb+srv://admin:toor@cluster0-uzjjh.mongodb.net/pokemones?retryWrites=true&w=majority',
        'cadena_postgresql' :'postgres://' +
            (os.environ['USER_POSTGRES'] if 'USER_POSTGRES' in os.environ else 'postgres')
                                                                              + ':' +
            (os.environ['PASS_POSTGRES'] if 'PASS_POSTGRES' in os.environ else 'toor')
                                                                              + '@' +
            (os.environ['HOST_POSTGRES'] if 'HOST_POSTGRES' in os.environ else 'localhost')
                                                                              + ':' +
            (os.environ['PORT_POSTGRES'] if 'PORT_POSTGRES' in os.environ else '5432')
                                                                              + '/' +
            (os.environ['DB_POSTGRES'] if 'DB_POSTGRES' in os.environ else 'postgres')
    }