import numpy as np

a = np.array([1, 2, 3, 4])
print(a)

# for el in a:
#     print(el)

print(a.dtype)
print(a[0])

# a[0] = 234

# print(a[0])
print(a[[0,0,0,0,0,0]])
print(a[[True, False, False, True]])

print(a.reshape(2,2)) #переделывает в марицу 2 на 2