def main ():
    length = int(input('digite o tamanho do array:'))
    registro = []

    for i in range (0,length) :
        element = input("element" + str  (i+1 ) + "  ")
        registro.append(element)
    print (f":{registro}")
main ()
