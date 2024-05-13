import pandas as pd
import plotly.express as px

data = pd.read_csv('ClientesDB.csv')

# Média de compra do cliente
media_compra_por_cliente = data.groupby('ClientID')['Prod_Price'].mean().reset_index()

# Ordenar os clientes pelo valor médio de compra
media_compra_por_cliente = media_compra_por_cliente.sort_values(by='Prod_Price', ascending=False)

# Criar um gráfico 
fig = px.bar(media_compra_por_cliente.head(20), 
             x='ClientID', 
             y='Prod_Price', 
             title='Top 20 Clientes por Valor Médio de Compra',
             labels={'ClientID': 'Cliente ID', 'Prod_Price': 'Valor Médio de Compra'},
             text='Prod_Price')

#  hover para mostrar o valor exato
fig.update_traces(marker_color='skyblue', texttemplate='%{text:.2f}', textposition='outside')

# Personalizar o layout do gráfico
fig.update_layout(xaxis_title='', yaxis_title='', xaxis=dict(type='category'))

# plotar o gráfico
fig.show()

#produto mais vendido 
produto_mais_vendido = data['ProductID'].value_counts().idxmax()

print('O produto mais vendido na loja é:', produto_mais_vendido)
