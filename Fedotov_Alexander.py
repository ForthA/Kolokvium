from resultant_m1 import *
from resultant_m2 import *

#N-3
#Добавление 1 к натуральному числу:
#Если младший разряд = 9, то заменяем на 0
#Есди все цифры = 9, то создаем лист размером len(A) + 1 с 1 в начале
#Если не 9, то +1 в разряд
def ADD_1N_N(A):
    k = len(A) - 1
    while A[k] == 9:
        if k == 0:
            L = [0] * (len(A) + 1)
            L[0] = 1
            return L
        else:
            A[k] = 0
            k -= 1
    A[k] += 1
    return A

#N-4
#Сложение натуральных чисел:
#Добавляем в начало разряд, дополняя меньшее чсило разрядами до большего
#Если сумма цирф в разряде > 10 то переносим 1 в старший
#Если len(ответ) == len(большего числа), то удаляем 0
def ADD_NN_N(A, B):
    if COM_NN_D(A, B) == 2:
        C = B
        B = A
        A = C
    k = len(B) - len(A)
    A.reverse()
    for i in range(0, k + 1, 1):
        A.append(0)
    A.reverse()
    B.reverse()
    B.append(0)
    B.reverse()
    print(A)
    print(B)
    for i in range(len(B) - 1, 0, -1):
        if B[i] + A[i] >= 10:
            B[i] = (B[i] + A[i]) % 10
            B[i - 1] += 1
        else:
            B[i] = B[i] + A[i]
    if B[0] == 0:
        B.remove(0)
    return B

#N-6
#Умножение натурального числа на цифру:
#Добавляем доп. разряд в начало
#k - перенос на другой разряд
#Если после умножения и + k число в разряде больше 10, то A[i] = A[i] % 10; k += 1
def MUL_ND_N(A, n):
    A.reverse()
    A.append(0)
    A.reverse()
    k = 0
    for i in range(len(A)-1, 0, -1):
        tmp = A[i]
        A[i] = A[i] * n % 10
        A[i] += k
        k = int(tmp * n / 10)
        if A[i] >= 10:
            A[i] = A[i] % 10
            k += 1
    A[0] = k
    if A[0] == 0:
        A.remove(0)
    return A





A=list(map(int,input().split()))
#B=list(map(int,input().split()))
n=int(input())

print(MUL_ND_N(A, n))
