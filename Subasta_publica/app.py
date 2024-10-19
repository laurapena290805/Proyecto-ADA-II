from flask import Flask, request, jsonify
import numpy as np
from dinamica import subasta_dp
from fuerza_bruta import subasta_fuerza_bruta
from voraz import subasta_voraz

app = Flask(__name__)

@app.route('/subasta', methods=['POST'])
def run_subasta():
    data = request.json
    A = data['A']
    B = data['B']
    n = data['n']
    ofertas = data['ofertas']
    algoritmoSelec = data['algoritmo']

    if algoritmoSelec == 'fuerza_bruta':
        valor_final, mejor_asignacion = subasta_fuerza_bruta(A, B, n, ofertas)
    elif algoritmoSelec == 'dinamica':
        valor_final, mejor_asignacion = subasta_dp(A, B, n, ofertas)
    elif algoritmoSelec == 'voraz':
        valor_final, mejor_asignacion = subasta_voraz(A, B, n, ofertas)
    else:
        return jsonify({
            'error': 'Algoritmo no válido'
        }), 400
    
    return jsonify({
        'valor_final': valor_final,
        'mejor_asignacion': mejor_asignacion
    })

if __name__ == '__main__':
    app.run(debug=True)
