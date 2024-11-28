def positif_negatif(nombre):
    int(nombre)
    if nombre > 0:
        print(nombre,"est positif")
    elif nombre == 0:
        print(nombre,"est nul")
    else:
        print(nombre,"est negatif")

positif_negatif(5)
positif_negatif(0)
positif_negatif(-5)