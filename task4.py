import numpy as np
from scipy import sparse
import time

def subtask1():
    print("Задача 4.1")
    rng = np.random.default_rng(seed=42)
    A = sparse.random(5, 5, density=0.2, format='csr', random_state=rng)
    print("Матрица A (CSR):")
    print(A.toarray())
    print(f"Формат: {A.format}, ненулевых элементов: {A.nnz} из {5 * 5}")
    return A

def subtask2(A):
    print("Задание 4.2")
    A_coo = A.tocoo()
    A_csc = A.tocsc()
    print(f"CSR: {A.format}, nnz = {A.nnz}")
    print(f"COO: {A_coo.format}, nnz = {A_coo.nnz}")
    print(f"CSC: {A_csc.format}, nnz = {A_csc.nnz}")
    return A_coo, A_csc

def subtask3(A):
    print("Задание 4.3")
    x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    result = A @ x
    print(f"Вектор x: {x}")
    print(f"A @ x = {result}")

def subtask4():
    print("Задание 4.4")
    rng = np.random.default_rng(seed=42)
    n = 1000
    density = 0.01
    A_sparse = sparse.random(n, n, density=density, format='csr', random_state=rng)
    A_dense = A_sparse.toarray()
    x = rng.random(n)
    t0 = time.perf_counter()
    for _ in range(10):
        _ = A_sparse @ x
    t_sparse = (time.perf_counter() - t0) / 10
    t0 = time.perf_counter()
    for _ in range(10):
        _ = A_dense @ x
    t_dense = (time.perf_counter() - t0) / 10
    print(f"Разреженная матрица: nnz = {A_sparse.nnz} из {n * n}")
    print(f"Время умножения разреженной: {t_sparse * 1000:.4f} мс")
    print(f"Время умножения плотной:  {t_dense * 1000:.4f} мс")
    print(f"Разреженная быстрее в {t_dense / t_sparse:.1f} раз")

A = subtask1()
subtask2(A)
subtask3(A)
subtask4()

