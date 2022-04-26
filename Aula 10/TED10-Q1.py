# Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos 20 números, o algoritmo deve escrever esses 20 números lidos na ordem inversa.

import random

numeros = []

for x in range(1, 21):
    ale = random.randrange(1, 1000)
    numeros.append(ale)
print(numeros)

numeros.reverse()
print('=' *100)
print(numeros)