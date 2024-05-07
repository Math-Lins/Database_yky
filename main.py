import mysql.connector
import os

os.system('cls')

meubd = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='********',
    database=''
)

cursor = meubd.cursor()
cursor.execute("SHOW DATABASES LIKE'meu_banco_de_dados'")

resultado = cursor.fetchall()

if resultado:
    print(("O Banco de Dados já existe."))
else:
    print("Criando Banco de Dados...")
    cursor.execute("CREATE DATABASE meu_banco_de_dados")

    print("Banco de Dados criado com sucesso!")
