#21
# person = {}
# person['name'] = 'Anna'
# person['age'] = 20
# print(person)

#22
# def get_value(dct, key):
#     if key in dct.keys():
#         return dct[key]
#     else:
#         return "Не найдено"
    
# print(get_value({'a': 1}, 'b'))

#23
# person = {'name': 'Боб', 'age': 20}
# person['age'] = 21
# print(person)

#24
# dct = {1: 10, 2: 20, 3: 30}
# print(sum(dct.values()))

#25 
# dct = {1: 5, 2: 15, 3: 10}
# new_dct = {}
# for key, value in dct.items():
#     if value > 10:
#         new_dct[key] = value

# print(new_dct)

#26
# person = {'name': 'Аня'}
# person['city'] = 'Moscow'
# print(person)

#27
# print('age' in {'name': 'Боб'})

#28
keys = ['a', 'b']
values = [1, 2]
dct = dict(zip(keys, values))

print(dct)

#29
# person = {'name': 'Аня', 'age': 25}
# del person['name']
# print(person)

#30
# dct = {'a': 1, 'b': 2, 'c': 3}
# print(len(dct.keys()))