import pandas as pd
import plotly.express as px


data = pd.read_csv('ClientesDB.csv')

# Corversão para o date type
data['SaleDate'] = pd.to_datetime(data['SaleDate'])


data_inicio = '2024-01-01'
data_fim = '2024-12-31'


data_filtrada = data[(data['SaleDate'] >= data_inicio) & (data['SaleDate'] <= data_fim)]


media_compra_por_cliente = data_filtrada.groupby('ClientID')['Prod_Price'].mean().reset_index()


media_compra_por_cliente = media_compra_por_cliente.sort_values(by='Prod_Price', ascending=False)


fig = px.bar(media_compra_por_cliente.head(20), 
             x='ClientID', 
             y='Prod_Price', 
             title=f'Top 20 Clientes por Valor Médio de Compra ({data_inicio} a {data_fim})',
             labels={'ClientID': 'Cliente ID', 'Prod_Price': 'Valor Médio de Compra'},
             text='Prod_Price')


fig.update_traces(marker_color='skyblue', texttemplate='%{text:.2f}', textposition='outside')

fig.update_layout(xaxis_title='', yaxis_title='', xaxis=dict(type='category'))


fig.show()

# produto mais vendido na loja
produto_mais_vendido = data_filtrada['ProductID'].value_counts().idxmax()

print(f'O produto mais vendido na loja durante o período de {data_inicio} a {data_fim} é:', produto_mais_vendido)
