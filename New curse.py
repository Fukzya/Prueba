from random import randint
valores = 0
n = 0
probabilidad = 0
for i in range(8):
    valores = randint(1, 6)
    if valores == 1:
        n += 1
probabilidad = (8 / n)
print("La probabilidad de que haya un peruano es de %", probabilidad)
