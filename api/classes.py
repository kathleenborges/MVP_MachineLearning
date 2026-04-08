import numpy as np
from joblib import load

class InteligenciaVinho:
    def __init__(self, path_model, path_scaler):
        # O modelo é carregado uma única vez ao iniciar o servidor
        self.modelo = load(path_model)
        self.scaler = load(path_scaler)

    def predizer(self, dados_lista):
        # Converte a lista recebida da API para o formato do modelo
        X_input = np.array(dados_lista).reshape(1, -1)
        X_scaled = self.scaler.transform(X_input)
        
        nota = self.modelo.predict(X_scaled)[0]
        probabilidade = self.modelo.predict_proba(X_scaled).max() # Bônus: confiança do modelo
        
        return {
            "nota": int(nota),
            "confianca": round(float(probabilidade) * 100, 2),
            "status": "Alta Qualidade" if nota >= 7 else "Qualidade Padrão"
        }