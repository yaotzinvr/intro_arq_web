import flask
from pokemon import service as pokemon_service

app = flask.Flask(__name__)

@app.route('/pokemon/all', methods=['POST'])
def all():
    args = {}
    for x in ['token']:
        args[x] = flask.request.get_json()[x] if flask.request.get_json() else flask.request.args[x]
    r = pokemon_service.all(**args)
    if not r['ok']: return flask.jsonify(r), r['code']
    return r

@app.route('/pokemon/<int:id>/<string:token>', methods=['GET'])
def one(id,token):
    r = pokemon_service.one(id,token)
    if not r['ok']: return flask.jsonify(r), r['code']
    return r

@app.route('/pokemon/find', methods=['POST'])
def find():
    args = {}
    for x in ['filters','token']:
        args[x] = flask.request.get_json()[x] if flask.request.get_json() else flask.request.args[x]
    r = pokemon_service.find(**args)
    if not r['ok']: return flask.jsonify(r), r['code']
    return r

@app.route('/pokemon/login', methods=['POST'])
def login():
    args = {}
    for x in ['usuario','password']:
        args[x] = flask.request.get_json()[x] if flask.request.get_json() else flask.request.args[x]
    r = pokemon_service.login(**args)
    if not r['ok']: return flask.jsonify(r), r['code']
    return r


@app.route('/', methods=['GET'])
def home():
    return 'OK'

if __name__=='__main__':
    app.run(host='0.0.0.0',
            port=8082,
            debug=True,
            )
