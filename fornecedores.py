import sqlite3

conect = sqlite3.connect("lojaPecas.db")

cursor = conect.cursor()

sql = """
  create table if not exists fornecedores (
  codigoInterno integer primary key autoincrement,
  razaoSocial string,
  nomeFantasia string,
  cnpj string,
  endereco string,
  telefoneCentral string)
"""
cursor.execute(sql)

sql="""
  insert into fornecedores(razaoSocial, nomeFantasia, cnpj, endereco, telefoneCentral)
  values('Multilazer','Multilazer', '1445214521', 'Rua Adolfo', '12456215')
"""
cursor.execute(sql)

conect.commit()
cursor.close()
conect.close()

print("Criação da tabela Fornecedores realizada com sucesso!!🚀")