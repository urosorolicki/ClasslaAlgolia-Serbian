Running CLASSLA
Getting started
To run the CLASSLA pipeline for the first time on processing standard Slovenian, follow these steps:

>>> import classla
>>> classla.download('sl')                            # download standard models for Slovenian, use hr for Croatian, sr for Serbian, bg for Bulgarian, mk for Macedonian
>>> nlp = classla.Pipeline('sl')                      # initialize the default Slovenian pipeline, use hr for Croatian, sr for Serbian, bg for Bulgarian, mk for Macedonian
>>> doc = nlp("France Prešeren je rojen v Vrbi.")     # run the pipeline
>>> print(doc.to_conll())                             # print the output in CoNLL-U format
# newpar id = 1
# sent_id = 1.1
# text = France Prešeren je rojen v Vrbi.
1	France	France	PROPN	Npmsn	Case=Nom|Gender=Masc|Number=Sing	4	nsubj	_	NER=B-PER
2	Prešeren	Prešeren	PROPN	Npmsn	Case=Nom|Gender=Masc|Number=Sing	1	flat_name	_	NER=I-PER
3	je	biti	AUX	Va-r3s-n	Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin	4	cop	_	NER=O
4	rojen	rojen	ADJ	Appmsnn	Case=Nom|Definite=Ind|Degree=Pos|Gender=Masc|Number=Sing|VerbForm=Part	0	root	_	NER=O
5	v	v	ADP	Sl	Case=Loc	6	case	_	NER=O
6	Vrbi	Vrba	PROPN	Npfsl	Case=Loc|Gender=Fem|Number=Sing	4	obl	_	NER=B-LOC|SpaceAfter=No
7	.	.	PUNCT	Z	_	4	punct	_	NER=O

