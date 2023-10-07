import sqlite3

conector = sqlite3.connect("lojaPecas.db")

cursor = conector.cursor()

sql = """
  create table if not exists clientes(
  id integer primary key autoincrement,
  nome string,
  rg string,
  cpf string,
  endereco string,
  email string,
  numTelefone string,
  numCelular string)
"""
cursor.execute(sql)

conector.commit()
cursor.close()
conector.close()

print("Criação da tabela Clientes realizada com sucesso!!🚀")