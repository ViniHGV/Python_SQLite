import sqlite3

conect = sqlite3.connect("lojaPecas.db")

cursor = conect.cursor()

sql = """
  create table if not exists listaContatoFornecedor(
  idContato integer primary key autoincrement,
  codigoInterno integer,
  nomeContato string,
  emailContato string,
  telefoneContato string,
  foreign key (codigoInterno) references fornecedores(codigoInterno))
"""
cursor.execute(sql)

sql="""
  insert into listaContatoFornecedor(codigoInterno, nomeContato, emailContato, telefoneContato)
  values(1, 'Contato Fornecedora Multilazer', 'ContatoMultilazer@gmail.com', '15423521')
"""
cursor.execute(sql)

conect.commit()
cursor.close()
conect.close()

print("Criação da tabela Contatos fonecedores realizada com sucesso!!🚀")