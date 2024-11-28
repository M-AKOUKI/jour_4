def moyenne(note1,note2,note3):
    return (note1+note2+note3)/3

x = int(input("Entrez une note:"))
y = int(input("Entrez une note:"))
z = int(input("Entrez une note:"))

moyenne_etudiant = moyenne(x,y,z)

def élève(moy):
    if moy >= 15 and moy <= 20:
        print("Très bon élève")   
    elif moy >= 11 and moy <= 14:
        print("bon élève")
    elif moy >= 8 and moy <= 10:
        print("élève moyen")
    else:
        if moy >= 0 and moy <= 7:
            print("élève devant faire des efforts")

élève(moyenne_etudiant)