def calculo_iprf (salarioBruto) :
    return (salarioBruto - salarioBruto*11/100)


def calculo_inss (salarioBruto) :
    return (salarioBruto - salarioBruto*8/100)


def desconto_sindicato (salarioBruto) :
    return (salarioBruto - salarioBruto*5/100)



def salario_liquido (salarioBruto) :
    return (salarioBruto - salarioBruto*5/100 - salarioBruto*8/100 - salarioBruto*11/100 )


def total_descontado (salarioBruto) :
    return ( salarioBruto - salarioBruto*24/100)


#def salario_bruto (horasTrabalhadas , valorDaHora)
 #   return (horasTrabalhadas*valorDaHora)

horasTrabalhadas = int (input("quantas horas trabalhadas por mês?:"))


valorDaHora = float (input("qual valor da sua hora de trabalho ?:"))


salarioBruto = valorDaHora*horasTrabalhadas

print ("valor do salário bruto:", salarioBruto)

descontoDoIprf = calculo_iprf(salarioBruto)
print("seu salário menos o desconto referente ao IPRF",descontoDoIprf)
