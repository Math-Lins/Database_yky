import mysql.connector
import os

os.system('cls')

meubd = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='34271573',
    database=''
)

cursor = meubd.cursor()
cursor.execute("SHOW DATABASES LIKE'crud'")

resultadoDB = cursor.fetchone()

if resultadoDB:
    print(("O Banco de Dados já existe."))
else:
    print("Criando Banco de Dados...")
    cursor.execute("CREATE DATABASE crud")

    print("Banco de Dados criado com sucesso!")

cursor.execute("USE crud")
cursor.execute("SHOW TABLES LIKE'clientes'")

resultadoTable = cursor.fetchone()

if resultadoTable:
    print(("\nA Tabela já existe."))
else:
    print("\nCriando Tabela...")
    cursor.execute("CREATE TABLE clientes(id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), email VARCHAR(255))")
    print("Tabela criada com sucesso!")

sql = "INSERT INTO clientes (nome, email) VALUES (%s,%s)"
dados = ("Diego Sawyer", "dhrsawyer@teste.email.com")

cursor.execute(sql, dados)
meubd.commit()
print("\nDados inseridos com sucesso!")