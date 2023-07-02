# #Criando o Banco de Dados:
# importando o SQLite
import sqlite3 as lite

conexao = lite.connect('clientes.db')
#
# # Criando o cursor:
c = conexao.cursor()
#
# # Criando a tabela:
#
c.execute("""CREATE TABLE  clientes (
     nome text,
     sobrenome text,
     email text,
     telefone text
     )""")
#
# #Commit as mudanças:
conexao.commit()
#
# #Fechar o banco de dados:
conexao.close()
