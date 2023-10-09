def calcola_perimetro():
    print("Calcoliamo il perimetro di una figura geometrica fra le seguenti scelte")
    print("scegli!")
    print("1 - Rettangolo")
    print("2 - Quadrato")
    print("3 - Cerchio")
    
    scelta = int(input(">>> "))
    
    if scelta == 1:
        latoR1 = float(input("Inserisci il primo lato del rettangolo in cm: "))
        latoR2 = float(input("Inserisci il secondo lato del rettangolo in cm: "))
        perimetroR = latoR1*2 + latoR2*2
        print("Il perimetro del rettangolo è: ", perimetroR, "cm")
    elif scelta == 2:
        latoQ = float(input("Inserisci il lato del quadrato in cm: "))
        perimetroQ = latoQ*4
        print("Il perimetro del quadrato è", perimetroQ, "cm")
    elif scelta == 3:
        raggio = float(input("Inserisci il raggio del cerchio in cm: "))
        circonferenza = 2*3.14*raggio
        print("La circonferenza del cerchio misura: ", circonferenza, "cm")
    else:
        print("inserisci una scelta valida")

calcola_perimetro()