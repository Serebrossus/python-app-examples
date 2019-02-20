number_list = range(-5, 5)
for number in number_list:
    print(number)

addresses = (
    ('home', 'Шаболовка', 'nice'),
    ('work', 'Варшавское шоссе', 'nice'),
    ('kremlin', 'Кремлевская набережная', 'very_nice'),
    ('previous_flat', 'Воронеж', 'below_average')
)

print(type(addresses))
print(addresses[1][2])

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)

another_list = ['n','z']
print(duplicates.intersection(another_list), duplicates.difference(another_list))
