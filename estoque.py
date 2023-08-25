import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect("estoque.db")
cursor = conn.cursor()

# Consulta para selecionar todos os itens e quantidades do estoque
cursor.execute("SELECT item, quantidade FROM estoque")

# Recuperando os resultados da consulta
estoque_itens = cursor.fetchall()

# Mostrando os dados do estoque
print("Estoque:")
print("Item \t\t Quantidade")
print("-------------------------")
for item, quantidade in estoque_itens:
    print(f"{item: <15} {quantidade: >10}")
input()
# Fechando a conexão com o banco de dados
conn.close()
