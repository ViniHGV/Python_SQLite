import sqlite3

conector = sqlite3.connect('lojaPecas.db')

cursor = conector.cursor()

sql = """
  create table if not exists pedidos(
  id integer primary key autoincrement,
  valorTotal STRING,
  dataRealizacao DATETIME,
  mercadorias STRING)
"""
cursor.execute(sql)

sql = """
  insert into pedidos ( valorTotal, mercadorias)
  values ('R$ 150,00', 'Chave de Fenda')
"""
cursor.execute(sql)

conector.commit()
cursor.close()
conector.close()

print("Criação da tabela Pedidos realizada com sucesso!!🚀")