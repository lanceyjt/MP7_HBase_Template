import happybase as hb

conn = hb.Connection('localhost')

print(conn.tables())