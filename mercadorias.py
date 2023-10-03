import sqlite3

conect = sqlite3.connect("lojaPecas.db")

cursor = conect.cursor()

sql = """
  create table mercadorias(
  id integer primary key autoincrement,
  cod integer,
  descricao string,
  preco numeric,
  qtdEstoque integer)
"""
cursor.execute(sql)

sql = """
  insert into mercadorias(cod, descricao, preco, qtdEstoque)
  values (21515, 'Chave de Fenda muito boa', 25.00, 25)
"""
cursor.execute(sql)

conect.commit()
cursor.close()
conect.close()

print("Criação da tabela Mercadorias realizada com sucesso!!🚀")
