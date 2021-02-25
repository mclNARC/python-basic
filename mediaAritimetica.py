"""
Entrei no banco e quero saber o meu tempo médio de espera.
Faça um programa que calcule e mostre a média aritmética de um cliente, baseado nos tempos de espera dos clientes anteriores (máximo 5  clientes).
"""



def main():



    numero_clientes = int (input("quantos clientes há na sua frente ?:"))


    tempo_de_espera = 0

    cont = 0

    while cont < tempo_de_espera :
        print (cont)

        atendimento = atendimento + tempo_de_espera
        tempo_de_espera = float(input("tempo estimado de espera", + str(cont)))
        cont = cont + 1

    media_aritimetica = (tempo_de_espera)/(numero_clientes)
    print ("tempo estimado de atendimento " , media_aritimetica)


main()








