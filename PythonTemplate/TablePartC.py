import happybase as hb
import csv

conn = hb.Connection('localhost')
table = conn.table('powers')

with open('input.csv', newline='') as csvfile:
     reader = csv.reader(csvfile, delimiter=',')
     for r in reader:
        table.put(r[0], {b'personal:hero': r[1],
                         b'personal:power': r[2],
                         b'professional:name': r[3],
                         b'professional:xp': r[4],
                         b'custom:color': r[5]})
