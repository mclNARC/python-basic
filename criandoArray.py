cidades = []
paises = []
i = 0
while i < 3 :
    add = input ( "digite 3 cidades:")
    i = i +1
    cidades.append(add)
print (f'{cidades}metodo1')

for i in range (0,3) :
    adc = input("digite 3 países:"+ str (i+1)+ " ")
    paises.append(adc)
print (f'{paises}metodo 2')

