import random

lancamentos=[]
for i in range(100): #serve para gerar aleatoriamente 100 vezes
    resultado=random.randint(1,6) #vai girar de 1 à 6
    lancamentos.append(resultado)

frequencia = []
for face in range(1,7):
    quantidade = lancamentos.count(face)
    frequencia.append(quantidade) #quantidade de vezes que encontrou em cada face 

print("Vetor de frequências (quantidade de vezes das faces: 1, 2, 3, 4, 5, 6)")
print(frequencia)
print("\nvetor de lançamentos (100 vezes)")
print(lancamentos)