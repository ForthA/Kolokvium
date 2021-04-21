from C import C
from resultant_m3 import *


# P - 3
# Умножение коэфа с многочленом
def MUL_PQ_P(arr, D):
    for i in range(0, len(arr)):
        arr[i].A, arr[i].B = MUL_QQ_Q([arr[i].A, arr[i].B], [D.A, D.B])
    return arr
