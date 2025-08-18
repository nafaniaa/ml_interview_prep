import numpy as np

# a = np.arange(10)
# print(a)

# a.shape = 2, 5
# print(a)

# b = a.reshape(10)

#разноые представления, но данные те же
# print(b)
# print(a)

# b.shape = -1, 5
# print(b)

# x_test = np.arange(32).reshape(8, 2, 2)

# #добавляем ось
# x_test4 = np.expand_dims(x_test, axis=0)

# print(x_test4.shape)

# a = np.append(x_test4, x_test4, axis = 0)
# print(a.shape)

a = np.arange(10)

b = a[np.newaxis, :]
print(b.shape)