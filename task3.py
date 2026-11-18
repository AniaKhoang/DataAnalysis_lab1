import numpy as np
import os
import timeit

def subtask1(filename = "array_dat"):
    print("Задание 3.1")
    shape = (1000, 1000)
    fp = np.memmap(filename, dtype=np.float32, mode='w+', shape=shape)
    fp[:] = np.random.rand(*shape)
    fp.flush()
    return fp

def subtask2(fp):
    print("Задание 3.2")
    row = fp[400, :]
    col = fp[:, 600]
    print(f"Строка 400 (первые 5): {row[:5]}")
    print(f"Столбец 600 (первые 5): {col[:5]}")

def subtask3(fp):
    print("Задание 3.3")
    t_rows = timeit.timeit('fp.sum(axis=1)', globals=dict(fp=fp), number=10)
    print(f"Сумма по строкам: {t_rows} сек")
    t_cols = timeit.timeit('fp.sum(axis=0)', globals=dict(fp=fp), number=10)
    print(f"Сумма по столбцам: {t_cols} сек")
    print("Сумма по строкам быстрее, потому что элементы строки лежат в памяти подряд.\nЭлементы столбца разнесены в памяти на 8000 байт")

fp = subtask1()
subtask2(fp)
subtask3(fp)
del fp
os.remove("array_dat")
