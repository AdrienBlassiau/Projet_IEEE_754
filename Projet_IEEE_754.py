def conversionIEEE(nombreDeBase):       # Procédure de conversion d'un nombre décimal en binaire.

    # On entre le signe en mémoire.
    
    signe=""
    if  nombreDeBase>=0:                    
        signe="0"
    else:
        signe="1"
        nombreDeBase=-nombreDeBase
    
    # On s'occupe d'abord de convertir la partie entière du nombre.
    
    N=floor(nombreDeBase)
    debutMantisse=""
    tab1=[1]*10000
    if N==0:
        debutMantisse="0"
    elif N>0:
        i=0
        while N>0:
            tab1[i]=N%2
            N=N//2
            i=i+1
        i=i-1
        for j in range(i+1):
            debutMantisse=debutMantisse+str(tab1[i-j])
    
    # On s'occupe ensuite de convertir la partie décimale du nombre.
    
    tab2=[0]*(10000)
    dec=(nombreDeBase-floor(nombreDeBase))
    
    for r in range (10000):
        dec=dec*2
        if dec<1:
            tab2[r]="0"
        else:
            tab2[r]="1"
            dec=dec-1
    mantisse="".join(tab2)
    
    # On lie partie entière et partie décimale.
    
    mantisse=debutMantisse+","+ mantisse
    
    
    # On calcule l'exposant et enlève la virgule et le 1 en trop.
    
    a=0
    b=0
    mantisse=list(mantisse)
    
    while mantisse[b] !=",":
        b=b+1  
    while mantisse[a] !="1":
        a=a+1 

    
    if a<b:
        exposant=b-a-1
    else:
        exposant=b-a
    
    mantisse=mantisse[a+1 :]
    mantisse="".join(mantisse)
    mantisse=mantisse.split(",")
    mantisse="".join(mantisse)
    
    # On convertit l'exposant.
    
    exposant=1023+exposant
    print ("L'exposant vaut : ",exposant)
    chaine1=""
    tab3=[0]*11
    
    l=0
    while exposant>0:
        tab3[l]=exposant%2
        exposant=exposant//2
        l=l+1
    l=l-1
    for b in range(l+1):
        chaine1=chaine1+str(tab3[l-b])
    
    while len(chaine1)!=11:
        chaine1="0"+chaine1
    
    # On affiche le nombre converti en binaire.
    
    nombreF=signe+chaine1+mantisse
    nombreF=nombreF[:64]
    lenTot=len(nombreF)
    print("Le nombre convertit en binaire est :", nombreF)
    
    convertionHexa(nombreF) # On appelle la procédure de conversion en hexadécimal.




def convertionHexa(nombreF):  # Procédure de conversion d'un nombre binaire en hexadécimal.
    Hexa=""
    for q in range (0,65,4):
        nombreFHexa=nombreF[q :q+4]
        if nombreFHexa=="0000":
            Hexa=Hexa+"0"
        elif nombreFHexa=="0001":
            Hexa=Hexa+"1"
        elif nombreFHexa=="0010":
            Hexa=Hexa+"2"
        elif nombreFHexa=="0011":
            Hexa=Hexa+"3"
        elif nombreFHexa=="0100":
            Hexa=Hexa+"4"
        elif nombreFHexa=="0101":
            Hexa=Hexa+"5"
        elif nombreFHexa=="0110":
            Hexa=Hexa+"6"
        elif nombreFHexa=="0111":
            Hexa=Hexa+"7"
        elif nombreFHexa=="1000":
            Hexa=Hexa+"8"
        elif nombreFHexa=="1001":
            Hexa=Hexa+"9"
        elif nombreFHexa=="1010":
            Hexa=Hexa+"A"
        elif nombreFHexa=="1011":
            Hexa=Hexa+"B"
        elif nombreFHexa=="1100":
            Hexa=Hexa+"C"
        elif nombreFHexa=="1101":
            Hexa=Hexa+"D"
        elif nombreFHexa=="1110":
            Hexa=Hexa+"E"
        elif nombreFHexa=="1111":
            Hexa=Hexa+"F"
    
    print("Le nombre convertit en héxadécimal est :", Hexa+""+"H")
    
    
    
    
    
def conversionDécimal(hexa):            # Procédure de conversion d'un nombre hexadécimal en binaire puis décimal.


    chabin=""   # Variable qui va recevoir la chaine binaire.
    
    # On le convertit en une chaine binaire.
    
    for i in hexa:
        if i=="0":
            chabin=chabin+"0000"
        elif i=="1":
            chabin=chabin+"0001"
        elif i=="2":
            chabin=chabin+"0010"
        elif i=="3":
            chabin=chabin+"0011"
        elif i=="4":
            chabin=chabin+"0100"
        elif i=="5":
            chabin=chabin+"0101"
        elif i=="6":
            chabin=chabin+"0110"
        elif i=="7":
            chabin=chabin+"0111"
        elif i=="8":
            chabin=chabin+"1000"
        elif i=="9":
            chabin=chabin+"1001"
        elif i=="A":
            chabin=chabin+"1010"
        elif i=="B":
            chabin=chabin+"1011"
        elif i=="C":
            chabin=chabin+"1100"
        elif i=="D":
            chabin=chabin+"1101"
        elif i=="E":
            chabin=chabin+"1110"
        elif i=="F":
            chabin=chabin+"1111"
    
    print ("Le nombre en IEEE binaire vaut :",chabin)
    
    # On vérifie que l'utilisateur n'a pas entré un exposant avec que des 0 ou que des 1.
    
    if chabin[1:12]=="00000000000":
        print ("Impossible, l'exposant est nul")
        raise SystemExit("")
    elif chabin[1:12]=="11111111111":
        print ("Impossible, l'exposant est uniquement constitué de 1")
        raise SystemExit("")
    
    
    # On convertit la chaine binaire en nombre décimal.
    
    nbdec=""  # Résultat final.
    
    # Conversion du bit de signe.
    
    if chabin[0]=="0":
        nbdec="+"
    elif chabin[0]=="1":
        nbdec="-"
    
    # Conversion de l'exposant.
    
    expo=0 
    
    for k in range (1,12):
            if chabin[k]=="1": 
                expo=expo+(2**(11-k))
            elif chabin[k]=="0":
                expo=expo+0   
    exposant = expo-(1023) # Calcul de l'exposant. 
    
    print ("L'exposant vaut : ",exposant)
    
    # Conversion de la mantisse. 
    
    mant=1
    
    for s in range (12,len(chabin)):
        if chabin[s]=="1":
            mant=mant+(2**(11-s))
        elif chabin[s]=="0":
            mant=mant+0
    
    nbdecimal= mant*(2**exposant) # Valeur absolue du résultat en format float. 
    
    chaine=str(nbdecimal) # Conversion du float en chaine de caractères. 
    
    nbdec=nbdec+chaine  # Ajout du signe. 
    
    print ("Votre nombre en décimale vaut: ",nbdec) # On obtient le résultat décimal.













from math import*

print("*****************************Menu*****************************")
print("")
print("1.Transformez un nombre décimal en un nombre respectant la norme IEEE 754 en 64 bits hexadécimal") 
print("2.Transformez un nombre respectant la norme IEEE 754 en 64 bits hexadécimal en un nombre décimal ",end="") 
print("")
C=int(input("Entrez votre type de conversion : "))

if C==1:
    
    # On demande à l'utilisateur d'entrer le nombre.
    
    nombreDeBase=float(input("Entrez un nombre décimal à convertir dans la norme IEEE 754\n"))
    
    if nombreDeBase==0:
        
        print("Le nombre converti en hexadécimal est : 0000000000000000")
    
    else :
        
        conversionIEEE(nombreDeBase) # On appelle la fonction de conversion d'un décimal en IEEE 754 hexadécimal.


if C==2:
    
    # On demande à l'utilisateur d'entrer le nombre.
    
    hexa=input("Entrez votre nombre IEEE héxadécimal à convertir en décimal\n")

    conversionDécimal(hexa)  # On appelle la fonction de conversion d'un IEEE 754 hexadécimal en décimal.


    
















from tkinter import *

class Interface(Frame):
    
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        self.nb_clic = 0
        
        # Création de nos widgets
        self.message = Label(self, text="Vous n'avez pas cliqué sur le bouton.")
        self.message.pack()
        
        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side="left")
        
        self.bouton_cliquer = Button(self, text="Cliquez ici", fg="red",
                command=self.cliquer)
        self.bouton_cliquer.pack(side="right")
    
    def cliquer(self):
        """Il y a eu un clic sur le bouton.
        
        On change la valeur du label message."""
        
        self.nb_clic += 1
        self.message["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)

fenetre = Tk()
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()
