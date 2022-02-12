import adjectif
import adverbe
import conjonction
import demonstratif
import nom
import preposition
import pronom_personnel as pp
import pronom_relatif as pr
import sqlite3
import verbe
import sys
txt=str(sys.argv[1]).lower()
print("\n"*3)
if txt[-1]==".":
	txt=txt[:-1]
txt=txt.split(".")
analyse=[]
for phrase in txt:
	phrase = phrase.split(",")
	analyse_phrase=[]
	for prop in phrase:
		prop = prop.split(" ")
		analyse_prop={}
		for mot in prop:
			result=[]
			nature=""
			if nom.nom(mot)!=None:
				result = nom.nom(mot)
				nature="nom"
				print(f"<b>{mot}</b>: <i>{result}</i><br>")
			elif adverbe.adverbe(mot)!=None and result==[]:
				result = adverbe.adverbe(mot)
				nature="adverbe"
				print(f"<b>{mot}</b>: <i>{result}</i><br>")
			
			elif conjonction.conj(mot)!=None and result==[]:
				result = conjonction.conj(mot)
				nature="conjonction"
				print(f"<b>{mot}</b>: <i>{result}</i><br>")
			
			elif preposition.prep(mot)!=None and result==[]:
				result = preposition.prep(mot)
				nature="preposition"
				print(f"<b>{mot}</b>: <i>{result}</i><br>")
			
			elif adjectif.adjectif(mot)!=None and result==[]:
				result = adjectif.adjectif(mot)
				nature="adjectif"
				print(f"<b>{mot}</b>: <i>{result}</i><br>")
			
			elif adjectif.comparatif(mot)!=None and result==[]:
				result = adjectif.comparatif(mot)
				nature="comparatif"
				print(f"<b>{mot}</b>: <i>{result}</i><br>")
			
			elif adjectif.superlatif(mot)!=None and result==[]:
				result=adjectif.superlatif(mot)
				nature="superlatif"
				print(f"<b>{mot}</b>: <i>{result}</i><br>")
			
			elif demonstratif.demonstratif(mot)!=None and result==[]:
				result=demonstratif.demonstratif(mot)
				nature="demonstratif"
				print(f"<b>{mot}</b>: <i>{result}</i><br>")
			
			elif pp.personel(mot)!=None and result==[]:
				result=pp.personel(mot)
				nature="pronom personnel"
				print(f"<b>{mot}</b>: <i>{result}</i><br>")
			elif pr.relatif(mot)!=None and result==[]:
				result=pr.relatif(mot)
				nature="pronom relatif"
				print(f"<b>{mot}</b>: <i>{result}</i><br>")
			
			elif verbe.verbe(mot)!=None and result==[]:
				result=verbe.verbe(mot)
				nature="verbe"
				print(f"<b>{mot}</b>: <i>{result}</i><br>")
			elif verbe.conj_etre(mot)!=None and result==[]:
				result=verbe.conj_etre(mot)
				nature="Verbe Etre"
				print(f"<b>{mot}</b>: <i>{result}</i><br>")
			else:
				print(f'<b>{mot}</b>: <i>{result}</i>')
			analyse_prop[mot]=(nature,result)
		analyse_phrase.append(analyse_prop)
		print("<br>")
	analyse.append(analyse_phrase)
# print(analyse)