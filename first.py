from Tarasov_Kostya import COM_NN_D

#Добавление единицы к натуральному N-3
def ADD_1N_N(A, n):
    k = n - 1
    while A[k] == 9:
        if k == 0:
            L = [0] * (n + 1)
            L[0] = 1
            return L
        else:
            A[k] = 0
            k -= 1
    A[k] += 1
    return A


#Сложение натуральных чисел N-4
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

