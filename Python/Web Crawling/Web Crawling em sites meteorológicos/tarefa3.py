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

# Este código exibe temperatura mínima e máxima da cidade na página inicial do site do Inmet

# faz requisição para retornar a página inicial
#page = requests.get("http://www.inmet.gov.br/portal/")

# faz o parse do conteúdo utilizando o beautifulsoup
#soup = bs(page.content, 'html.parser')

#cidade = soup.find(id="tempo_cidade")
#min_cidade = soup.find(id="tempo_temperatura_min")
#max_cidade = soup.find(id="tempo_temperatura_max")
#print("Cidade:", cidade.text)
#print("Mínima:", min_cidade.attrs["value"], "ºC")
#print("Máxima:", max_cidade.attrs["value"], "ºC")

# Exibe temperatura mínima e máxima de uma cidade qualquer
def exibe_previsao_tempo(cidade):
    # faz requisição dos dados climáticos de uma cidade na hora atual
    previsao_tempo = requests.get("http://www.inmet.gov.br/portal/index.php?r=tempo2/previsaoDeTempo&code="+str(cidade['id'])+"&_="+str(time()))
    # esta requisição retorna um JSON que deve ser tratado
    parse_previsao = previsao_tempo.json()
    # desta requisição pego apenas os dados da cidade
    retorno = parse_previsao[cidade['id']]

    # gero uma string com a data atual apenas para pegar a previsão do dia atual
    data_atual = str(strftime("%d-%m-%Y", gmtime()))
    # no objeto de cidade, com a data gerada acima, eu pego o nome do município e da UF
    municipio = retorno[data_atual]['manha']['entidade'] + " - " + retorno[data_atual]['manha']['uf']

    # utilizo o print com o argumento "sep=''" para remover o espaço vazio entre as string concatenadas
    print("\nPrevisão do tempo desta semana para a cidade de ",municipio, ":", sep='')
    # o objeto da cidade filtrada, retorna a previsão dos próximos dias
    for previsao_dia in retorno:
        # e para cada dia...
        previsao = retorno[previsao_dia]
        print("\nPrevisão do tempo para ", previsao_dia, ":", sep='')
        # aparentemente, o site retorna apenas temperaturas mínima e máxma para os dois primeiros dias
        if previsao.get('temp_min') != None:
            print("\n  Mínima: ", previsao.get('temp_min'), "ºC", sep='')
            print("  Máxima: ", previsao.get('temp_max'), "ºC", sep='')
        else:
            # e para o restante dos dias retorna mínima e máxima para os períodos da manhã, tarde e noite
            for periodo in previsao:
                print("\n  Previsão para o período da ", periodo, ":", sep='')
                print("\n    Mínima: ", previsao[periodo].get(
                    'temp_min'), "ºC", sep='')
                print("    Mínima: ", previsao[periodo].get(
                    'temp_min'), "ºC", sep='')
        print("\n-------------------------------------------")

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
    busca = requests.get("http://www.inmet.gov.br/portal/index.php?r=municipio/sugestMunicipio&term="+cidade)
    retorno = busca.json()
    if len(retorno) == 0:
        print("\nNenhuma cidade foi encontrada. Tente novamente.")
    else:
        encontrou = True
        if len(retorno) > 1:
            cont = 0
            for dados_cidade in retorno:
                print("\n",cont,' - ',dados_cidade['municipio'],sep='')
                cont += 1
            selecao = cont + 1
            print("\nVárias cidades foram encontradas.")
            while int(selecao) > cont:
                selecao = input("Digite o número antes do nome da cidade desejada para selecioná-la: ")
                selecao = int(selecao)
                cont -= 1
                if selecao > cont:
                    print("Este número não é válido, olhe novamente a lista.")
                else:
                    exibe_previsao_tempo(retorno[selecao])
        else:
            exibe_previsao_tempo(retorno[0])
