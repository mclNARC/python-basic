produto1 = float (input("qual valor do primeiro produto ?:"))
produto2 = float (input("qual valor do segundo produto ?:"))
produto3 = float (input("qual valor do terceiro produto ?:"))

if produto1 < produto2 and produto1 < produto3  :
    print("produto 1 é o mais barato")


elif produto2 < produto1 and produto2 < produto3 :
    print ("produto 2 é o mais barato ")



else :
    print("produto 3 é o mais barato")
