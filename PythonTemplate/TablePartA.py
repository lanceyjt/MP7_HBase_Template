import happybase as hb

conn = hb.Connection('localhost')

## Create table 'powers'
powers_family = {
    'personal': dict(),
    'professional': dict(),
    'custom': dict()
}
conn.create_table('powers', powers_family)

## Create table 'food'
food_family = {
    'nutrition': dict(),
    'taste': dict()
}
conn.create_table('food', food_family)