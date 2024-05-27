# Importar bibliotecas
import requests
import os
import pandas as pd
import PyPDF2
import streamlit as st
import re
import numpy as np
cont = 0
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

def categorizar_texto(reader):

    page = 0
    categorized_data = []
    for text in reader.pages:
        sections = re.split(r'(?<=\n)\n', text.extract_text())
        palavras = text.extract_text().split('\n')
        print(text.extract_text())
        print('¨¨¨¨¨¨¨¨¨¨¨¨'*10)
        for section in sections:
            print(section)
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

        # for s in dir(reader):
        #     if not '_' in s:
        #         try:
        #             print(s)
        #             print('  '*10,getattr(reader, s)())
        #             print('---'*10)
        #         except:
        #             try:
        #                 print(s)
        #                 print('  '*10,getattr(reader, s))
        #                 print('---'*10)
        #             except:
        #                 pass
        #
        # print(len(reader.pages))
        # page = reader.pages[3]
        # parts = []
        # def visitor_body(text, cm, tm, fontDict, fontSize):
        #     y = tm[5]
        #     if y > 50 and y < 720:
        #         parts.append(text)

        # for page in reader.pages:
        #     # parts = page.extract_text(visitor_text=visitor_body)
        #     texto = page.extract_text()
        #     parts.append(texto)
        categoria = categorizar_texto(reader)


        # text_body = "".join(parts)

        # print(text_body)
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