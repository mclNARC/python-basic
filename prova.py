def main () :
    velas_altura = int(input("Quantas velas?"))
    velas = []

    for i in range (0, velas_altura) :
        varvl = input ("varvl" + str  (i+1 ) + "  ")
        velas.append(varvl)
    print (max(velas, key=int))
    print (f"{velas}")
main ()






