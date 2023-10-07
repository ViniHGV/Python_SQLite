import sqlite3

conect = sqlite3.connect("lojaPecas.db")

cursor = conect.cursor()

sql = """
  create table if not exists mercadorias(
  codigoMercadoria integer primary key autoincrement,
  descricao string,
  preco numeric,
  qtdEstoque integer)
"""
cursor.execute(sql)

conect.commit()
cursor.close()
conect.close()

print("Criação da tabela Mercadorias realizada com sucesso!!🚀")
