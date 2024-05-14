import csv
import uuid
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Connect to the Cassandra database
auth_provider = PlainTextAuthProvider(username='your_username', password='your_password')
cluster = Cluster(['127.0.0.1'], auth_provider=auth_provider)
session = cluster.connect()

# Create a keyspace and table in the Cassandra database
session.execute("CREATE KEYSPACE IF NOT EXISTS kaggle_data WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};")
session.set_keyspace('kaggle_data')
session.execute("CREATE TABLE IF NOT EXISTS data (id UUID PRIMARY KEY, column1 text, column2 int);")

# Read data from a .csv file and insert it into the Cassandra database
with open('IMDb_Top_2000_Movies.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        session.execute("INSERT INTO data (id, column1, column2) VALUES (%s, %s, %s);", (uuid.uuid4(), row['column1'], row['column2']))

# Update data in the Cassandra database
session.execute("UPDATE data SET column1 = 'updated_value' WHERE id = your_uuid;")

# Read data from the Cassandra database
rows = session.execute("SELECT * FROM data;")
for row in rows:
    print(row)

# Delete data from the Cassandra database
session.execute("DELETE FROM data WHERE id = your_uuid;")

# Close the connection to the Cassandra database
cluster.shutdown()
