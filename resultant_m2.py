from resultant_m1 import *


# Z-1
# Модуль целого числа: первый элемент заменяем на 0
def ABS_Z_N(A):
    B = A[:]
    B[0] = 0
    return B


# Z-2
# Определение положительности числа (2 - положительное, 0 - равное нулю, 1 - отрицательное)
def POZ_Z_D(A):
    if A[0] == 1:
        return 1
    elif isZero(A):
        return 0
    else:
        return 2


# Проверка на ноль
def isZero(A):
    for i in range(len(A)):
        if A[i]:
            return False
    return True


# Z-3 Умножение целого на -1. Алгоритм проверяет, если число положительное, то есть первый индекс массива равно нулю,
# то заменяем на противоположный знак, иначе ничего не меняем.
def MUL_ZM_Z(A):
    if A[0] == 0:
        A[0] = 1
    else:
        A[0] = 0
    return A


# Z-4
# Преобразование массива цифр натурального числа в целое число
def TRANS_N_Z(A):
    A = [0] + A
    return A


# Z-5
# Перевод из целого в натуральное: удаляем первый элемент
def TRANS_Z_N(A):
    B = A[:]
    if B[0] == 0:
        B.pop(0)
    else:
        print("ERROR IN MODULE :TRANS_Z_N")
    return B


# Z-6
# Сложение целых чисел
def ADD_ZZ_Z(A, B):
    result = 0
    AZ = POZ_Z_D(A)
    BZ = POZ_Z_D(B)
    if (AZ == BZ) & (AZ == 1):
        a = ABS_Z_N(A)
        b = ABS_Z_N(B)
        result = ADD_NN_N(a, b)
        result = MUL_ZM_Z(result)
    elif (AZ == BZ) & (AZ == 2):
        a = ABS_Z_N(A)
        b = ABS_Z_N(B)
        result = ADD_NN_N(a, b)
    elif (AZ == BZ) & (AZ == 0):
        result = 0
    else:
        a = ABS_Z_N(A)
        b = ABS_Z_N(B)
        raz = COM_NN_D(a, b)
        if raz == 2:
            result = SUB_NN_N(a, b)
            if AZ == 1:
                result.insert(0, 0)
                result = MUL_ZM_Z(result)
        else:
            result = SUB_NN_N(b, a)
            result.insert(0, 0)
            if BZ == 1:
                result = MUL_ZM_Z(result)
    return result
