import random
from datetime import datetime, timedelta

# Função para gerar uma data aleatória dentro de um intervalo específico
def random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date

# Geração dos dados
num_dados = 3600
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 4, 30)

# IDs de cliente fixos
clientes_fixos = [68, 67, 88, 98, 105, 106, 104, 65, 64, 78, 75, 98, 99, 34, 35, 45, 46]

# IDs de produto fixos
produtos_fixos = [32, 64, 65, 66, 87, 97]

dados = []

for _ in range(num_dados):
    if random.random() < 0.4:  # 40% de chance de escolher um cliente fixo
        id_cliente = random.choice(clientes_fixos)
    else:
        id_cliente = random.randint(1, 200)
    data_venda = random_date(start_date, end_date).strftime('%d/%m/%Y')
    if random.random() < 0.50:  # 99% de chance de escolher um produto fixo
        id_produto = random.choice(produtos_fixos)
    else:
        id_produto = random.randint(1, 200)
    preco_produto = round(random.uniform(10, 1000), 2)
    dados.append((id_cliente, data_venda, id_produto, preco_produto))

# Salvando os dados em um arquivo CSV
with open('dados_regressao.csv', 'w') as f:
    f.write("ID Cliente,Data Venda,ID Produto,Preço Produto\n")
    for dado in dados:
        f.write(f"{dado[0]},{dado[1]},{dado[2]},{dado[3]}\n")

print("Dados gerados e salvos com sucesso!")
