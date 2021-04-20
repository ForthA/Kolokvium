from resultant_m2 import *


# Q-2
# Проверка на целое, если рациональное число является целым, то <да>, иначе <нет>
def INT_Q_B(A, B):
    A = A[1:]
    nod = GCF_NN_N(A, B)
    d = DIV_NN_N(B, nod)
    x = [1]
    y = [0]
    if COM_NN_D(A, y) == 0:
        return True
    if COM_NN_D(d, x) == 0:
        return True
    else:
        return False
    
    
#Q-3
#Преобразование целого в дробное
#Заносим целое число в двумерный массив
def TRANS_Z_Q(A):
    s=[A,[1]]
    return s



# Еще не готово
# Q - 5
# Сложение дробей
def ADD_QQ_Q(A, B, C, D):
    tempB = B.copy()
    tempD = D.copy()
    sum3 = MUL_NN_N(tempB, tempD)
    sum1 = MUL_ZZ_Z(A, TRANS_N_Z(D))
    sum2 = MUL_ZZ_Z(TRANS_N_Z(B), C)
    return ADD_ZZ_Z(sum1, sum2), sum3


# Q-8
# Деление дробей (делитель отличен от нуля)
def DIV_QQ_Q(A, B, C, D):
    result = 0
    C1 = []
    numer = []
    denom = []
    C1 = D.copy()
    D = C.copy()
    C = C1.copy()
    numer = MUL_ZZ_Z(A, C)
    denom = MUL_ZZ_Z(B, D)
    return numer, denom
