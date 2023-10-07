import sqlite3

conector = sqlite3.connect('lojaPecas.db')

cursor = conector.cursor()

sql = """
  create table if not exists pedidos(
  notaFiscal integer primary key autoincrement,
  idCliente integer,
  valorTotal numeric,
  dataPedido date,
  foreign key (idCliente) references clientes(id))
"""
cursor.execute(sql)

conector.commit()
cursor.close()
conector.close()

print("Criação da tabela Pedidos realizada com sucesso!!🚀")