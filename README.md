# Projeto de Análise de Dados -SAP

# Entendo a Nossa Secretária

Este projeto visa fornecer uma análise detalhada e abrangente sobre os servidores de uma determinada secretaria, focando em aspectos quantitativos e qualitativos que influenciam diretamente a administração pública e a política de recursos humanos. Através de uma série de passos, exploramos diversas dimensões para um entendimento profundo dos seguintes pontos:

## Análise Quantitativa
- **Passos 1-12:** Estes passos envolvem a análise da estrutura organizacional e financeira da secretaria, abrangendo desde o número de servidores ativos e inativos, médias salariais por cargo e status, até o impacto financeiro para o estado e históricos de reajustes salariais e reformas previdenciárias.

## Informações Adicionais Quantitativas
- **Passos 11-16:** Focam em investigações detalhadas sobre a sustentabilidade financeira da secretaria, incluindo déficit previdenciário, condições de aposentadoria dos servidores e comparações salariais detalhadas por status de emprego e atividade.

## Análise Qualitativa
- **Passos 17-22:** Estes passos tratam das percepções dos servidores sobre seu ambiente de trabalho e remuneração, o impacto da inflação e reformas previdenciárias nas suas remunerações, e comparações com outras secretarias. Também inclui a construção de um ranking nacional de remuneração dos policiais penais e socioeducativos.

Este projeto utiliza dados públicos para realizar análises que ajudem a melhorar a gestão de recursos humanos nas secretarias e fornecer transparência sobre a administração pública.



## Requisitos

- Python 3.9.1
- Pip

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt` e podem ser instaladas com o comando:

```bash
pip install -r requirements.txt
```

As principais bibliotecas utilizadas são:

- mysql-connector-python: para conectar e interagir com o banco de dados MySQL.
- numpy e pandas: para manipulação e análise de dados.
- streamlit: para criar aplicativos web de análise de dados.
- python-dotenv: para gerenciar variáveis de ambiente.
- streamlit_extras, streamlit-timeline, streamlit-on-Hover-tabs: para adicionar funcionalidades extras ao Streamlit.
- google-generativeai: para utilizar modelos de IA generativos do Google.
- plotly: para criar gráficos interativos.

## Execução

O aplicativo web é iniciado com o comando:

```bash
streamlit run main.py
```

Este comando deve ser executado no diretório raiz do projeto.

## Contribuição

Contribuições são bem-vindas. Para contribuir, por favor, faça um fork do projeto, crie uma branch, faça suas alterações e abra um Pull Request.

## Licença

Este projeto é licenciado sob os termos da licença MIT.