import sqlite3

conector = sqlite3.connect("lojaPecas.db")

cursor = conector.cursor()

sql = """
  create table if not exists mercadoriaPedido(
  id integer primary key autoincrement,
  notaFiscal integer,
  codigoMercadoria integer,
  quantidade integer,
  foreign key (numNotaFiscal) references pedidos(numNotaFiscal),
  foreign key (codMercadoria) references mercadorias(cod))
"""
cursor.execute(sql)

conector.commit()
cursor.close()
conector.close()

print("Tabela mercadoriaPedido criada com sucesso 🚀")