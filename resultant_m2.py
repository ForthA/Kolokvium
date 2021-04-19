from resultant_m1 import *


# Z-1
# Модуль целого числа: первый элемент заменяем на 0
def ABS_Z_N(A):
    B = A[:]
    B[0] = 0
    return B


# Z-2
# Определение положительности числа (2 - положительное, 0 - равное нулю, 1 - отрицательное)
def POZ_Z_D(A):
    if A[0] == 1:
        return 1
    elif isZero(A):
        return 0
    else:
        return 2


# Проверка на ноль
def isZero(A):
    for i in range(len(A)):
        if A[i]:
            return False
    return True


# Z-3 Умножение целого на -1. Алгоритм проверяет, если число положительное, то есть первый индекс массива равно нулю,
# то заменяем на противоположный знак, иначе ничего не меняем.
def MUL_ZM_Z(A):
    if A[0] == 0:
        A[0] = 1
    else:
        A[0] = 0
    return A


# Z-4
# Преобразование массива цифр натурального числа в целое число
def TRANS_N_Z(A):
    A = [0] + A
    return A


# Z-5
# Перевод из целого в натуральное: удаляем первый элемент
def TRANS_Z_N(A):
    B = A[:]
    if B[0] == 0:
        B.pop(0)
    else:
        print("ERROR IN MODULE :TRANS_Z_N")
    return B


# Z-6
# Сложение целых чисел
def ADD_ZZ_Z(A, B):
    result = 0
    AZ = POZ_Z_D(A)
    BZ = POZ_Z_D(B)
    if (AZ == BZ) & (AZ == 1):
        a = ABS_Z_N(A)
        b = ABS_Z_N(B)
        result = ADD_NN_N(a, b)
        result = MUL_ZM_Z(result)
    elif (AZ == BZ) & (AZ == 2):
        a = ABS_Z_N(A)
        b = ABS_Z_N(B)
        result = ADD_NN_N(a, b)
    elif (AZ == BZ) & (AZ == 0):
        result = 0
    else:
        a = ABS_Z_N(A)
        b = ABS_Z_N(B)
        raz = COM_NN_D(a, b)
        if raz == 2:
            result = SUB_NN_N(a, b)
            if AZ == 1:
                result.insert(0, 0)
                result = MUL_ZM_Z(result)
        else:
            result = SUB_NN_N(b, a)
            result.insert(0, 0)
            if BZ == 1:
                result = MUL_ZM_Z(result)
    return result



# Z-7
# Вычитание целых чисел
# Рассматриваем 4 случая. Когда оба числа положительные. Если первое число больше второго, то преобразуем эти числа в натуральные и находим разность. Полученное число будет иметь знак +, иначе число будет иметь знак -
# Когда оба числа отрицательные. Если абсолютное значение первого числа будет больше абс. знач. 2-го числа, то полученное число будет иметь знак -, иначе +
# Первое число положительное, второе-отрицательное. В этом случае складываем числа. Полученное значение будет иметь знак +
# Первое число отрицательное, второе-положительное. В этом случае так же складываем числа, но полученное значение будет иметь знак -.
def SUB_ZZ_Z(A, B):
    res = 0
    A1 = POZ_Z_D(A)
    B1 = POZ_Z_D(B)
    if ((A1 == B1) and (A1 == 2)):
        a = ABS_Z_N(A)
        b = ABS_Z_N(B)
        res = SUB_NN_N(a, b)
        if (COM_NN_D(a, b) == 1):
            res.insert(0, 0)
        else:
            res.insert(0, 0)
            res = MUL_ZM_Z(res)
    elif ((A1 == B1) and (A1 == 1)):
        a = ABS_Z_N(A)
        b = ABS_Z_N(B)
        res = SUB_NN_N(a, b)
        if (COM_NN_D(a, b) == 2):
            res.insert(0, 0)
        else:
            res.insert(0, 0)
            res = MUL_ZM_Z(res)
    elif ((A1 == B1) and (A1 == 0)):
        res = 0
    else:
        a = ABS_Z_N(A)
        b = ABS_Z_N(B)
        if ((A1 == 2) and ((B1 == 1) or (B1 == 0))):
            res = ADD_NN_N(a, b)

        elif ((A1 == 1) and ((B1 == 2) or (B1 == 0))):
            res = ADD_NN_N(a, b)
            res = MUL_ZM_Z(res)
        elif ((A1 == 0) and (B1 == 1)):
            res = ADD_NN_N(a, b)
            res = MUL_ZM_Z(res)
        elif ((A1 == 0) and (B1 == 2)):
            res = ADD_NN_N(a, b)
    return res


# Z-8
# Умножение целых чисел
def MUL_ZZ_Z(A, B):
    result = 0
    AZ = POZ_Z_D(A)
    BZ = POZ_Z_D(B)
    if (AZ == BZ):
        a = ABS_Z_N(A)
        b = ABS_Z_N(B)
        result = MUL_NN_N(a,b)
        if result[0] == 0 and result[1] == 0:
            del result[0]
    elif ((AZ == 0) | (BZ == 0)):
        result = 0
    else:
        a = ABS_Z_N(A)
        b = ABS_Z_N(B)
        result = MUL_NN_N(a,b)
        if result[0] == 0 and result[1] == 0:
            del result[0]
        result = MUL_ZM_Z(result)
    return result




# z-9 Частное от деления целых чисел

def DIV_ZZ_Z(A, B):
    num1 = A
    num2 = B
    num3 = DIV_NN_N(A[1:len(num1)],B[1:len(num2)])
    num3.reverse()
    num3.append(0)
    num3.reverse()
    if ((POZ_Z_D(num1) == 1) and (POZ_Z_D(num2) == 2)) or ((POZ_Z_D(num1) == 2) and (POZ_Z_D(num2) == 1)):
        num3[0] = 1
    return num3






#Z-10
#Остаток от деления целого на целое(делитель отличен от нуля)
#1)При положительных числах и при делителе(B) < 0: находим частное от деления и вычитаем от A произвение частного на B
#2)При делимом(А) < 0 и длителе(В) > 0: вычитаем из А В, чтобы при нахождении частного получить на 1 больше =>
# остаток > 0
#3)При делимом(А) < 0 и длителе(В) < 0: меняем знак у B и вычитаем из А В (-А - (В)) => получем частное на 1 больше =>
# остаток > 0
def MOD_ZZ_Z(A, B):
    if ((A[0] == 0) and (B[0] == 1)) or ((A[0] == 0) and (B[0] == 0)):
        return SUB_ZZ_Z(A, MUL_ZZ_Z(B, DIV_ZZ_Z(A, B)))
    if ((A[0] == 1) and (B[0] == 0)) or ((A[0] == 1) and (B[0] == 1)):
        Rev = B
        if (A[0] == 1) and (B[0] == 1):
            Rev = MUL_ZM_Z(B)
        inDiv = DIV_ZZ_Z(SUB_ZZ_Z(A, Rev), B)
        return SUB_ZZ_Z(A, MUL_ZZ_Z(inDiv, B))
