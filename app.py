from flask import Flask, request, jsonify, render_template
import pandas as pd
import os

app = Flask(__name__)


def carregar_dados():
    # Simulando uma base de dados com um arquivo CSV (substituir pelo caminho correto)
    return pd.read_csv('status_veiculos.csv')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/consulta', methods=['GET'])
def consulta():
    placa = request.args.get('placa')
    if not placa:
        return jsonify({'erro': 'Placa não informada'}), 400

    df = carregar_dados()
    resultado = df[df['Placa'] == placa.upper()]

    if resultado.empty:
        return jsonify({'status': 'Veículo não encontrado'}), 404

    status = resultado.iloc[0]['Status']
    return jsonify({'placa': placa, 'status': status})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))