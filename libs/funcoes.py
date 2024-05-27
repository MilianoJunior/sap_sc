import pandas as pd
import numpy as np
import streamlit as st
import os

# carregar os dados

def transformar_dados(df):
    ''' Transforma os dados dos servidores da SAP '''
    try:
        df['ValorBruto'] = df['ValorBruto'].str.replace('R$', '').str.replace('.', '').str.replace(',', '.')
        df['ValorBruto'] = df['ValorBruto'].replace(',', '.').astype(float)
        return df
    except Exception as e:
        raise Exception(f'Function transformar_dados: {e}')
def get_carregar_dados(path):
    ''' Carrega os dados dos servidores da SAP '''
    try:
        df = pd.read_csv(path, sep=';', index_col=False)
        df.columns = df.columns.str.strip()  # remove espaços em branco do início e do fim dos nomes das colunas
        df = transformar_dados(df)
        return df
    except Exception as e:
        raise Exception(f'Function carregar_dados: {e}')

def get_impacto_financeiro(df):
    ''' Retorna o impacto financeiro para o estado '''
    try:
        return df['ValorBruto'].sum()
    except Exception as e:
        raise Exception(f'Function impacto_financeiro: {e}')

def get_total_servidores_inativos(df):
    ''' Retorna o total de servidores inativos na SAP '''
    try:
        return df[df['situacao'] == 'INATIVO'].shape[0]
    except Exception as e:
        raise Exception(f'Function total_servidores_inativos: {e}')
def get_total_servidores_ativos(df):
    ''' Retorna o total de servidores ativos na SAP '''
    try:
        return df[df['situacao'] == 'ATIVO'].shape[0]
    except Exception as e:
        raise Exception(f'Function total_servidores_ativos: {e}')

def get_total_servidores(df):
    ''' Retorna o total de servidores '''
    try:
        return df.shape[0]
    except Exception as e:
        raise Exception(f'Function total_servidores: {e}')

def get_total_servidores_geral():
    ''' Retorna o total de servidores para o df escolhido '''
    try:
        return 180360.00
    except Exception as e:
        raise Exception(f'Function total_servidores_geral: {e}')

def get_total_despesas(df):
    ''' Retorna o total de despesas de todos os servidores para o df escolhido '''
    try:
        return df['ValorBruto'].sum()
    except Exception as e:
        raise Exception(f'Function total_despesas: {e}')

def percentual(X_maior, Y_menor):
    ''' Retorna o percentual do impacto financeiro para o estado '''
    try:
        return round((Y_menor / X_maior) * 100,3)
    except Exception as e:
        raise Exception(f'Function percentual: {e}')

def download_do(data):
    ''' Faz o download do diarios oficiais '''
    try:
        for s in range(3150, 3350):
            url = 'https://portal.doe.sea.sc.gov.br/apis/count-view/{s}'.format(s=s)
            name_file = download_pdf(url)
            print(s, name_file)
    except Exception as e:
        raise Exception(f'Function download_do: {e}')