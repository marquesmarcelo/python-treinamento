nuvem = input("Tem nuvem (S/N)")

if (nuvem == "S" or nuvem == "N"):
    
    if (nuvem == "S"):
        print("leve guarda chuva")
    else:
        print("não precisa de guarda chuva")
else:
    print("Opção invalida")
    
    
if (nuvem in ["S", "N"]):
    
    if (nuvem == "S"):
        print("leve guarda chuva")
    else:
        print("não precisa de guarda chuva")
else:
    print("Opção invalida")