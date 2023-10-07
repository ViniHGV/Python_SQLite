import sqlite3

conector = sqlite3.connect("lojaPecas.db")

cursor = conector.cursor()

sql = """
  create table if not exists mercadoriasPedido(
  id integer primary key autoincrement,
  notaFiscal integer,
  codigoMercadoria integer,
  quantidade integer,
  foreign key (notaFiscal) references pedidos(numNotaFiscal),
  foreign key (codigoMercadoria) references mercadorias(cod))
"""
cursor.execute(sql)

conector.commit()
cursor.close()
conector.close()

print("Tabela mercadoriaPedido criada com sucesso 🚀")