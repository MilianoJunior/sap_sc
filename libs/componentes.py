
import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go

def comp_gauge_servidores(X, y, titulo):
    ''' Cria um gauge para exibir a porcentagem de servidores do órgão '''
    # Cálculo da porcentagem
    porcentual = (y / X) * 100

    # Criando o gauge
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=porcentual,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': titulo},
        gauge={
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 50], 'color': 'lightgray'},
                {'range': [50, 100], 'color': 'gray'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90}
        }
    ))

    # Alterar o tamanho do gráfico
    fig.update_layout(autosize=False, width=320, height=220)

    return fig
    # return fig
def comp_gauge(X, y, titulo):
    ''' Valor percentual da varial X em relação a varial x - Pie'''

    percentual = (y / X) * 100

    fig = go.Figure()
    fig.add_trace(go.Pie(labels=['X', 'x'], values=[X, y], hole=0.7))

    # Adiciona anotação no centro do gráfico de pizza
    fig.update_layout(
        annotations=[dict(text=f'{percentual:.2f}', x=0.5, y=0.5, font_size=20, showarrow=False, font=dict(color='black'))]
    )

    # Configurando layout do gráfico
    fig.update_layout(title='', width=300, height=300)

    return fig

def componente_inflacao_acumulada():

    # inflação acumulada
    inflacao_ipca = {
                    '2022': 5.7848,
                    '2023': 4.6211,
                    '2024': 1.4669,
    }


    inflacao_ipca_ac = {
                    '2022': 5.7848, # de janeiro
                    '2023': 10.4059,
                    '2024': 11.8728, # até abril
    }

    # salários dos servidores
    remuneracao = [6000, 6000, 6000]

    # desconto do IPREV
    desconto_iprev = [0.14, 0.14, 0.14]

    # deasconto do IPRF
    desconto_iprf_media = [0.103, 0.103, 0.103]

    # calcular o salário líquido do IPREV
    salario_liquido = [r - (r * d) for r, d in zip(remuneracao, desconto_iprev)]

    # calcular a inflação acumulada
    salario_liquido_real = [r - (r * d) for r, d in zip(salario_liquido, desconto_iprf_media)]

    # calcular o salário líquido defasado
    salario_liquido_defasado = [r - (r * (i / 100)) for r, i in zip(salario_liquido_real, inflacao_ipca_ac.values())]

    # criar um DataFrame
    df = pd.DataFrame({
        'Ano': list(inflacao_ipca.keys()),
        'Remuneração Bruta (mil)': remuneracao,
        'Desconto IPREV (%)': desconto_iprev,
        'Desconto IPRF Médio (%)': desconto_iprf_media,
        'Salário Líquido Real': salario_liquido_real,
        'IPCA (%)': list(inflacao_ipca_ac.values()),
        'Salário Líquido defasado': salario_liquido_defasado
    })

    # exibir o DataFrame
    for i, row in df.iterrows():
        print(f"Ano: {row['Ano']}")
        print(f"Remuneração Bruta (mil): {row['Remuneração Bruta (mil)']}")
        print(f"Desconto IPREV (%): {row['Desconto IPREV (%)']}")
        print(f"Desconto IPRF Médio: {row['Desconto IPRF Médio (%)']}")
        print(f"Salário Líquido Real: {row['Salário Líquido Real']}")
        print(f"IPCA: {row['IPCA (%)']}")
        print('______________________')

    # Criar um objeto de figura
    fig = go.Figure()

    # Adicionar as linhas ao gráfico com pontos
    fig.add_trace(go.Scatter(x=df['Ano'], y=df['Remuneração Bruta (mil)'], mode='lines+markers', name='Remuneração Bruta (mil)'))
    fig.add_trace(go.Scatter(x=df['Ano'], y=df['Salário Líquido Real'], mode='lines+markers', name='Salário Líquido Real'))
    fig.add_trace(go.Scatter(x=df['Ano'], y=df['Salário Líquido defasado'], mode='lines+markers', name='Salário Líquido defasado'))

    # Adicionar anotações de texto para cada ponto no eixo y
    for i, row in df.iterrows():
        fig.add_annotation(x=row['Ano'], y=row['Remuneração Bruta (mil)'], text=str(round(row['Remuneração Bruta (mil)'], 2)))
        fig.add_annotation(x=row['Ano'], y=row['Salário Líquido Real'], text=str(round(row['Salário Líquido Real'], 2)))
        fig.add_annotation(x=row['Ano'], y=row['Salário Líquido defasado'], text=str(round(row['Salário Líquido defasado'], 2)))

    # Configurar o layout do gráfico
    fig.update_layout(title='Perdas Salariais dos Servidores em Relação à Inflação para um Salário de R$6.000 (Nível I)',
                      xaxis_title='Ano',
                      yaxis_title='Valor (R$)',
                      showlegend=True)

    # Exibir o gráfico
    st.plotly_chart(fig)

    st.dataframe(df)


def componente_impacto_dos_impostos():
    ''' Calcula o impacto dos impostos sobre a renda familiar '''

    # Dados
    gastos_familiares = {
        'gasolina': 600,
        'alimentacao': 1000,
        'luz': 200,
        'agua': 100,
        'internet': 100,
        'medicamentos': 400,
    }

    carga_tributaria_media = {
        'gasolina': 0.45,
        'alimentacao': 0.25,
        'luz': 0.25,
        'agua': 0.25,
        'internet': 0.25,
        'medicamentos': 0.25,
    }

    gastos_liquidos = {k: v - (v * carga_tributaria_media[k]) for k, v in gastos_familiares.items()}
    impostos = [v * carga_tributaria_media[k] for k, v in gastos_familiares.items()]

    df_gastos = pd.DataFrame({
        'Despesa familiares': list(gastos_liquidos.keys()),
        'Valor (R$)': list(gastos_familiares.values()),
        'Carga Tributária média (%)': list(carga_tributaria_media.values()),
        'Imposto (R$)': impostos,

    })
    st.dataframe(df_gastos)
    st.write(f'Total de despesas: {sum(list(gastos_liquidos.values()))}   Total de impostos: R$ {sum(impostos)}')
