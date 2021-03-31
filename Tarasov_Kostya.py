# Оставляем описание каждого алгоритма

# Сравнение чисел, если первое больше второго вывод - 2, если второе больше - 1,равны - 0
def COM_NN_D(A, B):
    i = 0
    if len(A) > len(B):
        return 2
    elif len(A) < len(B):
        return 1
    else:
        while 1:
            if A[i] > B[i]:
                return 2
            elif A[i] < B[i]:
                return 1
            elif (A[i] == B[i]) & (i == (len(A) - 1)):
                return 0
            i += 1

# Проверка на ноль, если ноль - нет, если не ноль - да
def NZER_N_B(A):
    if A[0] != 0:
        print("Да")
    else:
        print("Нет")
