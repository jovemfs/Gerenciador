import sqlite3  # importacao

MASTER_PASSWORD = "senhateste"

conn = sqlite3.connect('senhas.db')  # conexao com banco

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
    print('''                      
           ^jEQBQDj^             
          #@@@@@@@@@#           
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
     v###################v       ''')
    print('-='*15)
    print(' Selecione uma acao:')
    print('-='*15)
    print(' i - inserir nova senha')
    print(' r - recuperar senha')
    print(' s - servicos salvos')
    print(' f - finalizar programa')
    print('-='*15)
# terminal com as funcoes disponiveis p exec

while True:
    menu()
    op = input('Qual sua acao?  ')
    if op not in ['i', 'r', 's', 'f']:
        print('Acao nao existente. Favor selecionar uma valida.')
        continue
    if op == 'f':
        break

conn.close()
