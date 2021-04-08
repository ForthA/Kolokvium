# Сравнение чисел, если первое больше второго вывод - 2, если второе больше - 1,равны - 0
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


# Проверка на ноль, если ноль - нет, если не ноль - да
def NZER_N_B(A):
    if A[0] != 0:
        print("Да")
    else:
        print("Нет")


# N-3
# Добавление 1 к натуральному числу:
# Если младший разряд = 9, то заменяем на 0
# Есди все цифры = 9, то создаем лист размером len(A) + 1 с 1 в начале
# Если не 9, то +1 в разряд
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


# N-4
# Сложение натуральных чисел:
# Добавляем в начало разряд, дополняя меньшее чсило разрядами до большего
# Если сумма цирф в разряде > 10 то переносим 1 в старший
# Если len(ответ) == len(большего числа), то удаляем 0
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


# N - 5 Вычитание натуральных чисел
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
    for i in range(len(B) - 1, -1, -1):
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


# N-6
# Умножение натурального числа на цифру:
# Добавляем доп. разряд в начало
# k - перенос на другой разряд
# Если после умножения и + k число в разряде больше 10, то A[i] = A[i] % 10; k += 1
def MUL_ND_N(A, n):
    A.reverse()
    A.append(0)
    A.reverse()
    k = 0
    for i in range(len(A) - 1, 0, -1):
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


# N-7
# Умножаем на 10^k: добавляем k нулей в конец массива
def MUL_Nk_N(A, k):
    B = A[:]
    for i in range(k):
        B.append(0)

    return B


# N-8
# Умножение натуральных чисел
def MUL_NN_N(A, B):
    p = []
    B.reverse()
    B.append(0)
    for i in range(len(B)):
        # t - текущий разряд на который умножаем число
        t = B[i]
        # Умножаем исходное число на t
        c = MUL_ND_N(list(map(int, A)), t)
        # Умноженаем результат на 10^k, чтобы "сдвинуть" его
        c = MUL_Nk_N(list(map(int, c)), i)
        # добавляем к результату
        p = ADD_NN_N(list(map(int, p)), list(map(int, c)))
    del p[0]
    return p


# N-9 Вычитание из натурального другого натурального, умноженного на цифру для случая с неотрицательным результатом.
# Сначала находим произведение B и n. Если результат неотрицательный, то находим разность двух натуральных чисел,
# иначем возвращаем -1
def SUB_NDN_N(A, B, n):
    B = MUL_ND_N(B, n)

    if COM_NN_D(A, B) == 2 or COM_NN_D(A, B) == 0:

        A = SUB_NN_N(A, B)

        return A
    else:
        return "error in SUB_NDN_N"


# N-10
# Вычисление первой цифры деления, умноженное на 10^k, k - позиция этой цифры.
# Преобразование массивов в числа, перемещение большего числа на первое место,
# нахождение самого числа, ее позиции и результата.
def DIV_NN_Dk(A, B, k):
    i = 1
    count = 1
    flag = False
    if COM_NN_D(A, B) == 1:
        temp = A
        A = B
        B = temp
    MUL_Nk_N(A, k)
    while COM_NN_D(A[0:i], B) == 1:
        i += 1
    tm = B.copy()
    while COM_NN_D(A[0:i], MUL_ND_N(tm, count)) == 2:
        count += 1
        tm = B.copy()
        flag = True
    if flag:
        count -= 1
    return count
