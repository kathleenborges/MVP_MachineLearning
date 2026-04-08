from flask import Flask, request, jsonify, send_from_directory
from classes import InteligenciaVinho # Certifique-se que classes.py está na mesma pasta
from flask_cors import CORS 
import os

app = Flask(__name__, 
            static_folder='../frontend', 
            static_url_path='/static')
CORS(app) # Permite que o frontend acesse a API sem problemas de CORS

current_dir = os.path.dirname(os.path.abspath(__file__))
path_modelo = os.path.join(current_dir, 'modelo_rf_final.pkl') 
path_scaler = os.path.join(current_dir, 'scaler_rf.pkl') 

try:
    IA = InteligenciaVinho(
        path_model=path_modelo,
        path_scaler=path_scaler
    )
    print("✅ Modelo e Scaler carregados com sucesso!")
except Exception as e:
    print(f"❌ Erro ao carregar modelo: {e}")


@app.route('/')
def home():
    # Enviando o arquivo index.html que está dentro da pasta frontend
    return send_from_directory(app.static_folder, 'index.html')

# Rota para que o Flask encontre o style.css e script.js
@app.route('/<path:path>')
def send_static(path):
    return send_from_directory(app.static_folder, path)

@app.route('/prever', methods=['POST'])
def rota_previsao():
    try:
        dados = request.get_json()
        
        # 'features' deve ser uma lista com os 11 atributos enviada pelo Front/Postman
        resultado = IA.predizer(dados['features'])
        
        return jsonify(resultado), 200
    
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)