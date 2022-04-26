# Faça um algoritmo para ler 50 números e armazenar em um vetor VET, verificar e escrever se existem números repetidos no vetor VET e em que posições se
# encontram.

from collections import defaultdict
import random


VET = []

for x in range(1, 51):
    NumAle = random.randrange(1, 50)
    VET.append(NumAle)

print(VET)
print('-' * 100)

chaves = defaultdict(list)

for chave, valor in enumerate(VET):
    chaves[valor].append(chave)

for valor in chaves:
    if len(chaves[valor]) > 1:
        print(f'O numero {valor} se repete nos indecis {chaves[valor]}')