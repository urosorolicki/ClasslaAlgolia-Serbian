import itertools
import classla
#classla.download('sr') # <--- FRIST RUN AND DOWNLOAD 
nlp = classla.Pipeline('sr')
from deklinacije import deklinacije
import csv
import re # <-- Optional 
import pandas as pd # <-- optional

from google.cloud.translate_v2.client import ENGLISH_ISO_639
from google.cloud import translate_v2 as translate
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/ladmin/Desktop/yourgooglecloudcredentials.json" # <---- you can get them on https://cloud.google.com/ !!
client = translate.Client()
import cyrtranslit # <--- !! 

known_pos = ["NCM", "NCF", "NCN", "AGP", "AGC", "ASC"]

templates={}   
templates["NCM"] = "Many of these things are -.It concerns Ana's -.I am selling various -.It is hidden in the -.He is standing there with his -.He stands there with many of his -"
templates["NCF"] = "Many of these things are -.Ana is looking at-.He is standing there with his -.He stands there with many of his -"
templates["NCN"] = ".It is hidden in the -.I am selling various -.He is standing there with his -.He stands there with many of his -"


def check_lemma(word, lemma):
    return word[:2]==lemma[:2 ]
    
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

headerList = ['language', 'objectID', 'word', 'type']

with open("Recnik_flow.csv") as f, open("ananas_flow4.csv", "w") as w:
	lines = list(f)
	w.write(lines[0]) # <-- Write headers to new file, also optional!

	for n, l in enumerate(lines[1:], 1):
		w.write(re.sub(r"\d+,\s*$", str(n)+",\n", l))
def generate_dec_f2f(f1,f2):
    with open(f1,'r',encoding='utf8') as File:
        with open(f2, 'w',encoding='utf8',newline='') as File2:
            csvwriter = csv.writer(File2)
            for rec in File:
                doc=nlp(rec.rstrip())
                doc_dict=doc.to_dict()[0][0][0]
                lemma=doc_dict['lemma']
                pos=doc_dict['xpos']
                pos = pos.upper()[:3]
                if pos in known_pos:
                    dec = deklinacije(lemma=lemma, pos=pos)
                    gdec = gdeklinacije(word=lemma, pos=pos, client=client)
                    udec = list(set(dec) | set(gdec))
                    csvwriter.writerow(udec)
                    cdec = list(itertools.zip_longest(dec, gdec, fillvalue=""))
                    same = 0
                    for c in cdec:
                        if c[0]==c[1]: same+=1   
                    print(same, cdec)
                    #print(same, dec, gdec)
f1 = "/Users/ladmin/Desktop/File.csv"
f2 = "/Users/ladmin/Desktop/File2.csv"
generate_dec_f2f(f1,f2)
