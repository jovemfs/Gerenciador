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
    print('-='*12)
    print(' Selecione uma acao:')
    print('-='*12)
    print(' i - inserir nova senha')
    print(' r - recuperar senha')
    print(' s - servicos salvos')
    print(' f - finalizar programa')
    print('-='*12)
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
