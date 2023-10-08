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

sql = """
  insert into clientes(nome, rg, cpf, endereco, email, numTelefone, numCelular)
  values('Vinicius', '152154785', '125412541236', 'Rua Athos Palma', 'vinicius@gmail.com', '512452158', '11123456984')
"""
cursor.execute(sql)

sql = """
  insert into clientes(nome, rg, cpf, endereco, email, numTelefone, numCelular)
  values('Caic', '152154786', '125412541237', 'Rua Athos Palma', 'Caic@gmail.com', '512452159', '11123456985')
"""
cursor.execute(sql)

sql = """
  insert into clientes(nome, rg, cpf, endereco, email, numTelefone, numCelular)
  values('Guilherme', '152154787', '125412541238', 'Rua Athos Palma', 'Guilherme@gmail.com', '512452150', '11123456986')
"""
cursor.execute(sql)

sql = """
  insert into clientes(nome, rg, cpf, endereco, email, numTelefone, numCelular)
  values('Valdemar', '152154788', '125412541239', 'Rua Athos Palma', 'Valdemar@gmail.com', '512452151', '11123456987')
"""
cursor.execute(sql)

conector.commit()
cursor.close()
conector.close()

print("Criação da tabela Clientes realizada com sucesso!!🚀")
