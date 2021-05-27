import psycopg2

HOST_NAME = 'localhost'
DB_NAME = 'abhishek'
USER = 'abhishek'
PASSWORD = 'abhishek'

# SCEMA_NAME.TABLE_NAME
TABLE_NAME = 'information.employees'
ID = 'id'
NAME = 'name'

def fetchRows():
    # EXECUTE SELECT-QUERY
    cur.execute(f"SELECT * FROM {TABLE_NAME};")

    # FETCH
    rows = cur.fetchall()
    for row in rows:
        print(f"id:{row[0]} & name: {row[1]}")

# CONNECT TO DB
con = psycopg2.connect(host=HOST_NAME, database=DB_NAME, user=USER, password=PASSWORD)

# CREATE CURSOR
cur = con.cursor()

# EXECUTE QUERY
cur.execute(f"CREATE TABLE {TABLE_NAME}({ID} integer, {NAME} text);")

# EXECUTE INSERT-QUERY
cur.execute(f"INSERT INTO {TABLE_NAME}({ID}, {NAME}) VALUES('1', 'abhi');")

# EXECUTE INSERT-QUERY
cur.execute(f"INSERT INTO {TABLE_NAME}({ID}, {NAME}) VALUES('2', 'shek');")

# EXECUTE INSERT-QUERY
cur.execute(f"INSERT INTO {TABLE_NAME}({ID}, {NAME}) VALUES('3', 'patil');")

fetchRows()

# EXECUTE UPDATE-QUERY
cur.execute(f"UPDATE {TABLE_NAME} SET {NAME} = 'PATEL' WHERE {ID} = 3;")

fetchRows()

# EXECUTE DELETE-QUERY
cur.execute(f"DELETE FROM {TABLE_NAME} WHERE {ID} = 3;")

fetchRows()


# COMMIT YOU ACTIONS
con.commit()

# CLOSE CURSOR
cur.close()

# CLOSE DB
con.close()