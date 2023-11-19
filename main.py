import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="190920",
    database="academiaturmad"
)
print(banco)

meucursor = banco.cursor()
pesquisa = 'select * from alunos;'
meucursor.execute(pesquisa)
# fetchall recebe tudo da pesquisa e retorna através de uma tupla
resultado = meucursor.fetchall()

for x in resultado:
    print(x)

meucursor.close()
banco.close()