from pg_python.pg_python import *

HOST_NAME = 'localhost'
DB_NAME = 'abhishek'
USER = 'abhishek'
PASSWORD = 'abhishek'

# SCEMA-NAME.TABLE_NAME
TABLE_NAME = 'information.employees'
ID = 'id'
NAME = 'name'

def fetchRows():
    value_list = read(TABLE_NAME, [ID, NAME], {})
    print(value_list)

pgs = pg_server(DB_NAME, USER, PASSWORD, HOST_NAME, server='default', application_name='pg_python')

# READ BEFORE WRITE FROM DB
fetchRows()

# WRITE TO DB
write(TABLE_NAME, {ID: 1, NAME:'NAME_FROM_PGPYTHON'})
# WRITE TO DB
write(TABLE_NAME, {ID: 2, NAME:'NAME_FROM_PGPYTHON'})
# READ AFTER WRITE FROM DB
fetchRows()

# UPDATE TO DB
update(TABLE_NAME, {NAME:'OVERWRITTEN_VALUE'}, {ID:1})
# READ AFTER WRITE FROM DB
fetchRows()

# DELETE FROM DB
delete(TABLE_NAME, {ID:1})
# READ AFTER WRITE FROM DB
fetchRows()
