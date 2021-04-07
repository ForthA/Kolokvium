# Оставляем описание каждого алгоритма

# Сравнение чисел, если первое больше второго вывод - 2, если второе больше - 1,равны - 0 N-1
def COM_NN_D(A, B):
    i = 0
    if len(A) > len(B):
        return 2
    elif len(A) < len(B):
        return 1
    else:
        while 1:
            if A[i] > B[i]:
                return 2
            elif A[i] < B[i]:
                return 1
            elif (A[i] == B[i]) & (i == (len(A) - 1)):
                return 0
            i += 1

# Проверка на ноль, если ноль - нет, если не ноль - да N-2
def NZER_N_B(A):
    if A[0] != 0:
        print("Да")
    else:
        print("Нет")

#Вычитание из большего меньшего N-5        
def SUB_NN_N(A, B):
    i = 0
    if COM_NN_D(A, B) == 1:
        temp = A
        A = B
        B = temp
    k = len(A) - len(B)
    B.reverse()
    for i in range(0, k, 1):
        B.append(0)
    B.reverse()
    print(A)
    print(B)
    for i in range(len(B) - 1,-1,-1):
        if A[i] >= B[i]:
            A[i] = A[i] - B[i]
        else:
           k = i - 1
           A[i] = (A[i] + 10) - B[i]
           while A[k] == 0:
            A[k] = 9
            k -= 1
           A[k] -= 1
    i = 0
    while (A[i] == 0) & (len(A) != 1):
        A.remove(0)
    return A        
