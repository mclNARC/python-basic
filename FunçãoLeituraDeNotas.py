"""
(J- Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Gênero Inválido.)

(K- Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.)

(I- Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo. )

"""

#genero = str(input("informe seu gênero: [M/F]")).strip().upper()[0]
#print(genero)
#while genero not in "MF":
#    genero = str(input("dados inválidos, digite seu gênero novamente : [M/F]:")).strip().upper()[0]
#print("gênero {} registrado com sucesso".format(genero))


#primeira_nota = float (input("Insira a primeira nota:"))

#segunda_nota = float (input("Insira a segunda nota:"))

#media = (primeira_nota + segunda_nota)/2

#if media < 7:
   #print ("Aluno reprovado com media = " , media)

#if media >= 7 :
    #print("Aluno aprovado com media = " ,media)


#elif media >= 10 :
    #print ("Aprovado com Distinção com media = ", media)


num = int (input("digite um número:"))

if num < 0 :
    print ("Numero negativo", num)

else:
    print ("numero positivo", num)

