import sqlite3

conector = sqlite3.connect('lojaPecas.db')

cursor = conector.cursor()

sql = """
  create table if not exists pedidos(
  id integer primary key autoincrement,
  valorTotal STRING,
  dataRealizacao DATE,
  mercadorias STRING,
  idCliente integer,
  foreign key (idCliente) references clientes(id))
"""
cursor.execute(sql)

sql = """
  insert into pedidos ( valorTotal, mercadorias, idCliente )
  values ('R$ 150,00', 'Chave de Fenda', 1)
"""
cursor.execute(sql)

conector.commit()
cursor.close()
conector.close()

print("Criação da tabela Pedidos realizada com sucesso!!🚀")