#Consutra uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. Depois:
#Imprima o resultado da soma de todos os valores da matriz no terminal;
#E, criei uma nova matriz B, no qual cada item seja o valor da matriz A * 3;


import random

matriz_10x10_a = []

for i in range(10):
    
    matriz_aux = []
    
    for j in range(10):    
        matriz_aux.append(random.randint(0, 100))
    
    matriz_10x10_a.append(matriz_aux)        


for linha in matriz_10x10_a:
    print(linha)
    
print('=' * 100)

resultado_soma = 0

for l in matriz_10x10_a:
    
    for c in l:
        
        resultado_soma += c

print(f'Resultado da Soma = {resultado_soma}')

matriz_10x10_b = []

for l in range(0, len(matriz_10x10_a)):
    
    lista_auxiliar = []
    
    for c in range(0, len(matriz_10x10_a[l])):
        
        resultado_multiplicacao = matriz_10x10_a[l][c] * 3
        lista_auxiliar.append(resultado_multiplicacao)
        
    matriz_10x10_b.append(lista_auxiliar)
print('=' * 100)
print('Nova matriz')       
print(matriz_10x10_b)