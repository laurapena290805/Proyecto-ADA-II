from flask import Flask, request, jsonify
from flask_cors import CORS

from Subasta_publica.dinamica import subasta_dp
from Subasta_publica.fuerza_bruta import subasta_fuerza_bruta
from Subasta_publica.voraz import subasta_voraz
from Terminal_inteligente.dinamica import terminal_inteligente_dp
from Terminal_inteligente.fuerza_bruta import terminal_fuerza_bruta
from Terminal_inteligente.voraz import terminal_inteligente_voraz



app = Flask(__name__, static_folder='web', static_url_path='/')


CORS(app)

@app.route('/')
def index():
    return  app.send_static_file('index.html')



@app.route('/subasta', methods=['POST'])
def run_algorithm():
    data = request.json
    A = data['A']
    B = data['B']
    n = data['n']
    ofertas = data['ofertas']
    algoritmo = data['algoritmo']

    if algoritmo == 'dinamica':
        resultado, asignacion = subasta_dp(A, B, n, ofertas)
    elif algoritmo == 'fuerza_bruta':
        resultado, asignacion = subasta_fuerza_bruta(A, B, n, ofertas)
    elif algoritmo == 'voraz':
        resultado, asignacion = subasta_voraz(A, B, n, ofertas)
    else:
        return jsonify({'error': 'Algoritmo no válido'}), 400 
    return jsonify({'resultado': resultado, 'asignacion': asignacion})



@app.route('/terminal', methods=['POST'])
def run_algorithmT():
    data = request.json
    print(data)
    A = data['A']
    D = data['D']
    R = data['R']
    I = data['I']
    K = data['K']
    cadenaX = data['cadenaX']
    cadenaY = data['cadenaY']
    algoritmo = data['algoritmo']
    
    if algoritmo == 'dinamica':
        costo,operaciones = terminal_inteligente_dp(A, D, R, I, K, cadenaX, cadenaY)
    elif algoritmo == 'fuerza_bruta':
        costo,operaciones = terminal_fuerza_bruta(A, D, R, I, K, cadenaX, cadenaY)
    elif algoritmo == 'voraz':
        costo,operaciones = terminal_inteligente_voraz(A, D, R, I, K, cadenaX, cadenaY)
    return jsonify({'costo': costo, 'operaciones': operaciones})


if __name__ == '__main__':
    app.run(debug=True)