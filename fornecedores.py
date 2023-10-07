import sqlite3

conect = sqlite3.connect("lojaPecas.db")

cursor = conect.cursor()

sql = """
  create table fornecedores (
  codigoInterno integer primary key autoincrement,
  razaoSocial string,
  nomeFantasia string,
  cnpj string,
  endereco string,
  telefoneCentral string)
"""
cursor.execute(sql)

conect.commit()
cursor.close()
conect.close()

print("Criação da tabela Fornecedores realizada com sucesso!!🚀")