anos = []
for aa in range (0 ,5) :
    add = input ("ano:" + str (aa + 1)+ "  ")
    anos.append(add)
    anos.sort()
print (f'{anos}')
anos.sort(reverse=True)
print (anos)
