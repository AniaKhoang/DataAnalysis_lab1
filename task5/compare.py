import time
from sum_squares_p import sum_p
from sum_squares_c import sum_c

n = 10_000_000
start = time.perf_counter()
res_py = sum_p(n)
time_py = time.perf_counter() - start
start = time.perf_counter()
res_cy = sum_c(n)
time_cy = time.perf_counter() - start
print(f"Python:  {time_py:.4f} сек, результат = {res_py}")
print(f"Cython:  {time_cy:.4f} сек, результат = {res_cy}")