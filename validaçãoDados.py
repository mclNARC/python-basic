sexo = str (input("digite seu sexo [F/M]:")).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input("dados invalidos digite seu sexo [F/M]:")).strip().upper()[0]
print(f"{sexo}:<-----------")