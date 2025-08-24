import numpy as np

# np.random.seed(2)
# a = np.random.randint(10, size = 15)
# print(a)

#делаем из массива множество
# setA = np.unique(a)
# print(setA)

# параметр return_counts = True вернёт ещё массив с количеством поавторений
# setA = np.unique(a, return_counts = True)
# print(setA)

# параметр return_index= True позволяет определять индексы первого вхождения
# уникальных элементов
# параметр return_inverse = True возвращает массив, по котором уможно воостановить исходный массив

x = np.arange(4)
y = np.arange(1, 9)

# Метод np.in1d(x, y) показывает
# какие элементы из мн-ва y входят в
# множество x
print(np.in1d(x, y))