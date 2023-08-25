import os
import sys
import time
def main():
    senha_correta = "2805"
    tentativas_restantes = 3

    while tentativas_restantes > 0:
        senha_digitada = input("Digite a senha para acessar o caixa: ")

        if senha_digitada == senha_correta:
            print("Senha correta. Acesso permitido.")
            time.sleep(2)  # Pausa por 2 segundos
            os.system('cls')  # Limpa a tela
            break
        else:
            tentativas_restantes -= 1
            print(f"Senha incorreta. Tentativas restantes: {tentativas_restantes}")

            if tentativas_restantes == 0:
                print("Todas as tentativas foram esgotadas. Acesso bloqueado.")
                exit()
                break

if __name__ == "__main__":
    main()

def selecionar_opcao(opcoes):
    mostrar_menu(opcoes)
    escolha = int(input("Escolha uma opção: "))
    os.system('cls')
    return opcoes[escolha - 1]

def mostrar_menu(opcoes):
    for i, opcao in enumerate(opcoes, start=1):
        print(f"({i}) {opcao['nome']} {'-' * (80 - len(opcao['nome']) - len(str(opcao['preco'])))} {opcao['preco']} R$")

def main():
    extrato = []
    pedidos = []

    pizzas = [
        {"nome": "Calabresa", "preco": 15},
        {"nome": "Frango", "preco": 15},
        {"nome": "Napolitana", "preco": 15},
        {"nome": "Frango com catupiry", "preco": 18},
        {"nome": "Portuguesa", "preco": 18},
        {"nome": "Bacon com cheddar", "preco": 18},
        {"nome": "A moda", "preco": 23},
        {"nome": "Chocolate", "preco": 16},
        {"nome": "Banana com canela", "preco": 16},
        {"nome": "Doce de leite", "preco": 16}
    ]

    bebidas = [
        {"nome": "Guaraná Jesus", "preco": 8},
        {"nome": "Dolly", "preco": 5},
        {"nome": "Goianinho", "preco": 4},
        {"nome": "Mineiro", "preco": 5},
        {"nome": "Bare", "preco": 4},
        {"nome": "Itubaina", "preco": 4},
        {"nome": "Fresh", "preco": 3},
        {"nome": "Del Valle", "preco": 8},
        {"nome": "Kaiser", "preco": 7}
    ]

    while True:

        print("MENU PRINCIPAL (Caixa)")
        print("(1) Pizzas")
        print("(2) Bebidas")
        print("(3) Extrato")
        print("(4) Finalizar Pedido")
        print("(5) Zerar Extrato")
        print("(6) Ver Pedidos Realizados")
        print("(7) Gerar Relatório")
        print("(8) Sair")

        escolha_menu_principal = int(input("Escolha uma opção: "))
        os.system('cls')

        if escolha_menu_principal == 1:
            escolha_pizza = selecionar_opcao(pizzas)
            extrato.append(escolha_pizza)
            print(f"{escolha_pizza['nome']} adicionada ao extrato.")

        elif escolha_menu_principal == 2:
            escolha_bebida = selecionar_opcao(bebidas)
            extrato.append(escolha_bebida)
            print(f"{escolha_bebida['nome']} adicionada ao extrato.")

        elif escolha_menu_principal == 3:
            print("Extrato:")
            total = 0
            for item in extrato:
                print(f"{item['nome']}: {item['preco']} R$")
                total += item['preco']
            print(f"Total: {total} R$\n\n\n")

        elif escolha_menu_principal == 4:
            if extrato:
                pedidos.append(extrato.copy())
                total_pedido = sum(item['preco'] for item in extrato)
                extrato.clear()
                print(f"Pedido finalizado. Total: {total_pedido} R$")
            else:
                print("Nenhum item no extrato para finalizar.")

        elif escolha_menu_principal == 5:
            extrato.clear()
            print("Extrato zerado.")

        elif escolha_menu_principal == 6:
            print("Pedidos Realizados:")
            for idx, pedido in enumerate(pedidos, start=1):
                print(f"Pedido {idx}:")
                total_pedido = sum(item['preco'] for item in pedido)
                for item in pedido:
                    print(f"{item['nome']}: {item['preco']} R$")
                print(f"Total do Pedido: {total_pedido} R$\n")
            print("\n")

        elif escolha_menu_principal == 7:
            print("Gerando relatório...")
            time.sleep(3)  # Pausa por 3 segundos
            os.system('cls')  # Limpa a tela
            print("Calculando os preços...")
            time.sleep(3)  # Pausa por 3 segundos
            os.system('cls')  # Limpa a tela
            print("Juntando os pedidos...")
            time.sleep(3)  # Pausa por 3 segundos
            os.system('cls')  # Limpa a tela
            
            with open("relatorio_pedidos.txt", "w") as arquivo:
                arquivo.write("Relatório de Pedidos:\n")
                total_geral = 0
                total_pedidos = len(pedidos)
                
                for idx, pedido in enumerate(pedidos, start=1):
                    arquivo.write(f"Pedido {idx}:\n")
                    total_pedido = sum(item['preco'] for item in pedido)
                    total_geral += total_pedido

                    for item in pedido:
                        arquivo.write(f"{item['nome']}: {item['preco']} R$\n")

                    arquivo.write(f"Total do Pedido: {total_pedido} R$\n\n")

                arquivo.write(f"Total de Pedidos: {total_pedidos}\n")
                arquivo.write(f"Total Geral: {total_geral} R$\n")
            print("Bom trabalho!! O relatório foi criado sem nenhum problema.")
            print("o arquivo ficará na mesma pasta do programa com o nome: relatorio_pedidos")
            time.sleep(6)  # Pausa por 4 segundos
            os.system('cls')  # Limpa a tela

        elif escolha_menu_principal == 8:
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
