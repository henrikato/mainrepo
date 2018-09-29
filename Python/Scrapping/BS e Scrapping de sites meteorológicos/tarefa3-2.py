# importa o BeautifulSoup e dá a ele o alias 'bs'
from bs4 import BeautifulSoup as bs

# importa strftime, gmtime e time do módulo 'time' - https://docs.python.org/3/library/time.html
from time import strftime, gmtime, time
# https://docs.python.org/3/library/time.html#time.strftime
# strftime(formato, data) - converte uma data retornada por gmtime() ou localtime() para uma string especificada no formato
# https://docs.python.org/3/library/time.html#time.gmtime
# gmtime() - converte uma timestamp em um objeto com data e hora (struct_time)

import requests, json, os, platform
# requests - módulo python para fazer requisições de conteúdo
# json - módulo python para trabalhar com JSON
# os - módulo utilizado para interação com o sistema ou o console executando este código
# (https://docs.python.org/3/library/os.html)
# platform - acessa os dados de identificação da plataforma
# (https://docs.python.org/3/library/platform.html)

# Este código exibe temperatura mínima e máxima da cidade na
# página inicial do site do National Weather Service (serviço de meteorologia americano)

#encontra espaços em branco em uma string
def find_whitespace(string):
    for char in string:
        if char == ' ':
            return string.index(char)

# função que converte temperatura de fahrenheit para celsius e vice-versa
# https://www.w3resource.com/python-exercises/python-conditional-exercise-2.php
def converte_temperatura(temp, callback):
    # remove qualquer texto que tenha antes da temperatura em si
    temperature = temp[find_whitespace(temp)+1:]
    #converte o valor da temperatura para int (para que os cálculos sejam feitos)
    degree = int(temperature[:find_whitespace(temperature)])

    #pega o último caractere da string para identificar a escala (celsius ou fahrenheit)
    scale = temp[-1]
    
    if scale.upper() == "C":
        result = int(round((9 * degree) / 5 + 32))
        scale = "F"
    elif scale.upper() == "F":
        result = int(round((degree - 32) * 5 / 9))
        scale = "C"
    else:
        print("A temperatura informada é inválida.")
    return callback(result, scale)

def exibe_previsao_tempo(cidade):
    # parâmetros de busca de informações da cidade selecionada
    payloadBuscaCidade = {
        'text': cidade['text'], # nome da cidade
        'magicKey': cidade['magicKey'], # chave identificadora da cidade
        'f': 'json' # tipo de retorno
    }
    buscaCidade = requests.get("https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/find", params=payloadBuscaCidade)
    retornoBusca = buscaCidade.json()

    #os resultados da consulta acima ficam dentro de um objeto 'locations'
    dadosCidade = retornoBusca['locations'][0]

    print("\nPrevisão do tempo atual para ",dadosCidade['name'],":",sep='')

    # com a busca acima ainda é necessário se obter os dados de latitude e longitude
    # para que outro serviço busque os dados meteorológicos com base em coordenadas
    latLon = dadosCidade['feature']['geometry']

    # estas coordenadas então são adicionadas aos parâmetros de outra consulta
    payload = {
        'lat': round(latLon['y'], 4),
        'lon': round(latLon['x'], 4)
    }
    busca = requests.get("https://forecast.weather.gov/MapClick.php?", params=payload)

    # esta consulta, por sua vez, leva à página de previsão do tempo (ao invés de retornar um JSON)
    retorno = bs(busca.text, "html.parser")
    # é obtido a condição meteorológica da região
    print(retorno.find(class_="myforecast-current").get_text())
    # e a temperatura (em graus celsius)
    print(retorno.find(class_="myforecast-current-sm").get_text(),"\n")

    # esta página também possui informação detalhada da previsão para os próximos dias
    previsao_semana = retorno.find_all(class_="forecast-tombstone")
    cont = 0
    # e para cada um deles...
    for previsao in previsao_semana:
        # retorno o nome do dia
        print(previsao.find(class_="period-name").get_text(separator=u' '),":",sep='')
        # a descrição da condição do clima
        print("  ",previsao.find(class_="short-desc").get_text(separator=u' '))
        # e a temperatura (em ºF, porque eles querem)
        temperatura = previsao.find(class_="temp").get_text(separator=u' ')
        # mas como bom fuçador fiz uma função que converte essa temperatura para facilitar a vida
        # esta função recebe uma string com a temperatura, e retorna duas coisas:
        #  valor da temperatura e a escala (celsius ou fahrenheit)
        # como segundo parâmetro fiz uma função lamba que recebe estes 2 parâmetros e printa
        #  a temperatura formatada
        converte_temperatura(temperatura, lambda temp, escala: 
            print("   ",temp,"º",escala,sep='') 
        )
        cont += 1
        if cont % 2 == 1: print("-------------------------------")

# como todo bom programador nutella é importante limpar o console antes de rodar alguma coisa
#  então utilizando o platform.system() para identificar o S.O. e o os.system para interagir
#  com o console eu faço a limpeza
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

encontrou = False
while encontrou == False:
    print("(Caso queira sair do programa digite 'sair' no nome da cidade)")
    cidade = input("Digite o nome de uma cidade: ")
    if cidade == 'sair':
        print("(Programa encerrado)")
        break
    payloadBusca = {
        'f': 'json',
        'maxSuggestions': 10,
        'text': cidade
    }
    busca = requests.get("https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/suggest", params=payloadBusca)
    retorno = busca.json()['suggestions']
    if len(retorno) == 0:
        print("\nNenhuma cidade foi encontrada. Tente novamente.")
    else:
        encontrou = True
        if len(retorno) > 1:
            cont = 0
            for cidade in retorno:
                print("\n",cont," - ",cidade['text'], sep='')
                cont += 1
            
            print("\nVárias cidades foram encontradas.")
            selecao = input("Digite o número antes do nome da cidade desejada para selecioná-la: ")
            selecao = int(selecao)
            cont -= 1
            if selecao > cont:
                print("Este número não é válido, olhe novamente a lista.")
            else:
                exibe_previsao_tempo(retorno[selecao])
        else:
            exibe_previsao_tempo(retorno[0])
