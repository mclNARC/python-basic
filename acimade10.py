matriz = []
ct = 0

for i in range(4):
    matriz.append(int(input('Digite um número: ')))

for i in matriz:
    if i > 10:
        ct += 1

print(f'acima de 10= {ct}')