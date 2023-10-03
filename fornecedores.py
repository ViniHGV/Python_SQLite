import sqlite3

conect = sqlite3.connect("lojaPecas.db")

cursor = conect.cursor()

sql = """
  create table fornecedores (
  id integer primary key autoincrement,
  razaoSocial string,
  nomeFantasia string,
  CNPJ string,
  endereco string,
  telefoneCentral string,
  idPessoas integer,
  foreign key (idPessoas) references clientes(id))
"""
cursor.execute(sql)

sql = """
  insert into fornecedores (razaoSocial, nomeFantasia, CNPJ, endereco, telefoneCentral, idPessoas)
  values ('Ajudar pessoas Solidarias', 'Loja do seu Zé', '574.455.214/415-55', 'Rua do Seu Zé', '56742747', 1)
"""
cursor.execute(sql)

conect.commit()
cursor.close()
conect.close()

print("Criação da tabela Fornecedores realizada com sucesso!!🚀")