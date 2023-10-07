import sqlite3
import datetime

conector = sqlite3.connect('lojaPecas.db')

cursor = conector.cursor()

Data = datetime.date.today()

sql = """
  create table if not exists pedidos(
  notaFiscal integer primary key autoincrement,
  idCliente integer,
  valorTotal numeric,
  dataPedido string,
  foreign key (idCliente) references clientes(id))
"""
cursor.execute(sql)

sql = f"""
  insert into pedidos(idCliente, dataPedido)
  values(1, {Data})
"""
cursor.execute(sql)

conector.commit()
cursor.close()
conector.close()

print("Criação da tabela Pedidos realizada com sucesso!!🚀")