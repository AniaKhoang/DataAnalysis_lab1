import numpy as np

def subtask1():
    print("Задание 1.1")
    arr = np.array([0.1, 0.2, 0.3], dtype=np.float64)
    s = np.sum(arr)
    exact = 0.1 + 0.2 + 0.3
    print(f"Сумма (float32): {s}")
    print(f"Точное значение (float64): {exact}")
    print(f"Разница: {s - exact}")

def subtask2():
    print("\nЗадание 1.2")
    for dt in (np.float32, np.float64):
        eps = np.finfo(dt).eps
        print(f"{np.dtype(dt).name}: eps = {eps}")

def subtask3():
    print("\nЗадание 1.3")
    a32 = np.float32(1.000001)
    b32 = np.float32(1.000000)
    a64 = np.float64(1.000001)
    b64 = np.float64(1.000000)
    print("a = 1.000001, b = 1.000000")
    print(f"float32: a - b = {a32 - b32}")
    print(f"float64: a - b = {a64 - b64}")

subtask1()
subtask2()
subtask3()