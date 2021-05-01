from C import C
from resultant_m3 import *


# P-1 Сложение многочленов если коэффициент = 0, вводим его как (1 0/1) если старшая степень 1-го многочлена больше
# второго, то находим разницу стпеней и p присваиваем стпень 1-го многочлена проходим по циклу, если p превосходит n,
# то присваиваем значения числителя и знаменателя в результитрующий массив и уменьшаем p если же p не превосходит n,
# то проверяем условие, если m превосходит n, то складываем коэффициенты многочленов если же старшая степень 1-го
# многочлена меньше 2-го, то делаем все то же самое, но только меняем местами многочлены
def ADD_PP_P(arr, arr1):
    m = DEG_P_N(arr)
    n = DEG_P_N(arr1)
    if m >= n:
        p = m
        raz = m - n

        for i in range(0, m + 1):

            if p > n:

                arr[i] = arr[i].A, arr[i].B
                p = p - 1

            else:

                if m > n:

                    arr[i] = ADD_QQ_Q(arr[i].A, arr[i].B, arr1[i - raz].A, arr1[i - raz].B)
                else:
                    arr[i] = ADD_QQ_Q(arr[i].A, arr[i].B, arr1[i - raz].A, arr1[i - raz].B)

        return arr
    else:
        q = n
        raz = n - m
        for i in range(0, n + 1):

            if q > m:
                arr1[i] = arr1[i].A, arr1[i].B
                q = q - 1
            else:
                if n > m:
                    arr1[i] = ADD_QQ_Q(arr1[i].A, arr1[i].B, arr[i - raz].A, arr[i - raz].B)
                else:
                    arr1[i] = ADD_QQ_Q(arr1[i].A, arr1[i].B, arr[i - raz].A, arr[i - raz].B)

        return arr1


# P - 2
# Вычитание многочленов
def SUB_PP_P(arr, arr1):
    m = DEG_P_N(arr)
    n = DEG_P_N(arr1)
    if m >= n:

        array1 = []
        array2 = []

        p = m
        raz = m - n

        for i in range(0, m + 1):
            if p > n:
                arr[i] = arr[i].A, arr[i].B
                p = p - 1
            else:
                if m > n:
                    array1.clear()
                    array2.clear()
                    array1.append(arr[i].A)
                    array1.append(arr[i].B)
                    array2.append(arr1[i - raz].A)
                    array2.append(arr1[i - raz].B)
                    Q = SUB_QQ_Q(array1, array2)
                    arr1[i] = C(Q[0], Q[1])
                else:
                    array1.clear()
                    array2.clear()
                    array1.append(arr[i].A)
                    array1.append(arr[i].B)
                    array2.append(arr1[i - raz].A)
                    array2.append(arr1[i - raz].B)
                    Q = SUB_QQ_Q(array1, array2)
                    arr1[i] = C(Q[0], Q[1])

        return arr

    else:
        array1 = []
        array2 = []

        q = n
        raz = n - m

        for i in range(0, n + 1):
            if q > m:
                arr1[i] = arr1[i].A, arr1[i].B
                q = q - 1
            else:
                if n > m:
                    array1.clear()
                    array2.clear()
                    array1.append(arr[i].A)
                    array1.append(arr[i].B)
                    array2.append(arr1[i - raz].A)
                    array2.append(arr1[i - raz].B)
                    Q = SUB_QQ_Q(array1, array2)
                    arr1[i] = C(Q[0], Q[1])
                else:
                    array1.clear()
                    array2.clear()
                    array1.append(arr[i].A)
                    array1.append(arr[i].B)
                    array2.append(arr1[i - raz].A)
                    array2.append(arr1[i - raz].B)
                    Q = SUB_QQ_Q(array1, array2)
                    arr1[i] = C(Q[0], Q[1])

        return arr1

    # P - 3


# Умножение коэфа с многочленом
def MUL_PQ_P(arr, D):
    for i in range(0, len(arr)):
        arr[i].A, arr[i].B = MUL_QQ_Q([arr[i].A, arr[i].B], [D.A, D.B])
    return arr


# P-4
# Умножение многочлена на x^k
# Добавляем элементы [0, 0],[0], чтобы понимать сколько до конца многочлена
def MUL_Pxk_P(arr, k):
    for i in range(0, k):
        arr.append(C([0, 0], [1]))
    return arr


# P-5
# Старший коэффициент многочлена:
# Старший коэф это первый коэф(перед старршей степенью)
def LED_P_Q(arr):
    Q = list([arr[0].A, arr[0].B])
    return Q


# P-6
# Степень многочлена
def DEG_P_N(arr):
    return len(arr) - 1


# P-7 Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей Чтобы найти НОД чисел, сначала нужно
# найти НОД двух первых чисел, потом находим НОД вот таким образом, НОД(НОД двух предыдущих чисел, следующее число)
# Чтобы найти НОК чисел, сначала нужно найти НОК двух первых чисел, потом находим НОК вот таким образом, НОК(НОК двух
# предыдущих чисел, следующее число)

def FAC_P_Q(arr):
    m = DEG_P_N(arr)
    nok = []
    nod = []
    i = 0
    for i in range(0, m + 1):
        if POZ_Z_D(arr[i].A) == 1:
            arr[i].A = ABS_Z_N(arr[i].A)
        else:
            arr[i].A = TRANS_Z_N(arr[i].A)
    if m == 0:
        nod = arr[i].A
        nok = arr[i].B
    else:
        for i in range(0, m + 1):
            if i == 0:
                nod = GCF_NN_N(arr[i].A, arr[i + 1].A)
                nok = LCM_NN_N(arr[i].B, arr[i + 1].B)
            else:
                if i < m:
                    nod = GCF_NN_N(nod, arr[i + 1].A)
                    nok = LCM_NN_N(nok, arr[i + 1].B)
    return TRANS_N_Z(nod), nok


# P-12
# Производная многочлена
# m - степень переводим в список, т.к степнь может быть числом(для олее простого умножения)
# забираем знак у числителя и умножаем его на степень
# del result[len(result)-1] нужен для удаления нуля в конце после функции MUL_NN_N
# Возвращаем знак числителю и минусуем 1 от степени
def DER_P_P(arr):
    m = DEG_P_N(arr)
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
        del result[len(result) - 1]
        section.reverse()
        section.append(sign)
        section.reverse()
        arr[i].A = section
        result = SUB_NN_N(result, [1])
    return arr


'''#P-10
#Остаток от деления многочлена на многочлен при делении с остатком
def MOD_PP_P(arr,m, arr1,n):
    chas = DIV_PP_P(arr,m, arr1,n) #Находим частное от деления двух многочленов 
    k = MUL_PP_P(chas, arr1) #Произведение частногоь на второй многочлен
    res = SUB_PP_P(arr, m, k, n) #Вычитаем из первого исходного многочлена произведение частного на второй
    return res

#P-11
#НОД многочленов
#Если степень 1-го многочлена меньше второго (m<n), то создаем два массива, где присваиваем arr2 присваиваем arr1-это второй многочлен, arr3 присваиваем arr-это первый многочлен
#Находим остаток от деления двух многочленов
#Пока степень полученного многочлена больше нуля, то к arr2 присваиваем arr3, а к arr3 остаток, исли остаток равен нулю, то выводим arr3 
def GCF_PP_P(arr,m,arr1,n):
    if(m<n):
        arr2=[C]*(n+1)
        arr2=arr1
        arr3=[C]*(m+1)
        arr3=arr
        r=MOD_PP_P(arr2,n,arr3,m)
        while(DEG_P_N(r,(n-m))>0):
            arr2=arr3
            arr3=r
        return arr3
            r=MOD_PP_P(arr2,n,arr3,m)
    else:
        arr2=[C]*(m+1)
        arr2=arr
        arr3=[C]*(n+1)
        arr3=arr1
        r=MOD_PP_P(arr3,m,arr2,n)
        while(DEG_P_N(r,(n-m))>0):
            arr3=arr2
            arr2=r
            r=MOD_PP_P(arr3,m,arr2,n)
        return arr2

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
    return arr '''
