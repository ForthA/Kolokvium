from resultant_m1 import *

# Z-2
# Определение положительности числа (2 - положительное, 0 - равное нулю, 1 - отрицательное)
def POZ_Z_D(A):
    if (A[0]==1):
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
 
# N-8
# Умножение натуральных чисел
def MUL_NN_N(A, B):
    p = []
    B.reverse()
    B.append(0)
    for i in range(len(B)):
        # t - текущий разряд на который умножаем число
        t = B[i]
        # Умножаем исходное число на t
        c = MUL_ND_N(list(map(int, A)), t)
        # Умноженаем результат на 10^k, чтобы "сдвинуть" его
        c = MUL_Nk_N(list(map(int, c)), i)
        # добавляем к результату
        p = ADD_NN_N(list(map(int, p)), list(map(int, c)))
    del p[0]
    return p

# Z-6
# Сложение целых чисел
def ADD_ZZ_Z(A, B):
    result = 0
    AZ = POZ_Z_D(A)
    BZ = POZ_Z_D(B)
    if ((AZ == BZ) & (AZ == 1)):
        a = ABS_Z_N(A)
        b = ABS_Z_N(B)
        result = ADD_NN_N(a, b)
        result = MUL_ZM_Z(result)
    elif ((AZ == BZ) & (AZ == 2)):
        a = ABS_Z_N(A)
        b = ABS_Z_N(B)
        result = ADD_NN_N(a, b)
    elif ((AZ == BZ) & (AZ == 0)):
        result = 0
    else: 
        a = ABS_Z_N(A)
        b = ABS_Z_N(B)
        raz = COM_NN_D(a, b)
        if (raz == 2):
            result = SUB_NN_N(a, b)
            if (AZ == 1):
                result.insert(0,0)
                result = MUL_ZM_Z(result)
        else:
            result = SUB_NN_N(b, a)
            result.insert(0,0)
            if (BZ == 1):
                result = MUL_ZM_Z(result)
    return result
        
