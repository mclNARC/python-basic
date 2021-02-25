nomes = []
for aa in range (0 ,5) :
    add = input ("nome:" + str (aa + 1)+ "  ")
    nomes.append(add)
print (f'{nomes}')


for i in range (0,1):
        outro_nome = input("Digite mais 1 nome:"+ str (i + 1) +" ")
        nomes.append(outro_nome)
print (nomes)

for y in range (0,1) :
    mais_um =  input("digite mais um nome:"+ str (y + 1) + " ")
    nomes.insert(1,mais_um)
print(nomes)


