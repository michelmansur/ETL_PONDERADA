from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/get_weather_data')
def get_weather_data():
    # Consulta à API OpenWeather para obter dados climáticos de uma cidade (exemplo: São Paulo)
    api_key = 'fad000d130756c6d54a173e614889d3d'
    city_name = 'Sao Paulo'
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={SaoPaulo}&appid={api_key}'
    
    response = requests.get(api_url)
    weather_data = response.json()

    # Manipulação dos dados para criar a tabela com as colunas especificadas
    data_ingestion = 'data_atual'  # Substitua pela data atual
    tipo = 'clima'
    valores = weather_data['main']
    uso = 'análise'

    # Armazenamento das informações em uma estrutura de dados (ex: lista de dicionários)
    table_data = {
        'Data da Ingestão': data_ingestion,
        'Tipo': tipo,
        'Valores': valores,
        'Uso': uso
    }

    return jsonify(table_data)

if __name__ == '__main__':
    app.run(debug=True)
