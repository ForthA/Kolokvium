from resultant_m4 import *
from C import C
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Radiobutton


# Тут типа main

def clicked():
    s1 = txt11.get()
    s2 = txt12.get()
    A = [0] * len(s1)
    B = [0] * len(s2)
    txt13 = Entry(tab1, width=20)
    txt13.grid(column=0, row=15)
    for i in range(0, len(s1)):
        A[i] = int(s1[i])
    for i in range(0, len(s2)):
        B[i] = int(s2[i])
    if selected.get() == 1:
        txt13.insert(0, COM_NN_D(A, B))
    elif selected.get() == 2:
        txt13.insert(0, NZER_N_B(A))
    elif selected.get() == 3:
        temp = ADD_1N_N(A)
        s = ''
        for i in range(0, len(temp)):
            s += str(temp[i])
        txt13.insert(0, s)
    elif selected.get() == 4:
        temp = ADD_NN_N(A, B)
        s = ''
        for i in range(0, len(temp)):
            s += str(temp[i])
        txt13.insert(0, s)
    elif selected.get() == 5:
        temp = SUB_NN_N(A, B)
        s = ''
        for i in range(0, len(temp)):
            s += str(temp[i])
        txt13.insert(0, s)
    elif selected.get() == 6:
        n = ''
        for i in range(0, len(B)):
            n += str(B[i])
        temp = MUL_ND_N(A, int(n))
        s = ''
        for i in range(0, len(temp)):
            s += str(temp[i])
        txt13.insert(0, s)
    elif selected.get() == 7:
        k = ''
        for i in range(0, len(B)):
            k += str(B[i])
        temp = MUL_Nk_N(A, int(k))
        s = ''
        for i in range(0, len(temp)):
            s += str(temp[i])
        txt13.insert(0, s)
    elif selected.get() == 8:
        temp = MUL_NN_N(A, B)
        s = ''
        for i in range(0, len(temp)):
            s += str(temp[i])
        txt13.insert(0, s)
    elif selected.get() == 9:
        temp = SUB_NDN_N(A, B, B[len(B) - 1])
        s = ''
        for i in range(0, len(temp)):
            s += str(temp[i])
        txt13.insert(0, s)
    elif selected.get() == 10:
        temp = DIV_NN_Dk(A, B, 0)

        txt13.insert(0, str(temp))
    elif selected.get() == 11:
        temp = DIV_NN_N(A, B)
        print(temp)
        s = ''
        for i in range(0, len(temp)):
            s += str(temp[i])
        txt13.insert(0, s)

    elif selected.get() == 12:
        temp = MOD_NN_N(A, B)
        s = ''
        for i in range(0, len(temp)):
            s += str(temp[i])
        txt13.insert(0, s)

    elif selected.get() == 13:
        temp = GCF_NN_N(A, B)
        s = ''
        for i in range(0, len(temp)):
            s += str(temp[i])
        txt13.insert(0, s)
    elif selected.get() == 14:
        temp = LCM_NN_N(A, B)
        s = ''
        for i in range(0, len(temp)):
            s += str(temp[i])
        txt13.insert(0, s)


def clicked2():
    s1 = txt21.get()
    s2 = txt22.get()
    A = [0] * len(s1)
    B = [0] * len(s2)
    txt23 = Entry(tab2, width=20)
    txt23.grid(column=0, row=15)
    j = 0
    if s1[0] == '-':
        A[0] = 1
        for i in range(1, len(s1)):
            A[i] = int(s1[i])
    else:
        for i in range(0, len(s1)):
            A[i] = int(s1[i])
        A.reverse()
        A.append(0)
        A.reverse()
    if s2[0] == '-':
        B[0] = 1
        for i in range(1, len(s2)):
            B[i] = int(s2[i])
    else:
        for i in range(0, len(s2)):
            B[i] = int(s2[i])
        B.reverse()
        B.append(0)
        B.reverse()

    if selected.get() == 1:
        temp = ABS_Z_N(A)
        s = ''
        if temp[0] == 1:
            s += '-'
            for i in range(1, len(temp)):
                s += str(temp[i])
        else:
            for i in range(1, len(temp)):
                s += str(temp[i])
        txt23.insert(0, s)
    elif selected.get() == 2:
        temp = POZ_Z_D(A)
        txt23.insert(0, str(temp))
    elif selected.get() == 3:
        temp = MUL_ZM_Z(A)
        s = ''
        if temp[0] == 1:
            s += '-'
            for i in range(1, len(temp)):
                s += str(temp[i])
        else:
            for i in range(1, len(temp)):
                s += str(temp[i])
        txt23.insert(0, s)
    elif selected.get() == 4:
        temp = A.copy()
        s = ''
        if temp[0] == 1:
            s += '-'
            for i in range(1, len(temp)):
                s += str(temp[i])
        else:
            for i in range(1, len(temp)):
                s += str(temp[i])
        txt23.insert(0, s)
    elif selected.get() == 5:
        temp = A.copy()
        s = ''
        if temp[0] == 1:
            for i in range(1, len(temp)):
                s += str(temp[i])
            txt23.insert(0, s[0:len(temp)])
        else:
            for i in range(0, len(temp)):
                s += str(temp[i])
            txt23.insert(0, s[1:len(temp)])
    elif selected.get() == 6:
        temp = ADD_ZZ_Z(A, B)
        s = ''
        if temp[0] == 1:
            s += '-'
            for i in range(1, len(temp)):
                s += str(temp[i])
        else:
            for i in range(1, len(temp)):
                s += str(temp[i])
        txt23.insert(0, s)
    elif selected.get() == 7:
        temp = SUB_ZZ_Z(A, B)
        s = ''
        if temp[0] == 1:
            s += '-'
            for i in range(1, len(temp)):
                s += str(temp[i])
        else:
            for i in range(1, len(temp)):
                s += str(temp[i])
        txt23.insert(0, s)
    elif selected.get() == 8:
        temp = MUL_ZZ_Z(A, B)
        s = ''
        if temp[0] == 1:
            s += '-'
            for i in range(1, len(temp)):
                s += str(temp[i])
        else:
            for i in range(1, len(temp)):
                s += str(temp[i])
        txt23.insert(0, s)
    elif selected.get() == 9:
        temp = DIV_ZZ_Z(A, B)
        s = ''
        if temp[0] == 1:
            s += '-'
            for i in range(1, len(temp)):
                s += str(temp[i])
        else:
            for i in range(1, len(temp)):
                s += str(temp[i])
        txt23.insert(0, s)
    elif selected.get() == 10:
        temp = MOD_ZZ_Z(A, B)
        s = ''
        if temp[0] == 1:
            s += '-'
            for i in range(1, len(temp)):
                s += str(temp[i])
        else:
            for i in range(1, len(temp)):
                s += str(temp[i])
        txt23.insert(0, s)


def clicked3():
    s1 = txt31.get()
    s2 = txt32.get()
    temp1 = s1[0:s1.find("/")]
    temp2 = s1[s1.find("/") + 1:len(s1)]
    temp3 = s2[0:s2.find("/")]
    temp4 = s2[s2.find("/") + 1:len(s2)]
    A = [0] * len(temp1)
    B = [0] * len(temp2)
    C = [0] * len(temp3)
    D = [0] * len(temp4)
    txt33 = Entry(tab3, width=20)
    txt33.grid(column=0, row=15)
    for i in range(0, len(temp2)):
        B[i] = int(temp2[i])
    for i in range(0, len(temp4)):
        D[i] = int(temp4[i])
    if temp1[0] == '-':
        A[0] = 1
        for i in range(1, len(temp1)):
            A[i] = int(temp1[i])
    else:
        for i in range(0, len(temp1)):
            A[i] = int(temp1[i])
        A.reverse()
        A.append(0)
        A.reverse()
    if temp3[0] == '-':
        C[0] = 1
        for i in range(1, len(temp3)):
            C[i] = int(temp3[i])
    else:
        for i in range(0, len(temp3)):
            C[i] = int(temp3[i])
        C.reverse()
        C.append(0)
        C.reverse()

    if selected.get() == 1:
        temp = RED_Q_Q([A, B])
        temp1 = temp[0]
        temp2 = temp[1]
        s = ''
        if temp1[0] == 1:
            s += '-'
            for i in range(1, len(temp1)):
                s += str(temp1[i])
        else:
            for i in range(1, len(temp1)):
                s += str(temp1[i])
        s1 = ''
        for i in range(0, len(temp2)):
            s1 += str(temp2[i])
        txt33.insert(0, s + "/" + s1)
    elif selected.get() == 2:
        b = INT_Q_B(A, B)
        if b:
            s = "Да"
        else:
            s = "Нет"
        txt33.insert(0, s)
    elif selected.get() == 3:
        temp = A.copy()
        s = ''
        if temp[0] == 1:
            s += '-'
            for i in range(1, len(temp)):
                s += str(temp[i])
        else:
            for i in range(1, len(temp)):
                s += str(temp[i])
        txt33.insert(0, s + "/1")
    elif selected.get() == 4:
        temp = TRANS_Q_Z([A, B])
        s = ''
        if temp[0] == 1:
            s += '-'
            for i in range(1, len(temp)):
                s += str(temp[i])
        else:
            for i in range(1, len(temp)):
                s += str(temp[i])
        txt33.insert(0, s)
    elif selected.get() == 5:
        temp1, temp2 = ADD_QQ_Q(A, B, C, D)
        s = ''
        if temp1[0] == 1:
            s += '-'
            for i in range(1, len(temp1)):
                s += str(temp1[i])
        else:
            for i in range(1, len(temp1)):
                s += str(temp1[i])
        s1 = ''
        for i in range(0, len(temp2)):
            s1 += str(temp2[i])
        txt33.insert(0, s + "/" + s1)
    elif selected.get() == 6:
        temp1, temp2 = SUB_QQ_Q([A, B], [C, D])
        s = ''
        if temp1[0] == 1:
            s += '-'
            for i in range(1, len(temp1)):
                s += str(temp1[i])
        else:
            for i in range(1, len(temp1)):
                s += str(temp1[i])
        s1 = ''
        for i in range(0, len(temp2)):
            s1 += str(temp2[i])
        txt33.insert(0, s + "/" + s1)
    elif selected.get() == 7:
        temp1, temp2 = MUL_QQ_Q([A, B], [C, D])
        s = ''
        if temp1[0] == 1:
            s += '-'
            for i in range(1, len(temp1)):
                s += str(temp1[i])
        else:
            for i in range(1, len(temp1)):
                s += str(temp1[i])
        s1 = ''
        for i in range(0, len(temp2)):
            s1 += str(temp2[i])
        txt33.insert(0, s + "/" + s1)
    elif selected.get() == 8:
        temp1, temp2 = DIV_QQ_Q(A, B, C, D)
        print(temp1)
        print(temp2)
        s = ''
        if temp1[0] == 1:
            s += '-'
            for i in range(1, len(temp1)):
                s += str(temp1[i])
        else:
            for i in range(1, len(temp1)):
                s += str(temp1[i])
        s1 = ''
        for i in range(0, len(temp2)):
            s1 += str(temp2[i])
        txt33.insert(0, s + "/" + s1)


def clicked4():
    sm1 = txt41.get()
    sm2 = txt42.get()
    s1 = txt43.get()
    s2 = txt44.get()
    m = int(sm1)
    n = int(sm2)
    arr = [C] * (m + 1)
    j = 0
    while s1.find(" ") != -1:
        temp1 = s1[0:s1.find("/")]
        temp2 = s1[s1.find("/") + 1:s1.find(" ")]
        A = []
        B = []
        A = [0] * len(temp1)
        B = [0] * len(temp2)
        if temp1[0] == '-':
            A[0] = 1
            for i in range(1, len(temp1)):
                A[i] = int(temp1[i])
        else:
            for i in range(0, len(temp1)):
                A[i] = int(temp1[i])
            A.reverse()
            A.append(0)
            A.reverse()
        for i in range(0, len(temp2)):
            B[i] = int(temp2[i])
        arr[j] = C(A, B)
        s1 = s1[s1.find(" ") + 1:]
        j += 1
    temp1 = s1[0:s1.find("/")]
    temp2 = s1[s1.find("/") + 1:len(s1)]
    A = [0] * len(temp1)
    B = [0] * len(temp2)
    if temp1[0] == '-':
        A[0] = 1
        for i in range(1, len(temp1)):
            A[i] = int(temp1[i])
    else:
        for i in range(0, len(temp1)):
            A[i] = int(temp1[i])
        A.reverse()
        A.append(0)
        A.reverse()
    for i in range(0, len(temp2)):
        B[i] = int(temp2[i])
    arr[j] = C(A, B)
    arr1 = [C] * (n + 1)
    j = 0
    while s2.find(" ") != -1:
        temp1 = s2[0:s2.find("/")]
        temp2 = s2[s2.find("/") + 1:s2.find(" ")]
        A = []
        B = []
        A = [0] * len(temp1)
        B = [0] * len(temp2)
        if temp1[0] == '-':
            A[0] = 1
            for i in range(1, len(temp1)):
                A[i] = int(temp1[i])
        else:
            for i in range(0, len(temp1)):
                A[i] = int(temp1[i])
            A.reverse()
            A.append(0)
            A.reverse()
        for i in range(0, len(temp2)):
            B[i] = int(temp2[i])
        arr1[j] = C(A, B)
        s2 = s2[s2.find(" ") + 1:]
        j += 1
    temp1 = s2[0:s2.find("/")]
    temp2 = s2[s2.find("/") + 1:len(s2)]
    A = [0] * len(temp1)
    B = [0] * len(temp2)
    if temp1[0] == '-':
        A[0] = 1
        for i in range(1, len(temp1)):
            A[i] = int(temp1[i])
    else:
        for i in range(0, len(temp1)):
            A[i] = int(temp1[i])
        A.reverse()
        A.append(0)
        A.reverse()
    for i in range(0, len(temp2)):
        B[i] = int(temp2[i])
    arr1[j] = C(A, B)
    txt45 = Entry(tab4, width=20)
    txt45.grid(column=0, row=15)
    if selected.get() == 1:
        arr = ADD_PP_P(arr, arr1)
        s = ''
        for i in range(0, m + 1):
            temp1 = arr[i][0]
            if temp1[0] == 1:
                s += '-'
                for j in range(1, len(temp1)):
                    s += str(temp1[j])
            else:
                for j in range(1, len(temp1)):
                    s += str(temp1[j])
            s += "/"
            temp2 = arr[i][1]
            for k in range(0, len(temp2)):
                s += str(temp2[k])
            s += ' '
        txt45.insert(0, s)
    elif selected.get() == 2:
        arr = SUB_PP_P(arr, arr1)
        s = ''
        for i in range(0, m + 1):
            temp1 = arr[i][0]
            if temp1[0] == 1:
                s += '-'
                for j in range(1, len(temp1)):
                    s += str(temp1[j])
            else:
                for j in range(1, len(temp1)):
                    s += str(temp1[j])
            s += "/"
            temp2 = arr[i][1]
            for k in range(0, len(temp2)):
                s += str(temp2[k])
            s += ' '
        txt45.insert(0, s)
    elif selected.get() == 3:
        print()
    elif selected.get() == 4:
        print()
    elif selected.get() == 5:
        print()
    elif selected.get() == 6:
        print()
    elif selected.get() == 7:
        print()
    elif selected.get() == 8:
        print()
    elif selected.get() == 9:
        print()
    elif selected.get() == 10:
        print()
    elif selected.get() == 11:
        print()
    elif selected.get() == 12:
        print()




window = Tk()
window.title("Kolok pain 666")
window.geometry('1800x700')
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
lbl1 = Label(tab1)
lbl2 = Label(tab2)
tab_control.add(tab1, text='Модуль 1')
tab_control.add(tab2, text='Модуль 2')
tab_control.add(tab3, text='Модуль 3')
tab_control.add(tab4, text='Модуль 4')
selected = IntVar()
btn1 = Button(tab1, text="Рассчитать", command=clicked)
btn2 = Button(tab2, text="Рассчитать", command=clicked2)
btn3 = Button(tab3, text="Рассчитать", command=clicked3)
btn4 = Button(tab4, text="Рассчитать", command=clicked4)
txt11 = Entry(tab1, width=20)
txt12 = Entry(tab1, width=20)
txt21 = Entry(tab2, width=20)
txt22 = Entry(tab2, width=20)
txt31 = Entry(tab3, width=20)
txt32 = Entry(tab3, width=20)
txt41 = Entry(tab4, width=20)
txt42 = Entry(tab4, width=20)
txt43 = Entry(tab4, width=20)
txt44 = Entry(tab4, width=20)

# Модуль 1
rad11 = Radiobutton(tab1, text='N - 1', value=1, variable=selected)
rad12 = Radiobutton(tab1, text='N - 2', value=2, variable=selected)
rad13 = Radiobutton(tab1, text='N - 3', value=3, variable=selected)
rad14 = Radiobutton(tab1, text='N - 4', value=4, variable=selected)
rad15 = Radiobutton(tab1, text='N - 5', value=5, variable=selected)
rad16 = Radiobutton(tab1, text='N - 6', value=6, variable=selected)
rad17 = Radiobutton(tab1, text='N - 7', value=7, variable=selected)
rad18 = Radiobutton(tab1, text='N - 8', value=8, variable=selected)
rad19 = Radiobutton(tab1, text='N - 9', value=9, variable=selected)
rad110 = Radiobutton(tab1, text='N - 10', value=10, variable=selected)
rad111 = Radiobutton(tab1, text='N - 11', value=11, variable=selected)
rad112 = Radiobutton(tab1, text='N - 12', value=12, variable=selected)
rad113 = Radiobutton(tab1, text='N - 13', value=13, variable=selected)
rad114 = Radiobutton(tab1, text='N - 14', value=14, variable=selected)

# Модуль 2
rad21 = Radiobutton(tab2, text='Z - 1', value=1, variable=selected)
rad22 = Radiobutton(tab2, text='Z - 2', value=2, variable=selected)
rad23 = Radiobutton(tab2, text='Z - 3', value=3, variable=selected)
rad24 = Radiobutton(tab2, text='Z - 4', value=4, variable=selected)
rad25 = Radiobutton(tab2, text='Z - 5', value=5, variable=selected)
rad26 = Radiobutton(tab2, text='Z - 6', value=6, variable=selected)
rad27 = Radiobutton(tab2, text='Z - 7', value=7, variable=selected)
rad28 = Radiobutton(tab2, text='Z - 8', value=8, variable=selected)
rad29 = Radiobutton(tab2, text='Z - 9', value=9, variable=selected)
rad210 = Radiobutton(tab2, text='Z - 10', value=10, variable=selected)

# Модуль 3
rad31 = Radiobutton(tab3, text='Q - 1', value=1, variable=selected)
rad32 = Radiobutton(tab3, text='Q - 2', value=2, variable=selected)
rad33 = Radiobutton(tab3, text='Q - 3', value=3, variable=selected)
rad34 = Radiobutton(tab3, text='Q - 4', value=4, variable=selected)
rad35 = Radiobutton(tab3, text='Q - 5', value=5, variable=selected)
rad36 = Radiobutton(tab3, text='Q - 6', value=6, variable=selected)
rad37 = Radiobutton(tab3, text='Q - 7', value=7, variable=selected)
rad38 = Radiobutton(tab3, text='Q - 8', value=8, variable=selected)

# Модуль 4
rad41 = Radiobutton(tab4, text='P - 1', value=1, variable=selected)
rad42 = Radiobutton(tab4, text='P - 2', value=2, variable=selected)
rad43 = Radiobutton(tab4, text='P - 3', value=3, variable=selected)
rad44 = Radiobutton(tab4, text='P - 4', value=4, variable=selected)
rad45 = Radiobutton(tab4, text='P - 5', value=5, variable=selected)
rad46 = Radiobutton(tab4, text='P - 6', value=6, variable=selected)
rad47 = Radiobutton(tab4, text='P - 7', value=7, variable=selected)
rad48 = Radiobutton(tab4, text='P - 8', value=8, variable=selected)
rad49 = Radiobutton(tab4, text='P - 9', value=9, variable=selected)
rad410 = Radiobutton(tab4, text='P - 10', value=10, variable=selected)
rad411 = Radiobutton(tab4, text='P - 11', value=11, variable=selected)
rad412 = Radiobutton(tab4, text='P - 12', value=12, variable=selected)

# Модуль 1 - вывод кнопки и текста
txt11.grid(column=0, row=0)
txt12.grid(column=1, row=0)
btn1.grid(column=3, row=0)

# Модуль 1 - вывод Radio
rad11.grid(column=0, row=1)
rad12.grid(column=0, row=2)
rad13.grid(column=0, row=3)
rad14.grid(column=0, row=4)
rad15.grid(column=0, row=5)
rad16.grid(column=0, row=6)
rad17.grid(column=0, row=7)
rad18.grid(column=0, row=8)
rad19.grid(column=0, row=9)
rad110.grid(column=0, row=10)
rad111.grid(column=0, row=11)
rad112.grid(column=0, row=12)
rad113.grid(column=0, row=13)
rad114.grid(column=0, row=14)

# Модуль 2 - вывод кнопки и текста
txt21.grid(column=0, row=0)
txt22.grid(column=1, row=0)
btn2.grid(column=3, row=0)

# Модуль 2 - вывод Radio
rad21.grid(column=0, row=1)
rad22.grid(column=0, row=2)
rad23.grid(column=0, row=3)
rad24.grid(column=0, row=4)
rad25.grid(column=0, row=5)
rad26.grid(column=0, row=6)
rad27.grid(column=0, row=7)
rad28.grid(column=0, row=8)
rad29.grid(column=0, row=9)
rad210.grid(column=0, row=10)

# Модуль 3 - вывод Кнопки и текста
txt31.grid(column=0, row=0)
txt32.grid(column=1, row=0)
btn3.grid(column=3, row=0)

# Модуль 3 - вывод Radio
rad31.grid(column=0, row=1)
rad32.grid(column=0, row=2)
rad33.grid(column=0, row=3)
rad34.grid(column=0, row=4)
rad35.grid(column=0, row=5)
rad36.grid(column=0, row=6)
rad37.grid(column=0, row=7)
rad38.grid(column=0, row=8)

# Модуль 4 - вызов кнопки и текста
txt41.grid(column=0, row=0)
txt42.grid(column=1, row=0)
txt43.grid(column=0, row=1)
txt44.grid(column=1, row=1)
btn4.grid(column=3, row=0)

# Модуль 4 - вызов Radio
rad41.grid(column=0, row=2)
rad42.grid(column=0, row=3)
rad43.grid(column=0, row=4)
rad44.grid(column=0, row=5)
rad45.grid(column=0, row=6)
rad46.grid(column=0, row=7)
rad47.grid(column=0, row=8)
rad48.grid(column=0, row=9)
rad49.grid(column=0, row=10)
rad410.grid(column=0, row=11)
rad411.grid(column=0, row=12)
rad412.grid(column=0, row=13)

tab_control.pack(expand=1, fill='both')

window.mainloop()
