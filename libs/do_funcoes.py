# Importar bibliotecas
import streamlit as st
import requests
import os
import pandas as pd
import PyPDF2
import re
import numpy as np


cont = 0

# Restante do seu código...


def download_pdf(url):
    ''' Faz o download do diarios oficiais '''

    try:

        # primeiro request para pegar o nome do arquivo
        response = requests.get(url)

        # pegar o nome do arquivo
        print(response.json())

        if not response.json()['error']:
            file_name = response.json()['data']['dsArquivo']
            name = os.path.join('assets', file_name.replace('/', '_'))
        #     name = 'assets/' + file_name.replace('/', '_')
        #     # segundo request para fazer o download do pdf
            url_pdf = 'https://portal.doe.sea.sc.gov.br/repositorio' + file_name
        #     print(url_pdf)
            response = requests.get(url_pdf)
        #     print('Fazendo o download do pdf...')
            with open(name, 'wb') as f:
                f.write(response.content)
            return name
        else:
            return None
    except Exception as e:
        return  None

def armazenar_nomes_arquivos():
    ''' Armazena os nomes dos arquivos '''

    path = 'assets/'
    files = os.listdir(path)
    return files
'''
Tenho a seguinte lib para abrir o pdf
PyPDF2, e preciso categorizar o texto e tratar os dados para que eu possa fazer a análise dos dados.
o DO é dividido em seções, preciso tratar essas informações e criar um dataframe com as informações.
'''
def abrir_pdf(file_name):
    ''' Abre o pdf '''

    try:
        pdfFileObj = open(file_name, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        return pdfReader
    except Exception as e:
        raise Exception('Erro ao abrir o pdf.{e}'.format(e=e))

def anexar_frase(palavras):
    ''' Anexa a frase '''
    qtd = len(palavras)
    for i in range(0,qtd):
        if i >= qtd-1:
            break
        # print(i, qtd, palavras[i])
        if palavras[i][-1] == '-':
            palavras[i] =  palavras[i][:-1] + palavras[i+1]
            palavras.pop(i + 1)
            qtd = len(palavras)

    return palavras

def buscar_secao(palavras):
    ''' Busca a seção '''
    def todas_palavras_maiusculas(frase):
        palavras = frase.split()
        for palavra in palavras:
            if not palavra.isupper():
                return False
        return True
    secao = []
    for palavra in palavras:
        # verifica se as palavras são todas maiúsculas
        if todas_palavras_maiusculas(palavra):
            secao.append(palavra)
    return secao

def categorizar_texto(reader):

    page = 0
    categorized_data = []
    for text in reader.pages:
        sections = re.split(r'(?<=\n)\n', text.extract_text())
        palavras = text.extract_text().split('\n')
        palavras = anexar_frase(palavras)
        secao = buscar_secao(palavras)
        for section in enumerate(secao):
            print('Secao: ',section)
            print('---'*10)

        # print(sections)
        for palavra in palavras:
            categorized_data.append(palavra)
        break

    df = criar_dataframe({'palavras': categorized_data})

    return df

def criar_dataframe(categorized_data):
    df = pd.DataFrame(categorized_data)
    return df

def ignore_header_footer(reader):
    try:
        categoria = categorizar_texto(reader)
        return categoria
    except Exception as e:
        raise Exception('Erro ao ignorar o header e footer.{e}'.format(e=e))

def tratar_data(x):
    ''' Trata a data '''
    return f'{x[6:]}-{x[4:6]}-{x[:4]}'

def main():
    ''' Função principal'''
    try:
        global cont
        download = st.button('Download DO')
        leitura = st.button('Leitura')
        indice = st.empty()
        erro = 0
        if download:
            for s in range(400, 4000):
                indice.text(f'Cont: {cont} - Download NR: {s} - erro: {erro}')
                url = 'https://portal.doe.sea.sc.gov.br/apis/count-view/{s}'.format(s=s)
                name_file = download_pdf(url)
                if cont is not None:
                    cont += 1
                else:
                    erro += 1
        if leitura:
            nomes = pd.DataFrame({'nomes': armazenar_nomes_arquivos()})
            nomes['data'] = nomes['nomes'].apply(lambda x: tratar_data(x.split('_')[2]))
            st.dataframe(nomes)
            path = os.path.join('assets', nomes['nomes'][0])
            dados = abrir_pdf(path)
            body = ignore_header_footer(dados)

            # st.write(len(body))
            st.dataframe(body)
            st.dataframe(body['palavras'].value_counts())


    except Exception as e:
        print('Erro no main.{e}'.format(e=e))


