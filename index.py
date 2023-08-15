print ("Olá, bem-vindo(a) ao PPizzas.2!")
print ("Essa será a segunda versão melhorada do meu primeiro contato com programação,\num programa para uma pizzaria que encontra-se no link:")
print ("https://github.com/mateusmoraiss/projeto-pizzaria-C")
print ("\n  \n")
print ("Tá, mas qual a diferença entre eles?")
print ("Trarei algumas melhorias significativas, deixando-o mais prático e funcional")
print ("Algumas das melhorias:")
print ("1) Banco de dados local.")
print ("2) Mais funcional.")
print ("3) Gerar relatórios de vendas, clientes etc...")
print ("4) Melhores práticas de código.")
print ("5) Melhores práticas de experiência.")
print ("6) Dashboard do estoque.")
print ("7) Linguagem mais moderna.")
print("\nManual no README do GitHub:")
print("https://github.com/mateusmoraiss/ppizzas.2/blob/main/README.md")
print("Onde deixei as senhas específicas para acessar o programa com os respectivos direitos.")

'''    CRIAÇÃO DOS DBAS             '''
import sqlite3

conn = sqlite3.connect("estoque.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS estoque (
                    item TEXT PRIMARY KEY,
                    quantidade INTEGER
                )''')

cursor.execute("SELECT COUNT(*) FROM estoque")
num_rows = cursor.fetchone()[0]

if num_rows == 0:
    itens_iniciais = [
        ("massa", 425), ("molho", 10000), ("calabresa", 10000), ("queijo", 10000),
        ("presunto", 10000), ("ovo", 432), ("bacon", 8000), ("catupiry", 6000),
        ("cheddar", 6000), ("cebola", 87), ("oregano", 500), ("caramelo", 5000),
        ("pimentao", 67), ("manjericao", 1000), ("banana", 100), ("canela", 1000),
        ("chocolate", 10000), ("frango", 15000), ("milho", 7000), ("doce", 12000),
        ("azeitona", 11000), ("tomate", 56), ("gjesus", 180), ("dolly", 180),
        ("goianinho", 180), ("mineiro", 180), ("bare", 180), ("itubaina", 180),
        ("fresh", 99), ("delvalle", 99), ("kaiser", 240)
    ]
    cursor.executemany("INSERT INTO estoque (item, quantidade) VALUES (?, ?)", itens_iniciais)
    print("\n\n\n\nAhh, mais uma coisa!\nComo essa é a primeira vez que o programa é aberto, estou criando os arquivos essenciais para o funcionamento.")
    print("Por favor, não apague nada. Se algo for excluído acidentalmente, basta executar este programa novamente.")


    conn.commit()

conn.close()
print("Atenciosamente, Mateus! :)")
input("")


