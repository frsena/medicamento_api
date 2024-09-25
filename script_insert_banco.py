from datetime import datetime
import sqlite3


db_path = "database/"

conn = sqlite3.connect('database//db.sqlite3')


sql_del = 'DELETE FROM medicamento'
conn.execute(sql_del)
conn.commit()
conn.close()