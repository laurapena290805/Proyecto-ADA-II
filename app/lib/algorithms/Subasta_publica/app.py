from flask import Flask, request, jsonify
from dinamica import subasta_dp
from fuerza_bruta import subasta_fuerza_bruta
from voraz import subasta_voraz

app = Flask(__name__)

@app.route('/run_algorithm', methods=['POST'])
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

if __name__ == '__main__':
    app.run(debug=True)
