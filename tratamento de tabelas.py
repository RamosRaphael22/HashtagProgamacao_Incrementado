import os
import pandas as pd
import plotly.express as px

# Passo 1 - Percorrer todos os arquivos da pasta base de dados (Pasta Vendas)
lista_arquivo = os.listdir(r"C:\pythonProject1\atividades\Vendas")
tabela_total = pd.DataFrame()
tabela_especifica = pd.DataFrame()
lista_fatumento_lojas = []
lista_devolucoes_lojas= []

# Passo 2 - Importar as bases de dados de vendas
for arquivo in lista_arquivo:
  if "Vendas" in arquivo:
    # Passo 3 - Tratar / Compilar as bases de dados
    tabela = pd.read_csv(fr"C:\pythonProject1\atividades\Vendas/{arquivo}")
    tabela_total = tabela_total._append(tabela)
    lista_fatumento_lojas.append(tabela)
  else:
    tabela = pd.read_csv(fr"C:\pythonProject1\atividades\Vendas/{arquivo}")
    lista_devolucoes_lojas.append(tabela)

# Passo 4 - Calcular o produto mais vendido em todas as lojas(em quantidade)
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)
print(tabela_produtos)

# Passo 5 - Calcular o produto que mais faturou (em faturamento)
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
print(tabela_faturamento)

# Passo 6 - Calcular a loja/cidade que mais vendeu (em faturamento) - criar um gráfico/dashboard
tabela_lojas = tabela_total.groupby('Loja').sum().sort_values(by='Faturamento', ascending=True)
grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento', title='Faturamento por loja')
grafico.show()

#passo 7 calcular o produto mais vendido de cada loja/cidade
for item in lista_fatumento_lojas:
  tabela_especifica = item
  tabela_especifica['Faturamento'] = item['Quantidade Vendida'] * item['Preco Unitario']
  tabela_faturamento_por_loja = tabela_especifica.groupby('Produto').sum().sort_values(by='Faturamento', ascending=False)
  tabela_faturamento_por_loja['loja'] = tabela_especifica["Loja"][0]
  fig = px.pie(tabela_faturamento_por_loja, values="Faturamento", names=tabela_faturamento_por_loja.index, title='Faturamento '+tabela_faturamento_por_loja['loja'][0]) 
  fig.show()

#passo 8 criar um grafico com as devoluções de cada loja/cidade
for item in lista_devolucoes_lojas:
  tabela_especifica = item
  tabela_especifica['Devoluções'] = item['Quantidade Devolvida'] * item['Preço Unitário']
  tabela_devolucoes_por_loja = tabela_especifica.groupby('Produto').sum().sort_values(by='Devoluções', ascending=False)
  tabela_devolucoes_por_loja['loja'] = tabela_especifica["Loja"][0]
  fig = px.pie(tabela_devolucoes_por_loja, values="Devoluções", names=tabela_devolucoes_por_loja.index, title='Devoluções '+tabela_faturamento_por_loja['loja'][0]) 
  fig.show()