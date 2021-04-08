from Fedotov_Alexander import *
from Kalimullin_Roman import *
from Tarasov_Kostya import *

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
    # Меняем местами, если нужно, в b - меньшее
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

