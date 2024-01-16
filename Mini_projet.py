def saisie():
    n=int(input("Donner 1=<n=<100: "))
    while not 1=<n=<100:
        n=int(input("Donner 1=<n=<100: "))
    return n 
def verif_1(T,N,i):
    #Initialisation de verif
    verif=True
    #Etape 1 (verifier que la chaine n'existe q'une cet fois)
    f=i
    while not f==N-2:
        if T[i]==T[f+1]:
            verif=False
        f+=1
    #Etape 2
    s=T[i]
    for j in range(len(T[i])):
        if not("a"=<s[j]=<"z" or "A"=<s[j]=<"B"):
            verif=False
    return verif       
def remp1(T):
    for i in range(N):
        T[i]=input("Donner Votre Nom BENPrenom_du_pere Nom")
        while not 
