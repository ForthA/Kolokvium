from Tarasov_Kostya import COM_NN_D
from Tarasov_Kostya import NZER_N_B
# Тут типа main
A = []
print('Ввод A')
A = list(map(int, input().split()))
print(A)
print('Ввод B')
B = []
B = list(map(int, input().split()))
print(COM_NN_D(A, B))
NZER_N_B(A)
NZER_N_B(B)
