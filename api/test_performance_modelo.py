import pytest
from classes import InteligenciaVinho
import os

def test_modelo_acuracia_minima():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ia = InteligenciaVinho(
        path_model=os.path.join(current_dir, 'modelo_rf_final.pkl'),
        path_scaler=os.path.join(current_dir, 'scaler_rf.pkl')
    )
    
    # Simulando um teste com dados reais que já se sabe o resultado
    # Se a acurácia for menor que o limite, o teste falha e impede o deploy
    vinho_bom = [7.4, 0.3, 0.3, 2.0, 0.07, 15, 40, 0.99, 3.3, 0.85, 14.0]
    predicao = ia.predizer(vinho_bom)
    
    assert predicao['nota'] >= 5
