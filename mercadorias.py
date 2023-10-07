import sqlite3

conect = sqlite3.connect("lojaPecas.db")

cursor = conect.cursor()

sql = """
  create table if not exists mercadorias(
  codigoMercadoria integer primary key autoincrement,
  descricao string,
  preco numeric,
  quantidadeEstoque integer)
"""
cursor.execute(sql)

sql = """
  insert into mercadorias (descricao, preco, quantidadeEstoque)
  values ('Mouse', 59.99, 10)
"""
cursor.execute(sql)

sql = """
  insert into mercadorias (descricao, preco, quantidadeEstoque)
  values ('Teclado Gamer', 259.99, 15)
"""
cursor.execute(sql)

conect.commit()
cursor.close()
conect.close()

print("Criação da tabela Mercadorias realizada com sucesso!!🚀")
