import numpy as np

# a = np.arange(1,5)
# a.shape = 2, 2
# b = np.arange(5,9)
# b.shape = 2, 2

# horizontal = np.hstack([a,b])
# vertical = np.vstack([a, b])

# print(horizontal)
# print('----------------------------')
# print(vertical)

#Разбор функции concatenate
a = np.arange(1,13)
b = np.arange(13,26)
a.resize(3, 3, 2)
b.resize(3, 3, 2)

c2 = np.concatenate([a,b], axis=2)

print(c2)