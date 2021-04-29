from C import C
from resultant_m3 import *

# P-1
# Сложение многочленов
# если коэффициент = 0, вводим его как (1 0/1)
def ADD_PP_P(arr,m, arr1,n):
    if (m >= n):
        p = m
        raz = m - n

        for i in range(0, m + 1):

            if (p > n):

                arr[i] = arr[i].A, arr[i].B
                p = p - 1

            else:

                if (m > n):

                    arr[i] = ADD_QQ_Q(arr[i].A, arr[i].B, arr1[i - raz].A, arr1[i - raz].B)
                else:
                    arr[i] = ADD_QQ_Q(arr[i].A, arr[i].B, arr1[i - raz].A, arr1[i - raz].B)

        return arr
    else:
        q = n
        raz = n - m
        for i in range(0, n + 1):

            if (q > m):
                arr1[i] = arr1[i].A, arr1[i].B
                q = q - 1
            else:
                if (n > m):
                    arr1[i] = ADD_QQ_Q(arr1[i].A, arr1[i].B, arr[i - raz].A, arr[i - raz].B)
                else:
                    arr1[i] = ADD_QQ_Q(arr1[i].A, arr1[i].B, arr[i - raz].A, arr[i - raz].B)

        return arr1


    
#P - 2
#Вычитание многочленов
def SUB_PP_P(arr, m, arr1, n):
    if(m >= n):
        
        array1 = []
        array2 = []
            
        p = m
        raz = m - n
        
        for i in range(0, m+1):
            if(p > n):
                arr[i] = arr[i].A,arr[i].B
                p = p - 1
            else:
                if(m > n):
                    array1.clear()
                    array2.clear()
                    array1.append(arr[i].A)
                    array1.append(arr[i].B)
                    array2.append(arr1[i-raz].A)
                    array2.append(arr1[i-raz].B)
                    arr[i] = SUB_QQ_Q(array1, array2)
                else:
                    array1.clear()
                    array2.clear()
                    array1.append(arr[i].A)
                    array1.append(arr[i].B)
                    array2.append(arr1[i-raz].A)
                    array2.append(arr1[i-raz].B)
                    arr[i] = SUB_QQ_Q(array1, array2)
                     
        return arr
         
    else:
        array1 = []
        array2 = []
            
        q = n
        raz = n - m
        
        for i in range(0, n+1):
            if(q > m):
                arr1[i] = arr1[i].A,arr1[i].B
                q = q - 1
            else:
                if(n > m):
                    array1.clear()
                    array2.clear()
                    array1.append(arr[i].A)
                    array1.append(arr[i].B)
                    array2.append(arr1[i-raz].A)
                    array2.append(arr1[i-raz].B)
                    arr1[i] = SUB_QQ_Q(array1, array2)
                else:
                    array1.clear()
                    array2.clear()
                    array1.append(arr[i].A)
                    array1.append(arr[i].B)
                    array2.append(arr1[i-raz].A)
                    array2.append(arr1[i-raz].B)
                    arr1[i] = SUB_QQ_Q(array1, array2)
                    
        return arr1    

# P - 3
# Умножение коэфа с многочленом
def MUL_PQ_P(arr, D):
    for i in range(0, len(arr)):
        arr[i].A, arr[i].B = MUL_QQ_Q([arr[i].A, arr[i].B], [D.A, D.B])
    return arr


#P-4
#Умножение многочлена на x^k
#Добавляем элементы [0, 0],[0], чтобы понимать сколько до конца многочлена
def MUL_Pxk_P(arr, k):
    for i in range(0, k):
        arr.append(C([0, 0], [0]))
    return arr

# P-6
# Степень многочлена
def DEG_P_N(arr,m):
    return m

#P-7
#Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей
#Чтобы найти НОД чисел, сначала нужно найти НОД двух первых чисел, потом находим НОД вот таким образом, НОД(НОД двух предыдущих чисел, следующее число)
#Чтобы найти НОК чисел, сначала нужно найти НОК двух первых чисел, потом находим НОК вот таким образом, НОК(НОК двух предыдущих чисел, следующее число)

def FAC_P_Q(arr,m):
    nok=[]
    nod=[]
    for i in range(0,m+1):
        if(POZ_Z_D(arr[i].A)==1):
            arr[i].A=ABS_Z_N(arr[i].A)
        else:
            arr[i].A=TRANS_Z_N(arr[i].A)
    if(m==0):
        nod=arr[i].A
        nok=arr[i].B
    else:
        for i in range(0,m+1):
            if(i==0):
                nod=GCF_NN_N(arr[i].A,arr[i+1].A)
                nok=LCM_NN_N(arr[i].B,arr[i+1].B)
            else:
                if(i<m):
                    nod=GCF_NN_N(nod,arr[i+1].A)
                    nok=LCM_NN_N(nok,arr[i+1].B)
    return TRANS_N_Z(nod),nok



# P-12
# Производная многочлена
# m - степень переводим в список, т.к степнь может быть числом(для олее простого умножения)
# забираем знак у числителя и умножаем его на степень
# del result[len(result)-1] нужен для удаления нуля в конце после функции MUL_NN_N
# Возвращаем знак числителю и минусуем 1 от степени
def DER_P_P(arr, m):
    tmp = m
    result = []
    while m > 0:
        result.append(m % 10)
        m //= 10
    result.reverse()
    for i in range(0, tmp):
        sign = arr[i].A[0]
        del arr[i].A[0]
        section = MUL_NN_N(arr[i].A, result)
        del result[len(result)-1]
        section.reverse()
        section.append(sign)
        section.reverse()
        arr[i].A = section
        result = SUB_NN_N(result, [1])
    return arr
