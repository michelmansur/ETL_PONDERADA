import pytest
from your_flask_app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_get_weather_data(client):
    response = client.get('/get_weather_data')
    assert response.status_code == 200

    data = response.get_json()
    assert 'Data da Ingestão' in data
    assert 'Tipo' in data
    assert 'Valores' in data
    assert 'Uso' in data
