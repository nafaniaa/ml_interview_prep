# with open('Python_OOP/pi_digits.txt') as file_object:
#     contents = file_object.read()

# print(contents)


#это я добавляла каждую строку в список сама:
# my_list = []

# with open('Python_OOP/pi_digits.txt') as file_object:
#     for line in file_object:
#         my_list.append(line.rstrip())


# print(my_list)

#а так это показано в книге:

# with open('Python_OOP/pi_digits.txt') as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())


#запись в пустой файл

filename = 'Python_OOP/programming.txt'

with open(filename , 'w') as file_object:
    file_object.write('I love programming!')

with open(filename) as file_obj:
    content = file_obj.read()

print(content)


with open(filename, 'a') as file_obj:
    file_obj.write('\nand money;)')

with open(filename) as file_obj:
    content = file_obj.read()

print(content)


