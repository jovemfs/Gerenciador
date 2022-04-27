import sqlite3  # importacao

MASTER_PASSWORD = "senhateste"

# verificacao de senha mestre
senha = input('Entrar com a senha para execucao:  ')
if senha != MASTER_PASSWORD:
    print('Senha incorreta. Fim da execucao do programa.')
    exit()
# fim da verificacao de senha mestre

conn = sqlite3.connect('senhas.db')  # conexao com banco
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
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')
# exec de tabela de usuario
# criacao senhas.db, arquivo binario


def menu():
    print('-=' * 15)
    print(seguranca)
    print('-='*15)
    print(' Selecione uma acao:')
    print('-='*15)
    print(' i - inserir nova senha')
    print(' r - recuperar senha')
    print(' l - servicos salvos')
    print(' s - finalizar programa')
    print('-='*15)
# terminal com as funcoes disponiveis p exec


def get_password(service):
    cursor.execute(f'''
        SELECT username, senha FROM users
        WHERE service = '{service}'
    ''')

    if cursor.rowcount == 0:
        print("Voce nao cadastrou esse servico (use 's' para verificar servicos")
    else:
        for user in cursor.fetchall():
            print(user)

# inserir senha
def insert_password(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password)
        VALUES ('{service}', '{username}', '{password}')
    ''')
    conn.commit()
# inserir senha

# mostrar servicos
def show_services():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)
# mostrar servicos


while True:
    menu()
    op = input('Qual sua acao?  ')
    if op not in ['l', 'i', 'r', 's']:
        print('Acao nao existente. Favor selecionar uma valida.')
        continue

    if op == 's':
        break

    if op == 'i':
        service = input('Nome do servico:  ')
        username = input('Nome de usuario:  ')
        password = input('Senha:  ')
        insert_password(service, username, password)

    if op == 'l':
        show_services()

    if op == 'r':
        service = input('Qual o servico para qual quer a senha?  ')
        get_password(service)

conn.close()
