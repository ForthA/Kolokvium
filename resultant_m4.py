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
