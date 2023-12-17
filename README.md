# ETL_PONDERADA
Este é um projeto simples que demonstra a criação de uma aplicação Flask para realizar ETL (Extract, Transform, Load) usando a API OpenWeather. O objetivo é consultar dados climáticos de uma cidade específica, manipulá-los e armazená-los em uma tabela com quatro colunas: Data da Ingestão, Tipo, Valores e Uso.

## Configuração
Antes de executar o código, certifique-se de ter o Python instalado em seu ambiente. Além disso, você precisará de uma chave da API OpenWeather, que pode ser obtida aqui.

pip install -r requirements.txt

## Executando a Aplicação
Para iniciar o servidor Flask, execute o seguinte comando no terminal:


python app.py
O servidor será iniciado e estará disponível em http://127.0.0.1:5000/. A rota principal é /get_weather_data.

## Testes de Integração
Os testes de integração foram implementados usando a biblioteca pytest. Para executar os testes, utilize o seguinte comando:

bash
pytest test_app.py

## Estrutura do Projeto (pastas)
app.py: Contém o código principal da aplicação Flask.
test_app.py: Arquivo de teste de integração usando pytest.
requirements.txt: Lista de dependências do projeto.