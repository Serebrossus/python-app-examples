# https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html - здесь описание
import sqlite3
sqlite_file = 'C:/Users/alexm/Dropbox/Programming/Python/testdb.sqlite'
table_name = 'my_table'
id_field = 'id'
id_field_type = 'INTEGER'
name_field = 'name'
name_field_type = 'STRING'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
create_table_query = 'CREATE TABLE {tn} ({nf1} {ft1} PRIMARY KEY, {nf2} {ft2})'\
    .format(tn=table_name, nf1=id_field, ft1=id_field_type, nf2=name_field, ft2=name_field_type)
c.execute(create_table_query)
conn.commit()
conn.close()