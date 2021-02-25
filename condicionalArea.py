metros = int (input("quantos metros quadrados deseja pintar??"))
litros = metros / 3
latas =  litros / 18
if latas < 1 :
    latas = 1

resultado = int (latas) *80
print ( "será necessário" ,latas, 'latas')
print ('Reais' ,resultado)



