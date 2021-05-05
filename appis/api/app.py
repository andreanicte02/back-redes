from flask import Flask, request
from flask_cors import CORS
import simplejson as json
import requests

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origin": "*"}})
urlListaIdEvento = "http://localhost:5000/ListarIdEvento"
urlAgregarUsuario = "http://localhost:5000/AgregarUsuario"
urlListarPorCarnet = "http://localhost:5000/ListarPorCarnet"

@app.route('/', methods=['GET'])
def check():
    return 'hola perros'

@app.route('/AgregarUsuario', methods=['POST'])
def AgregarUsuario():
    content = request.get_json()
    r = requests.post(urlAgregarUsuario, json=content)
    print(r.status_code)
    if r == None:
        return "Record not found", 400

    return r.text, 200



@app.route('/ListarIdEvento', methods=['POST'])
def ListarIdEvento():
    content = request.get_json()
    print(content)
    r = requests.get(urlListaIdEvento, json={'idEvento': content['idEvento']})

    if r == None:
        return "Record not found", 400

    return json.dumps(r.json(), 200)

@app.route('/ListarPorCarnet', methods=['POST'])
def ListarPorCarnet():
    content = request.get_json()
    print(content)
    r = requests.get(urlListarPorCarnet, json={'carnet': content['carnet']})

    if r == None:
        return "Record not found", 400

    return json.dumps(r.json(), 200)



if __name__ == '__main__':

    #print(db.registrarEsistencia(2000,"abc",'congresos','1','akjñklaslkdf'))
    app.run(host='0.0.0.0', port=5002, threaded=True, use_reloader=True)
