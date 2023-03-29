import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER
conn = hb.Connection('localhost')
table = conn.table('powers')

for key, data in table.scan(include_timestamp=True):
    print('Found: {}, {}'.format(key, data))

