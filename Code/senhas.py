import sqlite3

MASTER_PASSWORD = "senhateste"

senha = input("Insira a senha de entrada:  ")
if senha != MASTER_PASSWORD:
    print("Senha incorreta. Fim da execucao.")
    exit()
# verificacao de senha mestre

conn = sqlite3.connect('passwords.db')

seguranca = """                               
                                   
                                                      ^jEQBQDj^             
                                                   r#@@@@@@@@@#r           
                                                   ?@@@#x_`_v#@@@x          
                                                   g@@@!     !@@@Q          
                                                   Q@@@_     _@@@B          
                                                rgg@@@@QgggggQ@@@@ggr       
                                                Y@@@@@@@@@@@@@@@@@@@Y       
                                                Y@@@@@@@Qx^xQ@@@@@@@Y       
                                                Y@@@@@@@^   ~@@@@@@@Y       
                                                Y@@@@@@@@r r#@@@@@@@Y       
                                                Y@@@@@@@@c,c@@@@@@@@Y       
                                                Y@@@@@@@@@@@@@@@@@@@Y       
                                                v###################v       
                                                   
                                                                
    """

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS user (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')
# exec de tabela de usuario
# criacao passwords.db, arquivo q vai funcionar como bando de dados


def menu():
    print("-="*55)
    print(seguranca)
    print("-="*55)
    print(' Selecione uma acao:')
    print("-="*55)
    print(' i - inserir nova senha')
    print(' r - recuperar senha')
    print(' l - servicos salvos')
    print(' s - finalizar programa')
    print("-="*55)
# terminal com as funcoes disponiveis p exec


def get_password(service):
    cursor.execute(f'''
        SELECT (username, password) FROM users
        WHERE service = '{service}'
    ''')

    if cursor.rowcount == 0:
        print("Voce nao cadastrou o servico (digite 'i' para ver a lista)")
    else:
        for user in cursor.fetchall():
            print(service)


def insert_password(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password)
        VALUES ('{service}', '{username}', '{password}')
    ''')
    conn.commit()
# inserir senha


def show_services():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)
# mostrar servicos


while True:
    menu()
    op = input("Qual acao deseja realizar?  ")
    if op not in ['l', 'i', 'r', 's']:
        print("Acao nao existente. Favor selecionar uma valida.")
        continue

    if op == 's':
        break

    if op == 'i':
        service = input('Servico:  ')
        username = input('Nome de usuario:  ')
        password = input('Senha:  ')
        insert_password(service, username, password)

    if op == 'l':
        show_services()

    if op == 'r':
        service = input('Qual o servico para qual quer a senha?  ')
        get_password(service)

conn.close()
