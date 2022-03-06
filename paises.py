import  json

import requests

url_all = 'https://restcountries.com/v3/all'
url_name = 'https://restcountries.com/v3.1/name'
url_region = 'https://restcountries.com/v3.1/region'


def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print('Erro ao fazer requisição em: ', url)


def parsing(texto_da_resposta):
    try:
        return json.loads(texto_da_resposta)
    except:
        print('Erro ao fazer parsing')


def contagem_paises(todos_os_paises):
    return len(todos_os_paises)


def listar_paises():
    try:
        resposta = requisicao(url_all)
        lista_paises = parsing(resposta)
        if lista_paises:
            for pais in lista_paises:
                print(f"{pais['name']['common']}")
        else:
            print('Erro ao lista países')
    except:
        print('Erro! Tente Novamente.')


def mostrar_populacao(nome_pais):
    try:
        resposta = requisicao(f"{url_name}/{nome_pais}")
        if resposta:
            lista_paises = parsing(resposta)
            if lista_paises:
                for pais in lista_paises:
                    print(f"{pais['name']['common']}: {pais['population']}")
            else:
                print('País não encontrado')
    except:
        print('Erro! Tente Novamente.')


def mostrar_capital(nome_pais):
    try:
        resposta = requisicao(f'{url_name}/{nome_pais}')
        if resposta:
            lista_paises = parsing(resposta)
            if lista_paises:
                for pais in lista_paises:
                    print(f"{pais['name']['common']}: {pais['capital']}")
            else:
                print('País não encontrado')
    except:
        print('Erro! Tente Novamente.')

def mostrar_regiao(url):
    try:
        resposta = requisicao(url)
        if resposta:
            lista_paises = parsing(resposta)
            if lista_paises:
                for pais in lista_paises:
                    print(f"{pais['name']['common']}")
            else:
                print('Região não encontrado')
    except:
        print('Erro! Tente Novamente.')


while True:
    print('='*30)
    print('Bem vindo ao sistema de países')
    print('Qual ação deseja realizar?')
    print('''
     1 - Listar Países
     2 - Total de População de um país
     3 -  Capital de um país
     4 - Listar países de uma região
     0 - sair
     ''')
    print('='*30)
    resposta = input('Digite o número da ação: ')
    if resposta == '1':
        listar_paises()
    elif resposta == '2':
            pais = input('País: ').capitalize()
            mostrar_populacao(pais)
            if mostrar_populacao(pais) == ' ':
                print('Dados sobre o país não encontrados!')
    elif resposta == '3':
        pais = input('País: ').capitalize()
        mostrar_capital(pais)
        if mostrar_capital(pais) == ' ':
            print('Dados sobre o país não encontrados!')
    elif resposta == '4':
        print('''
        1 - África
        2 - América
        3 - Ásia
        4 - Europa
        5 - Oceania
        ''')
        res = input('Digite o número da opção: ')
        if res == '1':
            print('Listando países da África...')
            mostrar_regiao('https://restcountries.com/v3.1/region/africa')
        elif res == '2':
            print('Listando países da América...')
            mostrar_regiao('https://restcountries.com/v3.1/region/americas')
        elif res == '3':
            print('Listando países da Ásia...')
            mostrar_regiao('https://restcountries.com/v3.1/region/asia')
        elif res == '4':
            print('Listando países da Europa...')
            mostrar_regiao('https://restcountries.com/v3.1/region/europe')
        elif res == '5':
            print('Listando países da Oceania...')
            mostrar_regiao('https://restcountries.com/v3.1/region/oceania')
        elif mostrar_regiao('https://restcountries.com/v3.1/region/') == None:
            print('Dados sobre a região não encontrados')
    elif resposta == '0':
        print('Saindo do sistema de países...')
        break
    else:
        print('Opção inválida! Tente novamente.')