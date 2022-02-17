def imenica_muskog_roda(text):      #ncm
    a=[]
    a.append(text)
    a.append(text+'i')  #mnozina
    #a.append(text+'ovi')  #mnozina
    a.append(text+'a')  #genitiv
    a.append(text+'e')  #akuzativ mn
    a.append(text+'u')  #lokativ
    a.append(text+'om') #instrumental
    a.append(text+'ima')    #instrumental mn
    return a
def imenica_zenskog_roda_na_a(text):       #ncf
    a=[]
    a.append(text)
    a.append(text[:-1]+'e')  #mnozina
    a.append(text[:-1]+'u')  #akuzativ
    a.append(text[:-1]+'om')  #instrumental
    a.append(text[:-1]+'ama')  #instrumental mn
    return a
def imenica_srednjeg_roda(text):       #ncn
    a=[]
    if (text[-3:]=="nje"):
        a.append(text)
        a.append(text[:-1]+'u')  #lokativ
        a.append(text[:-1]+'a')  #akuzativ mn
        a.append(text[:-1]+'em')  #instrumental
        a.append(text[:-1]+'ima')  #instrumental mn
        return a
    elif (text[-1:]=="e"):
        a.append(text)
        a.append(text[:-1]+'u')  #lokativ
        a.append(text[:-1]+'a')  #akuzativ mn
        a.append(text[:-1]+'em')  #instrumental
        a.append(text[:-1]+'ima')  #instrumental mn 
        return a   
    else:
        a.append(text)
        a.append(text[:-1]+'u')  #lokativ
        a.append(text[:-1]+'a')  #akuzativ mn
        a.append(text[:-1]+'om')  #instrumental
        a.append(text[:-1]+'ima')  #instrumental mn
        return a
def pridev(text):         
    a=[]
    if(text[-1]=='i'):
        a.append(text)
        t=text[:-1]
        a.append(t+'i')  #nom mr
        a.append(t+'a')  #nom za
        a.append(t+'o')  #nom sr
        a.append(t+'e')  #nom mn zr
        a.append(t+'u')  #lokativ zr
        a.append(t+'ih')  #genitiv mn
        a.append(t+'im')  #instrumental j mr
        a.append(t+'og')  #genitiv mr
        a.append(t+'om')  #instrumental j zr
    elif(text[-2:]=='an'):
        a.append(text)
        t=text[:-2]
        a.append(t+'ni')  #nom mr
        a.append(t+'na')  #nom za
        a.append(t+'no')  #nom sr
        a.append(t+'ne')  #nom mn zr
        a.append(t+'nu')  #lokativ zr
        a.append(t+'nih')  #genitiv mn
        a.append(t+'nim')  #instrumental j mr
        a.append(t+'nog')  #genitiv mr
        a.append(t+'nom')  #instrumental j zr   
    else:
        a.append(text)
        a.append(text+'i')  #nom mr
        a.append(text+'a')  #nom za
        a.append(text+'o')  #nom sr
        a.append(text+'e')  #nom mn zr
        a.append(text+'u')  #lokativ zr
        a.append(text+'ih')  #genitiv mn
        a.append(text+'im')  #instrumental j mr
        a.append(text+'og')  #genitiv mr
        a.append(text+'om')  #instrumental j zr
    return a
def deklinacije(lemma, pos):
    pos = pos.upper()[:3]
    if pos=="NCM" : var=imenica_muskog_roda(lemma)
    elif pos=="NCF" : var=imenica_zenskog_roda_na_a(lemma)
    elif pos=="NCN" : var=imenica_srednjeg_roda(lemma)
    elif pos=="AGP" : var=pridev(lemma)
    elif pos=="AGC" : var=pridev(lemma)
    elif pos=="ASC" : var=pridev(lemma)
    else: var=[lemma]
    return(var) 