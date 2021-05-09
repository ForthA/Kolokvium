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
                    arr[i] = C(Q[0], Q[1])
                else:
                    array1.clear()
                    array2.clear()
                    array1.append(arr[i].A)
                    array1.append(arr[i].B)
                    array2.append(arr1[i - raz].A)
                    array2.append(arr1[i - raz].B)
                    Q = SUB_QQ_Q(array1, array2)
                    arr[i] = C(Q[0], Q[1])

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
def MUL_Pxk_P(arr0, k):
    arr = arr0[:]
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


# P-8
def MUL_PP_P(arr1, arr2):
    m = DEG_P_N(arr1)
    n = DEG_P_N(arr2)
    deg = m + n + 1
    res = [C] * deg
    for i in range(0, deg):
        res[i] = C([0, 0], [1])

    for i in range(0, n + 1):
        for j in range(0, m + 1):
            resDeg = i + j
            frac1 = [arr1[j].A, arr1[j].B]
            frac2 = [arr2[i].A, arr2[i].B]
            mul = MUL_QQ_Q(frac2, frac1)
            numerR = res[resDeg].A
            demonR = res[resDeg].B
            numerM = mul[0]
            demonM = mul[1]
            res[resDeg].A, res[resDeg].B = ADD_QQ_Q(numerR, demonR, numerM, demonM)
    return res


# P-9
# Частное от деления многочлена на многочлен при делении с остатком:
# Коэф делимого делим на старший коэф делителя -> получаем нужный коэф частного
# Вычитаем из делимого нужный многочлен
# Повторяем нужное кол-во раз
def DIV_PP_P(arr01, arr02):
    # Коэфы многочленов
    arr1 = arr01[:]
    arr2 = arr02[:]

    # Степень многочленов
    st1 = DEG_P_N(arr1)
    st2 = DEG_P_N(arr2)

    if st1 < st2:
        return [[[0, 0], [1]]]  # Нулевой многочлен
    else:
        # Степень и кол-во коэфов частного
        ansSt = st1 - st2
        ansLen = ansSt + 1

        # Инициализация частного(все коэфы 0)
        ans = [C] * (ansLen)
        for i in range(ansLen):
            ans[i].A = [0, 0]
            ans[i].B = [1]

        Q1 = arr2[0].A[:]
        Q2 = arr2[0].B[:]  # Старший коэф делителя
        # Расчет частного
        for i in range(ansLen):
            tmp = DIV_QQ_Q(arr1[0].A, arr1[0].B, Q1, Q2)
            ans[i] = C(tmp[0], tmp[1])  # Коэф частного

            tmp = MUL_Pxk_P(arr2, ansSt - i)
            arrSUB = MUL_PQ_P(tmp, ans[i])  # Вычитаемый многочлен

            for j in range(len(arrSUB)):  # Костыль. Для правильной работы SUB_PP_P
                if arrSUB[j].A[1] == 0:
                    arrSUB[j].A[0] = 1

            arr1 = SUB_PP_P(arr1, arrSUB)
            arr1.pop(0)

    return ans


# P-10
# Остаток от деления многочлена на многочлен при делении с остатком
def MOD_PP_P(arr, arr1):
    chas = DIV_PP_P(arr, arr1)  # Находим частное от деления двух многочленов
    k = MUL_PP_P(chas, arr1)  # Произведение частногоь на второй многочлен
    res = SUB_PP_P(arr, k)  # Вычитаем из первого исходного многочлена произведение частного на второй
    return res


# P-11 НОД многочленов Если степень 1-го многочлена меньше второго (m<n), то создаем два массива, где присваиваем
# arr2 присваиваем arr1-это второй многочлен, arr3 присваиваем arr-это первый многочлен Находим остаток от деления
# двух многочленов Пока степень полученного многочлена больше нуля, то к arr2 присваиваем arr3, а к arr3 остаток,
# исли остаток равен нулю, то выводим arr3
def GCF_PP_P(arr, arr1):
    m = DEG_P_N(arr)
    n = DEG_P_N(arr1)
    if n > m:
        arr2 = arr1
        arr3 = arr
        r = MOD_PP_P(arr2, arr3)
        while DEG_P_N(r) > 0:
            arr2 = arr3
            arr3 = r
            r = MOD_PP_P(arr2, arr3)
        return arr3
    else:
        arr2 = arr
        arr3 = arr1
        r = MOD_PP_P(arr3, arr2)
        while DEG_P_N(r) > 0:
            arr3 = arr2
            arr2 = r
            r = MOD_PP_P(arr3, arr2)
        return arr2


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
