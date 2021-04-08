#Ф-ции не преобразуют входящий массив, а возвращают новый.
from resultant_m1 import *
from resultant_m2 import *

#N-7
#Умножаем на 10^k: добавляем k нулей в конец массива
def MUL_Nk_N(A, k):
    B = A[:]
    for i in range(k):
        B.append(0)

    return B


#Z-1
#Модуль целого числа: первый элемент заменяем на 0
def ABS_Z_N(A):
    B = A[:]
    B[0] = 0
    return B


#Z-5
#Перевод из целого в натуральное: удаляем первый элемент
def TRANS_Z_N(A):
    B = A[:]
    if B[0] == 0:
        B.pop(0)
    else:
        print("ERROR IN MODULE :TRANS_Z_N")
    return B

#Q-1
#Q-7

