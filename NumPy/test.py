import numpy as np
import time

# Большой массив
a = np.random.rand(1000000)

# Тест np.amax
start = time.time()
np_amax = np.amax(a)
time_np = time.time() - start

# Тест max
start = time.time()
# py_max = max(a)
max_num = a[0]
for num in a:
    if num > max_num:
        max_num = num
time_py = time.time() - start

print(f"np.amax: {time_np:.6f} сек")
print(f"max: {time_py:.6f} сек")