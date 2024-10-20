from flask import Flask, request, jsonify
from fuerza_bruta import terminal_fuerza_bruta
from dinamica import terminal_dinamica
from voraz import terminal_voraz

#Servidor para terminal_inteligenteUI para ejecutar el algoritmo de fuerza bruta

app = Flask(__name__)

@app.route('/run_algorithmT', methods=['POST'])
def run_algorithmT():
    data = request.json
    A = data['A']
    D = data['D']
    R = data['R']
    I = data['I']
    K = data['K']
    cadenaX = data['cadenaX']
    cadenaY = data['cadenaY']
    algoritmo = data['algoritmo']
    
    if algoritmo == 'dinamica':
        costo,operaciones = terminal_dinamica(A, D, R, I, K, cadenaX, cadenaY)
    elif algoritmo == 'fuerza_bruta':
        costo,operaciones = terminal_fuerza_bruta(A, D, R, I, K, cadenaX, cadenaY)
    elif algoritmo == 'voraz':
        costo,operaciones = terminal_voraz(A, D, R, I, K, cadenaX, cadenaY)
    
    return jsonify({'costo': costo, 'operaciones': operaciones})

if __name__ == '__main__':
    app.run(debug=True)
