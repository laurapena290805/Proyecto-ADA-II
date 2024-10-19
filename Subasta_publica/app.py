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
    
    valor_final, mejor_asignacion = subasta_dp(A, B, n, ofertas)
    
    return jsonify({
        'valor_final': valor_final,
        'mejor_asignacion': mejor_asignacion
    })

if __name__ == '__main__':
    app.run(debug=True)
