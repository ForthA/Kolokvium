from resultant_m2 import *

#Q-1
#Сокращение дроби:
# числитель -> натуральное число
# Делим числитель и знаменатель на их НОД
# Возвращаем дробь в соответсствии со знаком
def RED_Q_Q(Q0):
    A = Q0[0][:]
    B = Q0[1][:]

    A1 = ABS_Z_N(A)
    A1 = TRANS_Z_N(A1)

    nod = GCF_NN_N(A1, B)
    A1 = DIV_NN_N(A1, nod)
    B = DIV_NN_N(B, nod)

    A1.insert(0, A[0])
    Q = [A1, B]
    return Q


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

#Q-4
#Считаем количество элементов и нулевых элементов в знаменателе,
#если их количества совпадают и последний элемент знаменателя равен нулю,
#то возвращаем только числитель
def TRANS_Q_Z(A):
    count = 0
    num = 0
    flag = 0
    for i in range (len(A[1])):
        if (A[1][i] == 0):
            count = count + 1
        num = num + 1
        
    if ((count == num - 1) and (A[1][count] == 1)):
            flag = 1
            
    if (flag == 1):
        return A[0]
    
   
# Q - 5
# Сложение дробей
def ADD_QQ_Q(A, B, C, D):
    tempB = B.copy()
    tempD = D.copy()
    sum3 = MUL_NN_N(tempB, tempD)
    sum1 = MUL_ZZ_Z(A, TRANS_N_Z(D))
    sum2 = MUL_ZZ_Z(TRANS_N_Z(B), C)
    temp = ADD_ZZ_Z(sum1, sum2)
    temp1, temp2 = RED_Q_Q([temp, sum3])
    return temp1, temp2

#Q-6
#Вычитание дробей
#Находим НОК знаменателей, потом домножаем числители и вычитаем из первого второй

def SUB_QQ_Q(Q01, Q02):
    A1 = Q01[0][:]
    A2 = Q01[1][:]
    B1 = Q02[0][:]
    B2 = Q02[1][:]
    NOK = LCM_NN_N(A2, B2)
    A2.reverse()
    A2.append(0)
    A2.reverse()
    B2.reverse()
    NOK.reverse()
    NOK.append(0)
    NOK.reverse()
    numeratorA = MUL_ZZ_Z(DIV_ZZ_Z(NOK, A2), A1)
    numeratorB = MUL_ZZ_Z(DIV_ZZ_Z(NOK, B2), B1)
    del NOK[0]
    Q = [SUB_ZZ_Z(numeratorA, numeratorB), NOK]
    return Q


#Q-7
#Умножение дробей:
# знаменатель -> целое
# умножение знаменателей и числителей
# знаменатель -> натуральное
# вывод дроби
def MUL_QQ_Q(Q01, Q02):
    A1 = Q01[0][:]
    B1 = Q01[1][:]
    A2 = Q02[0][:]
    B2 = Q02[1][:]

    B1 = TRANS_N_Z(B1)
    B2 = TRANS_N_Z(B2)

    A = MUL_ZZ_Z(A1, A2)
    B = MUL_ZZ_Z(B1, B2)

    B = TRANS_Z_N(B)
    Q = [A, B]
    return Q



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
