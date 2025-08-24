import numpy as np
# Multiplication of two matrix
# Method np.dot()

# a = np.arange(1, 10).reshape(3, 3)
# b = np.arange(10,19).reshape(3, 3)

# print(np.dot(a, b))
# print(np.dot(b, a))

# np.matmul()
# print(np.matmul(b, a))

# Multiplication of two vectors

# a = np.arange(1,10)
# b = np.ones(9) # array of nine ones

# print(np.dot(a, b)) #внутреннее умножение
# print(np.inner(a, b)) #лучше использовать для внутреннего умножения

# print(np.outer(a, b)) #внешнее умножение 
# print(np.outer(b, a))

# Inner multiplication  with @
# print( a @ b)

# Matrix multiplication wit @
# a.shape = 3, 3
# b.shape = 3, 3
# print( a @ b)

#module linalg 

a = np.vander([1,2,3], increasing= True)
print(a)

#rang of matrix
print(np.linalg.matrix_rank(a))

y =np.array([10, 20, 30])

#решение СЛАУ
print(np.linalg.solve(a, y)) #В основе лежит LU-разложение матрицы A

# Inverse matrix
invA = np.linalg.inv(a)
print(invA @ y)