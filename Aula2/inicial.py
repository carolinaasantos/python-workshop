'''Case - Cancelamento de Clientes

Você foi contratado por uma empresa com mais de 800 mil clientes para um projeto de Dados. Recentemente a empresa percebeu que da sua base total de clientes, a maioria são clientes inativos, ou seja, que já cancelaram o serviço.

Precisando melhorar seus resultados ela quer conseguir entender os principais motivos desses cancelamentos e quais as ações mais eficientes para reduzir esse número.'''

'''Passo a passo
- Passo 1: Importar base de dados
- Passo 2: Visualizar base de dados
- Passo 3: Corrigir problema da base de dados
- Passo 4: Análise dos cancelamentos
- Passo 5: Análise da causa dos cancelamentos (como as colunas impactam no cancelamento?)'''

# Instalações: pandas plotly openpyxl numpy nbformat ipykernel

# PASSO 1: Importar a base de dados
import pandas as pd
tabela = pd.read_csv('./cancelamentos.csv')
print(tabela)


# PASSO 2: Visualizar a base de dados
    # Entender quais informações você tem disponível
    # Identificar os problemas da base de dados
# Drop -> exclui linhas ou tabelas de acordo com a informação que passar

tabela = tabela.drop(columns="CustomerID")
print(tabela)


# PASSO 3: Tratamento de Dados = Corrigir problemas da base dados
# Valores vazios na base de dados
# Formato das informações está correto
# NaN = Not a Number
# Dropna -> exclui linhas com valores vazios

tabela = tabela.dropna()
print(tabela.info())


# PASSO 4: Analisar o cancelamento dos clientes
# Quantos clientes cancelaram? Porcentagem? 0 - não cancelou, 1 - cancelou
# Para selecionar a coluna usa colchetes []

print(tabela["cancelou"].value_counts()) # Contar a quantidade de 0 e 1
print(tabela["cancelou"].value_counts(normalize=True)) # Porcentagem


# PASSO 5: Analisar a causa de cancelamento dos clientes
# (Como as informações dos clientes impactam)
# Sempre para criar gráficos no Python são 3 etapas:

# 1. Importar a biblioteca de gráficos
import plotly.express as px

# 2. Criar o gráfico
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
    
    # 3. Exibir o gráfico
    grafico.show()

'''**Análise dos Dados**
1) Clientes do contrato mensal SEMPRE cancelam
    - Solução: Oferecer desconto nos planos anuais e trimestrais
2) Clientes que ligam amis do que 4 vezes para o call center cancelam
    - Solução: Criar um processo para resolver o problema do cliente em no máximo 3 ligações
3) Clientes que atrasaram mais de 20 dias cancelam
    - Solução: Política para resolver atrasos em até 10 dias (financeiro)'''

# Mostrando a análise caso realizemos melhoras
tabela = tabela[tabela["duracao_contrato"]!="Monthly"]
tabela = tabela[tabela["ligacoes_callcenter"]<=4]
tabela = tabela[tabela["dias_atraso"]<=20]

print(tabela["cancelou"].value_counts())
# Em percentual
print(tabela["cancelou"].value_counts(normalize=True))