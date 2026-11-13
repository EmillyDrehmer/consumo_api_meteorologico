import requests


#Função que obtem dados da previsão
def obter_previsao():

    #endpoint
    url = "http://127.0.0.1:8000/v1/forecast"

    #parametros para consulta
    parametros = {
        "latitude": -26.4851,
        "longitude": -49.0713,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,wind_speed_10m",
        "forecast_days": 1,
        "timezone": "America/Sao_Paulo"
    }

    
    #puxa os parametros da consulta
    resposta = requests.get(
    url, 
    params=parametros,
    timeout = 15
    )

    #retorna erro se a api não funcionar 
    resposta.raise_for_status()

    #dados da api
    dados = resposta.json()

    #condições
    condicoes = dados["current"]

    temperature = condicoes["temperature_2m"]
    umidade = condicoes["relative_humidity_2m"]
    sensacao_termica = condicoes["apparent_temperature"]

    return{
        "Temperatura" : temperature,
        "Umidade" : umidade,
        "Sensação_Térmica" : sensacao_termica
    }
    

#teste de consumidor
if __name__ == "__main__":

    resultado = obter_previsao()

    print("PREVISÃO METEOROLÓGICA")
    print(f"Temperatura: {resultado['Temperatura']}°C")
    print(f"Umidade: {resultado['Umidade']}°C")
    print(f"Sensação Térmica: {resultado['Sensação_Térmica']}°C")
