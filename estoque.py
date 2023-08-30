import sqlite3
import sys
import time
import os
def mostrar_estoque(cursor):
    print("Estoque:")
    print("ID \t Item \t\t Quantidade")
    print("-------------------------")
    cursor.execute("SELECT rowid, item, quantidade FROM estoque")
    estoque_itens = cursor.fetchall()
    for rowid, item, quantidade in estoque_itens:
        print(f"{rowid: <3} {item: <15} {quantidade: >10}")

def inserir_item(cursor, conn):
    item = input("Digite o nome do novo item: ")
    quantidade = int(input("Digite a quantidade do novo item: "))
    cursor.execute("INSERT INTO estoque (item, quantidade) VALUES (?, ?)", (item, quantidade))
    conn.commit()
    print(f"{quantidade} unidades de {item} foram adicionadas ao estoque.")

def remover_item(cursor, conn):
    item_id = int(input("Digite o ID do item a ser removido: "))
    cursor.execute("SELECT item FROM estoque WHERE rowid=?", (item_id,))
    item = cursor.fetchone()
    if item:
        cursor.execute("DELETE FROM estoque WHERE rowid=?", (item_id,))
        conn.commit()
        print(f"O item '{item[0]}' foi removido do estoque.")
    else:
        print("Item não encontrado.")

def atualizar_quantidade(cursor, conn):
    mostrar_estoque(cursor)
    item_id = int(input("Digite o ID do item para atualizar quantidade: "))
    quantidade = int(input("Digite a quantidade a ser adicionada (positiva) ou removida (negativa): "))
    cursor.execute("SELECT item, quantidade FROM estoque WHERE rowid=?", (item_id,))
    item_data = cursor.fetchone()
    if item_data:
        item, current_quantity = item_data
        new_quantity = current_quantity + quantidade
        cursor.execute("UPDATE estoque SET quantidade=? WHERE rowid=?", (new_quantity, item_id))
        conn.commit()
        if quantidade >= 0:
            print(f"{quantidade} unidades foram adicionadas ao estoque de {item}.")
        else:
            print(f"{-quantidade} unidades foram removidas do estoque de {item}.")
    else:
        print("Item não encontrado.")

# Conectando ao banco de dados
conn = sqlite3.connect("estoque.db")
cursor = conn.cursor()

while True:
    
    print("\nOpções:")
    print("1. Mostrar estoque")
    print("2. Inserir item")
    print("3. Remover item")
    print("4. Atualizar quantidade")
    print("5. Sair")
    escolha = input("Escolha uma opção: ")
    os.system('cls')  # Limpa a tela
    if escolha == "1":
        mostrar_estoque(cursor)
    elif escolha == "2":
        inserir_item(cursor, conn)
    elif escolha == "3":
        mostrar_estoque(cursor)
        remover_item(cursor, conn)
    elif escolha == "4":
        mostrar_estoque(cursor)
        atualizar_quantidade(cursor, conn)
    elif escolha == "5":
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

# Fechando a conexão com o banco de dados
conn.close()
