import sqlite3

def ExibeDados(Dados):
    strSaida = "{:2} {:30} {:11} {:30} {:>6}"
    print(strSaida.format('id', 'nome', 'telefone', 'email', 'idFornecedor'))
    for d in Dados:
        print(strSaida.format(d[0], d[1], d[2], d[3], d[4]))

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

# sql = """
#   insert into contatoFornecedor (nome, telefone, email, idFornecedor)
#   values ('Caic Fornecedor', '11914186154', 'Caic@gmail.com', 1)
# """
# cursor.execute(sql)
# sql = """
#   insert into contatoFornecedor (nome, telefone, email, idFornecedor)
#   values ('Guilherme Fornecedor', '11914186153', 'Gui@gmail.com', 1)
# """
# cursor.execute(sql)
# sql = """
#   insert into contatoFornecedor (nome, telefone, email, idFornecedor)
#   values ('André Fornecedor', '11914186152', 'André@gmail.com', 1)
# """
# cursor.execute(sql)
# sql = """
#   insert into contatoFornecedor (nome, telefone, email, idFornecedor)
#   values ('Valdemar Fornecedor', '11914186151', 'Valdemar@gmail.com', 1)
# """
# cursor.execute(sql)

sql = """
  select * from contatoFornecedor where (idFornecedor == 1)
"""
cursor.execute(sql)

findAll = cursor.fetchall()


ExibeDados(findAll)

conect.commit()
cursor.close()
conect.close()

print("\n\nCriação da tabela Contatos fonecedores realizada com sucesso!!🚀\n\n")