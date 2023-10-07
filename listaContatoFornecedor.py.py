import sqlite3

# def ExibeDados(Dados):
#     strSaida = "{:2} {:30} {:11} {:30} {:>6}"
#     print(strSaida.format('id', 'nome', 'telefone', 'email', 'idFornecedor'))
#     for d in Dados:
#         print(strSaida.format(d[0], d[1], d[2], d[3], d[4]))

conect = sqlite3.connect("lojaPecas.db")

cursor = conect.cursor()

sql = """
  create table if not exists contatoFornecedor(
  idContato integer primary key autoincrement,
  codigoInterno integer,
  nomeContato string,
  emailContato string,
  telefoneContato string,
  foreign key (codigoInterno) references fornecedores(codigoInterno))
"""
cursor.execute(sql)

conect.commit()
cursor.close()
conect.close()

print("\n\nCriação da tabela Contatos fonecedores realizada com sucesso!!🚀\n\n")