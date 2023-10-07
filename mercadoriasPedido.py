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

sql = """
  insert into mercadoriasPedido(notaFiscal, codigoMercadoria, quantidade)
  values (1, 1, 2)
"""
cursor.execute(sql)

sql="""
  UPDATE pedidos 
  SET valorTotal = (
  SELECT preco
  FROM mercadorias 
  WHERE codigoMercadoria = 1
  ) * (select quantidade
  FROM mercadoriasPedido
  WHERE codigoMercadoria = 1
  )
  WHERE(notaFiscal == 1)
"""
cursor.execute(sql)

conector.commit()
cursor.close()
conector.close()

print("Tabela mercadoriaPedido criada com sucesso 🚀")