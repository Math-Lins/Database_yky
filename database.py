import csv
import uuid
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider 

# Conexão com o Cassandra
auth_provider = PlainTextAuthProvider(username='seu_usuario', password='sua_senha')
cluster = Cluster(['127.0.0.1'], auth_provider=auth_provider)
session = cluster.connect()

# Seleção do keyspace
session.set_keyspace('kaggle_data')

# Abrir o arquivo CSV e inserir dados no Cassandra
with open('imdb_top_2000_movies.csv', 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        session.execute(
            """
            INSERT INTO data (id, column1, column2, column3, column4, column5, column6, column7, column8, column9, column10)
            VALUES (%(id)s, %(Movie_Name)s, %(Release_Year)s, %(Duration)s, %(IMDB_Rating)s, %(Metascore)s, %(Votes)s, %(Genre)s, %(Director)s, %(Cast)s, %(Gross)s);
            """,
            {
                "id": uuid.uuid4(),
                "Movie_Name": row['Movie Name'],
                "Release_Year": int(row['Release Year']),
                "Duration": int(row['Duration']),
                "IMDB_Rating": float(row['IMDB Rating']),
                "Metascore": float(row['Metascore']),
                "Votes": int(row['Votes']),
                "Genre": row['Genre'],
                "Director": row['Director'],
                "Cast": row['Cast'],
                "Gross": float(row['Gross'])
            }
        )

# Fechar a conexão
cluster.shutdown()
