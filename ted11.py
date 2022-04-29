#Consutra uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. Depois:
from  random import randint
import numpy as np
m = []
soma = []
for numeros in range(10):
    linha = []
    for coluna in range(10):
        linha.append(randint(1,100))
    m.append(linha)
    print(linha)
soma.append(m)
print("#"*100)
print("Soma dos indices da matriz : ")
print(np.sum(soma))

print("#"*100)
matrizb = np.array(m)
soma = matrizb* 3
print("mutiplicação 1")
print("Resulta na matriz B:")
print("#"*100)
print(soma)
print("#"*100)
print("finsh")
print("#"*100)