from fastapi import FastAPI, Query
import requests
import json

app = FastAPI()

@app.get('/api/hello')
def hello_word():
    '''
    Retorna um dicionário com a chave 'Hello' e o valor 'World'
    '''
    return {'Hello': 'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Retorna um dicionário com os restaurantes e seus cardápios
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if (response.status_code == 200):
        dados_jason = response.json()
        if restaurante is None:
            return {'Dados': dados_jason}
        
        dados_restaurante = []
        for item in dados_jason:
            if item ['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Restaurantes': restaurante, 'Cardápio': dados_restaurante}
    else:
        print(f'Erro ao acessar a API: {response.status_code} - {response.text}')
