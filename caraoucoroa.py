import random

#lançamento de uma moeda
lancamento = [random.choice(['Cara','Coroa']) for _ in range(20)]

print(lancamento)
print(lancamento.count('Cara'))
