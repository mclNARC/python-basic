nomes = []
for aa in range (0 ,4) :
    add = input ("nome" + str (aa + 1)+ "  ")
    nomes.append(add)

nomes.insert(1,'Lima')
print (f'{nomes}')
