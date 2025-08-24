import numpy as np

a = np.arange(12)
# print(a[0])
# print(a[-1])

# print(a[2:5])
# print(a[::-1])
# print(a[0::2])

# for x in a:
#     print(x, sep = ' ', end = ' ')

arr = np.arange(9)
arr.shape = 3, 3

# print(arr)

# for row in arr:
#     for col in row:
#         print(col, sep = ' ', end = ' ')

#вывод второго столбца
# print(arr[:, 1])

# print(arr[0:2,0:2])

#альтернатива for

# for val in arr.flat:
#     print(val, end = ' ')

#булева списочная индексация

# array = np.array([1, 5, 7, 2, 3, 99, 1 ,4])
# i = array > 5
# print(i) #[False False  True False False  True False False]
# print(array[i]) #[ 7 99]
# print(array[array > 4])


#списочная многомерная индексация для  массивов
# a = np.arange(1,10)
# print(a)
# i = np.array([[0, 1], 
#               [2, 3]]) #обязательно использовать np
# print('-----------------------------------')
# print(a[i]) 
# [[1 2]
#  [3 4]]


#списочная индексация для многомерных массивов
a = np.arange(1,13).reshape(3, 4)
print(a)
print("--------------------------------------------")
# indx = [2, 1, 0]
# print(a[indx]) #вывел строки в обратном порядке

# indx = np.array([[1, 0], [2, 1]])
# print(a[indx]) #получаем трёхмерный массив

#как выбрать столбцы из матрицы
i0 = [0, 1] #выбирает строки
i1 = [1, 2] # 1 - второй элемент из первой строки, 2 - третий элемент из второй строки
print(a[i0, i1]) #[2 7]

print('------------------------')
print(a[:,i1])
#взяли все сстроки, и два столбца