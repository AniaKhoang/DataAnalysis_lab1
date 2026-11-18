import numpy as np

def subtask1():
    print("Задание 2.1")
    A = np.arange(20).reshape(4, 5)
    print("Массив (4,5)\n", A)
    print("Вторая строка: ", A[1])
    print("Столбец с индексом 3: ", A[:, 3])
    print("Подмассив из строк 1-3 и столбцов 2-4\n", A[0:3, 1:4])

def subtask2():
    print("\nЗадание 2.2")
    A = np.arange(20).reshape(4, 5)
    result = A[np.ix_([0, 2, 3], [1, 4])]
    print("Элементы [0, 2, 3] по строкам и [1, 4] по столбцам")
    print(result)

def subtask3():
    print("\nЗадание 2.3")
    A = np.array([[-1, -2, -3, -4, -5],
                  [6, 7, 8, 9, 10],
                  [-11, -12, -13, -14, -15],
                  [16, 17, 18, 19, 20],])
    print("Исходный массив: ")
    print(A)
    A[A < 0] = 0
    print("Массив после замены отрицательных на 0:")
    print(A)

def subtask4():
    print("\nЗадание 2.4")
    B = np.arange(4).reshape(4, 1)
    C = np.arange(5).reshape(1, 5)
    print("Массив B:")
    print(B)
    print("Массив C:")
    print(C)
    result = B + C
    print("B + C: ")
    print(result)

subtask1()
subtask2()
subtask3()
subtask4()