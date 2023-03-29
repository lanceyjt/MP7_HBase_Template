import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER
conn = hb.Connection('localhost')
table = conn.table('powers')

name_lst = []
power_lst = []
color_lst = []
for key, data in table.scan(include_timestamp=False):
    name_lst.append(data[b'professional:name'])
    power_lst.append(data[b'personal:power'])
    color_lst.append(data[b'custom:color'])

res = []
num = len(name_lst)
for i in range(num):
    for j in range(num):
        if color_lst[i] == color_lst[j] and name_lst[i] != name_lst[j]:
            
            color = color_lst[i]
            name = name_lst[i]
            power = power_lst[i]

            color1 = color_lst[j]
            name1 = name_lst[j]
            power1 = power_lst[j]

            print('{}, {}, {}, {}, {}'.format(name, power, name1, power1, color))


