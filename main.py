'''
# Entendo a Nossa Secretária

Este projeto visa fornecer uma análise detalhada e abrangente sobre os servidores de uma determinada secretaria, focando em aspectos quantitativos e qualitativos que influenciam diretamente a administração pública e a política de recursos humanos. Através de uma série de passos, exploramos diversas dimensões para um entendimento profundo dos seguintes pontos:

## Análise Quantitativa
- **Passos 1-12:** Estes passos envolvem a análise da estrutura organizacional e financeira da secretaria, abrangendo desde o número de servidores ativos e inativos, médias salariais por cargo e status, até o impacto financeiro para o estado e históricos de reajustes salariais e reformas previdenciárias.

## Informações Adicionais Quantitativas
- **Passos 11-16:** Focam em investigações detalhadas sobre a sustentabilidade financeira da secretaria, incluindo déficit previdenciário, condições de aposentadoria dos servidores e comparações salariais detalhadas por status de emprego e atividade.

## Análise Qualitativa
- **Passos 17-22:** Estes passos tratam das percepções dos servidores sobre seu ambiente de trabalho e remuneração, o impacto da inflação e reformas previdenciárias nas suas remunerações, e comparações com outras secretarias. Também inclui a construção de um ranking nacional de remuneração dos policiais penais e socioeducativos.

Este projeto utiliza dados públicos para realizar análises que ajudem a melhorar a gestão de recursos humanos nas secretarias e fornecer transparência sobre a administração pública.

'''
# -----------------------------------------------------------
# importar bibliotecas necessárias
# -----------------------------------------------------------
import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go
import os
from libs.funcoes import ( get_carregar_dados,
                           get_impacto_financeiro,
                           get_total_servidores_inativos,
                           get_total_servidores_ativos,
                           get_total_despesas,
                           get_total_servidores,
                           get_total_servidores_geral,
                           percentual)

from libs.componentes import (comp_gauge_servidores,
                              comp_gauge,
                              componente_inflacao_acumulada)

# -----------------------------------------------------------
# Configuração da página
# -----------------------------------------------------------

st.set_page_config(
                        layout="wide",
                        page_title="EngeSEP",
                        page_icon="📊",
                        initial_sidebar_state="expanded",
                     )

# -----------------------------------------------------------
# Layout das páginas - Análise Quantitativa
# -----------------------------------------------------------

def resumo():
    ''' Menu de navegação '''
    st.sidebar.title('Menu de Navegação')
    st.sidebar.write('Selecione a análise que deseja visualizar:')

    # Análise Quantitativa
    st.sidebar.subheader('Análise Quantitativa')
    st.sidebar.write('1. Total de Servidores')
    st.sidebar.write('2. Total de Servidores Ativos')
    st.sidebar.write('3. Total de Servidores Inativos')
    st.sidebar.write('4. Total de Despesas')
    st.sidebar.write('5. Impacto Financeiro')
    st.sidebar.write('6. Média Salarial')
    st.sidebar.write('7. Média Salarial por Cargo')
    st.sidebar.write('8. Média Salarial por Status')
    st.sidebar.write('9. Média Salarial por Status e Cargo')
    st.sidebar.write('10. Total de Servidores por Status')
    st.sidebar.write('11. Total de Servidores por Status e Cargo')
    st.sidebar.write('12. Total de Servidores por Cargo')
    st.sidebar.write('13. Total de Servidores por Status e Atividade')
    st.sidebar.write('14. Total de Servidores por Status e Sexo')
    st.sidebar.write('15. Total de Servidores por Status e Escolaridade')
    st.sidebar.write('16. Total de Servidores por Status e Faixa Etária')

    # Análise Qualitativa
    st.sidebar.subheader('Análise Qualitativa')
    st.sidebar.write('17. Percepções dos Servidores')
    st.sidebar.write('18. Impacto da Inflação')
    st.sidebar.write('19. Impacto das Reformas Previdenciárias')
    st.sidebar.write('20. Comparação com Outras Secretarias')
    st.sidebar.write('21. Ranking Nacional de Remuneração')
    st.sidebar.write('22. Conclusão')



resumo()
# Configuração da variável path
path_sap = os.path.join(os.getcwd(), 'data', 'servidores_sap.csv')
path_geral = os.path.join(os.getcwd(), 'data', 'total_servidores.csv')

# carregar os dados
df_sap = get_carregar_dados(path_sap)
df_geral = get_carregar_dados(path_geral)

# Exibir o título do projeto
st.subheader('Entendendo a SAP')

# colunas
col1, col2 = st.columns(2)

# 1 passo: quantos servidores fazer parte desta secretária
total_servidores_sap = get_total_servidores(df_sap)
total_servidores = get_total_servidores_geral()


print(total_servidores_sap, df_sap.shape)
print(total_servidores)
with col1:
    st.metric('Total de servidores na SAP:',total_servidores_sap)

# gauge_01 = comp_gauge_servidores(total_servidores_sap, total_servidores, '')
gauge_01 = comp_gauge(total_servidores,total_servidores_sap, 'Total de servidores na SAP')

with col2:
    st.plotly_chart(gauge_01)

with col1:
    st.metric('Total de servidores:',total_servidores)

gauge_02 = comp_gauge(total_servidores, total_servidores, '')

with col2:
    st.plotly_chart(gauge_02)

# 2 passo: qual o impacto financeiro para o estado
total_despesas_sap = get_total_despesas(df_sap)
total_despesas_geral = get_total_despesas(df_geral)
st.write('Total de despesas na SAP:',total_despesas_sap)
comp_gauge_servidores(total_despesas_sap, total_despesas_geral, 'Total de despesas na SAP')

componente_inflacao_acumulada()

# percentual = round((impacto_financeiro / total_despesas) * 100,3)
#
# texto = f'O impacto financeiro para o estado é de R$ {impacto_financeiro}, representando {percentual} % do total de despesas. Total de despesas: R$ {total_despesas:.2f}'
#
# st.write(texto)














def main():
    ''' Dashboard principal '''

    # configuração da página


    st.markdown("""
        <style>
            body {
                margin: 0; !important
                padding: 0; !important
            }
            .st-emotion-cache-1jicfl2{
                width: 100%;
                padding: 0rem 1rem 1rem;
                min-width: auto;
                max-width: initial;
            }
        </style>
        """, unsafe_allow_html=True)

    # Header


if __name__ == '__main__':

    main()














