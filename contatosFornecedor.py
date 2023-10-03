import sqlite3

conect = sqlite3.connect("lojaPecas.db")

cursor = conect.cursor()

sql = """
  create table if not exists contatoFornecedor(
  id integer primary key autoincrement,
  nome string,
  telefone string,
  email string,
  idFornecedor integer,
  foreign key (idFornecedor) references mercadorias(id))
"""
cursor.execute(sql)

sql = """
  insert into contatoFornecedor (nome, telefone, email, idFornecedor)
  values ('Vinicius Fornecedor', '11914186155', 'ixxvinicius@gmail.com', 1)
"""
cursor.execute(sql)

conect.commit()
cursor.close()
conect.close()

print("Criação da tabela Contatos fonecedores realizada com sucesso!!🚀")