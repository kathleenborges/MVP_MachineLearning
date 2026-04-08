import pytest
from app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Testa se a página inicial carrega"""
    response = client.get('/')
    assert response.status_code == 200

def test_api_previsao_sucesso(client):
    """Testa se a rota /prever aceita dados e retorna JSON correto"""
    payload = {
        "features": [7.4, 0.7, 0.0, 1.9, 0.076, 11.0, 34.0, 0.9978, 3.51, 0.56, 9.4]
    }
    response = client.post('/prever', 
                           data=json.dumps(payload),
                           content_type='application/json')
    
    dados = json.loads(response.data)
    
    assert response.status_code == 200
    assert "nota" in dados
    assert dados["status"] in ["Alta Qualidade", "Qualidade Padrão"]

def test_api_previsao_erro_dados(client):
    """Testa se a API reclama quando enviamos dados errados"""
    payload = {"features": [1, 2, 3]} # Enviando apenas 3 campos em vez de 11
    response = client.post('/prever', 
                           data=json.dumps(payload),
                           content_type='application/json')
    
    assert response.status_code == 400