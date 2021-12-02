from unicodedata import normalize


def tolet(x):
    "transforme l'entier [x] en la [x]ième lettre majuscule (modulo 26)"
    return chr(65 + x % 26)


def toint(c):
    "tranforme la lettre majuscule [c] en sa position dans l'alphabet (de 0 à 25)"
    return ord(c) - 65


def shift(c, d):
    """décale la lettre [c] de k positions dans l'alphabet (modulo 26)
     où [k] est la position de la lettre [d] dans l'alphabet"""
    return tolet(toint(c) + toint(d))


def unshift(c, d):
    """décale la lettre [c] de k positions dans l'alphabet (modulo 26)
     où [k] est la position de la lettre [d] dans l'alphabet"""
    return tolet(toint(c) - toint(d))

def extraireSousTextes2(m,k):
    lesTextes = [""]*k
    for i in range(len(m)):
        lesTextes[i%k]+=m[i]
    return lesTextes

def ic(freq):
    n=0
    icSum=0
    for x in freq:
        nx=freq[x]  # nombre d'occurences du caractère x
        n=n+nx
        icSum+= nx*(nx-1)
    ic = icSum/(n*(n-1))
    return ic


def calculICMoyen(textes):
    resultat = 0.0
    freq = {}
    icTotal = 0
    for mot in textes:
        freq = {}
        for c in mot:
            freq[c] = freq.get(c, 0) + 1
        icTotal += ic(freq)
    ##ic

    return icTotal / len(textes)

def nettoie(m):
    "nettoie la chaîne [m] en ne gardant que les lettres débarassées de leurs accents et passées en majuscules"
    return ''.join([c for c in normalize('NFKD',m).upper().strip() if ord(c)>64 and ord(c)<91])


def trouveLeE(texte):
    freq = {}
    for mot in texte:
        ##frequence
        for x in mot:
            freq[x] = freq.get(x, 0) + 1
    l = [(freq[c], c) for c in freq]
    l.sort(reverse=True)
    return l[0][1]


def calculerDecalage(texte):
    resultat = (toint(trouveLeE(texte)) - toint('E')) % 26
    return resultat


def calculerDecalages(textes):
    resultat = []
    for i in textes:
        resultat.append(calculerDecalage(i))
    return resultat

def constructionCle(decalages):
    cle=''
    for i in decalages:
        cle+=(tolet(i))
    return cle

def chiffrementVigenere(texteClair,cle):
    texteClair=''.join([x for x in texteClair if x.isalpha()]).upper()
    chiffre =''
    i = 0
    while i<len(texteClair):
        for c in cle:
            ##chiffre+=tolet((toint(texteClair[i])+toint(c))%26)
            chiffre+=shift(texteClair[i],c)
            i+=1
            if not(i<len(texteClair)):
                return chiffre
    return chiffre

def constructionCleDechiffrement(cle):
    cleResultat=''
    for i in cle:
        cleResultat+=tolet((26-toint(i))%26)
    return cleResultat

def remettreEnForme(textdechiffre,texts : list):
    letexte=""
    index=0
    for i in texts:
        for j in range(len(i)-1):
            if(i[j].isalpha()):
                letexte+=textdechiffre[index]
                index+=1
            else:
                letexte+=i[j]
        letexte+="\n"
    return letexte



if __name__ == "__main__":
    reader = open("message.vig", "r")
    txt1 = reader.readlines()
    txt=txt1.copy()
    for i in txt :
        i = i[:-1]
    texte = "".join(txt)
    texte = nettoie(texte)
    print(txt)
    n=1000
    for i in range(1,40):
        moyen = calculICMoyen(extraireSousTextes2(texte,i))
        #print(moyen," ",i)
        if(moyen>0.070):
            n = min(i,n)
            print(moyen," ",i)
    reader.close()
    print(n)

    liste = extraireSousTextes2(texte,n)

    cle = constructionCle(calculerDecalages(liste))
    textedechiffre = chiffrementVigenere(texte,constructionCleDechiffrement(cle))

    print(remettreEnForme(textedechiffre,txt))






