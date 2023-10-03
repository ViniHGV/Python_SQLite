import sqlite3

conector = sqlite3.connect('lojaPecas.db')

cursor = conector.cursor()

sql = """
  create table pedidos(
  id integer primary key autoincrement,
  numNotaFiscal STRING,
  valorTotal STRING,
  dataRealizacao DATETIME,
  mercadorias STRING)
"""
cursor.execute(sql)

sql = """
  insert into pedidos (numNotaFiscal, valorTotal, mercadorias)
  values ('1235124', 'R$ 150,00', 'Chave de Fenda')
"""
cursor.execute(sql)

conector.commit()
cursor.close()
conector.close()

print("Criação da tabela Pedidos realizada com sucesso!!🚀")