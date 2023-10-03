import sqlite3

conector = sqlite3.connect("lojaPecas.db")

cursor = conector.cursor()

sql = """
  create table if not exists clientes  (
  id integer primary key autoincrement,
  nome string,
  RG string,
  CPF string,
  endereco string,
  email string,
  fixo string,
  celular string)
"""
cursor.execute(sql)

sql = """
  insert into clientes (nome, RG, CPF, endereco, email, fixo, celular)
  values ('vinicius', '576558837', '57425932873', 'rua athos palma', 'ixxvinicius', '56742747', '914186155')
"""
cursor.execute(sql)

conector.commit()
cursor.close()
conector.close()

print("Criação da tabela Clientes realizada com sucesso!!🚀")