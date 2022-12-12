import psycopg2

conn = psycopg2.connect(database="chinook")
cursor = conn.cursor()
cursor.execute('SELECT * FROM "Album"')
results = cursor.fetchall()
conn.close()
for re in results:
    print(re)