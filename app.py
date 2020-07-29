import flask
from pokemon import service as pokemon_service

app = flask.Flask(__name__)

@app.route('/pokemon/all', methods=['GET'])
def all():
    r = pokemon_service.all()
    if not r['ok']: return flask.jsonify(r), r['code']
    return r

@app.route('/pokemon/<int:id>', methods=['GET'])
def one(id):
    r = pokemon_service.one(id)
    if not r['ok']: return flask.jsonify(r), r['code']
    return r

@app.route('/pokemon/find', methods=['POST'])
def find():
    args = {}
    for x in ['filters']:
        args[x] = flask.request.get_json()[x] if flask.request.get_json() else flask.request.args[x]
    r = pokemon_service.find(**args)
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
