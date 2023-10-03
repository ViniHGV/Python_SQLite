import sqlite3

conect = sqlite3.connect("lojaPecas.db")

cursor = conect.cursor()

sql = """
  create table if not exists mercadorias(
  id integer primary key autoincrement,
  cod integer,
  descricao string,
  preco numeric,
  qtdEstoque integer,
  idPedido integer,
  foreign key (idPedido) references pedidos(id))
"""
cursor.execute(sql)

sql = """
  insert into mercadorias(cod, descricao, preco, qtdEstoque, idPedido)
  values (21515, 'Chave de Fenda muito boa', 25.00, 25, 1)
"""
cursor.execute(sql)

sql = """
  insert into mercadorias(cod, descricao, preco, qtdEstoque, idPedido)
  values (21515, 'Chave de Boca', 25.00, 25, 1)
"""
cursor.execute(sql)

conect.commit()
cursor.close()
conect.close()

print("Criação da tabela Mercadorias realizada com sucesso!!🚀")
