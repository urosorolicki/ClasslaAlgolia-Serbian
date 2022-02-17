# %%
import itertools
import classla
#classla.download('sr')
nlp = classla.Pipeline('sr')
from deklinacije import deklinacije

from google.cloud.translate_v2.client import ENGLISH_ISO_639
from google.cloud import translate_v2 as translate
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/branimir/Projects/algolia/agpoc"
client = translate.Client()
import cyrtranslit

templates={}   
templates["NCM"] = "Many of these things are -.It concerns Ana's -.I am selling various -.It is hidden in the -.He is standing there with his -.He stands there with many of his -"
templates["NCF"] = "Many of these things are -.Ana is looking at-.He is standing there with his -.He stands there with many of his -"
templates["NCN"] = ".It is hidden in the -.I am selling various -.He is standing there with his -.He stands there with many of his -"
#templates["AGP"] = ""

def check_lemma(word, lemma):
    doc=nlp(word)
    doc_dict=doc.to_dict()[0][0][0]
    nlemma=doc_dict['lemma']
    return nlemma[:2]==lemma[:2 ]

def gdeklinacije(word, pos, client):
    eword = client.translate(word, target_language=ENGLISH_ISO_639, source_language="sr")["translatedText"]
    gdec = []
    gdec.append(word)
    if pos in templates:
        res = client.translate(templates[pos].replace("-",eword), target_language="sr", source_language=ENGLISH_ISO_639)["translatedText"].split(".")
        for r in res:
            nword = cyrtranslit.to_latin(r.split(" ")[-1])
            if check_lemma(nword,word):
                gdec.append(nword)
            else: gdec.append("")                
    else:
        pos = "UNK"
        res = ""
    return gdec    

with open("/home/branimir/Projects/algolia-sr/test/lista10.txt",'r',encoding='utf8') as lista_reci:
    with open("/home/branimir/Projects/algolia-sr/test/nova_lista10.txt", 'w',encoding='utf8') as nova_lista_reci:
        for rec in lista_reci:
            doc=nlp(rec.rstrip())
            doc_dict=doc.to_dict()[0][0][0]
            lemma=doc_dict['lemma']
            pos=doc_dict['xpos']
            #nova_lista_reci.write(" ".join(deklinacije(lemma=doc_dict['lemma'], pos=doc_dict['xpos']))+"\n")
            dec = deklinacije(lemma=lemma, pos=pos)
            gdec = gdeklinacije(word=lemma, pos=pos.upper()[:3], client=client)
            cdec = list(itertools.zip_longest(dec, gdec, fillvalue=""))
            same = 0
            for c in cdec:
                if c[0]==c[1]: same+=1   
            print(same, cdec)
            #print(same, dec, gdec)


