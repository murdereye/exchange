import requests
from bs4 import BeautifulSoup
import re

def detail(money,select,to):
    fonklist=listem
    fixedmoneys=[]
    themoney=1
    if "Türk" in fonklist[0]:
        fonklist.remove(fonklist[0])
    
    if "Türk" in select:
        for i in mlist:
            fixedmoneys.append(float(money)/float(i))
    else:
        listwithmoney=list(zip(fonklist,mlist))
        themoney=1
        for j in listwithmoney:
            if select==j[0]:
                themoney=float(j[1])
        for i in listwithmoney:
            fixedmoneys.append(themoney*float(money)/float(i[1]))

    resultlist=[]    
    final=list(zip(fonklist,fixedmoneys))
    if "Türk" not in final:
        final.insert(0,["Türk Lirası - TRY" ,themoney*float(money)])
    for x in final:
        if x[0]!=select:
            resultlist.append([x[0],format(x[1],'.2f')])
    fonklist=listem
    return resultlist
    
def fun(money,select,to):
    global mlist
    mlist=[]
    x=requests.get('https://kur.doviz.com/')
    soup=BeautifulSoup(x.text,"html.parser")
    liste=[]
    x=False
    left=soup.find_all("td")
    for l in left:
    	if l.get_text()!="":
    		if "USD" in l.get_text() or x:
    			liste.append(l.get_text())
    			x=True
    	
    	# select=input("\nNe çevrilecek: ")
    	# money=input("Miktar: ")
    	# to=input("Neye çevrilecek: ")
    for a in range(len(liste)):
        try:
            if liste[a] in listem:
                mlist.append(liste[a+2].replace(',','.'))
        except:
            break
    for i in range(len(liste)):
    	if to in liste[i]:
    		if select in "Türk Lirası - TRY":
                    result=float(money)/float((liste[i+2].replace(',','.')))
                    return(f"{format(result,'.2f')}")
    			# clc.config(text=liste[i+1])
    	if select in liste[i]:
    		if to in "Türk Lirası - TRY":
    			result=float(liste[i+2].replace(',','.'))*float(money)
    			# clc.config(text=liste[i+1])
    			return(f"{format(result,'.2f')}")
    		else:	
    			for j in range(len(liste)):
    					if to in liste[j]:
    						result=float(liste[i+2].replace(',','.'))*float(money)/float(liste[j+2].replace(',','.'))
    						return(f"{format(result,'.2f')}")
    						# clc.config(text=liste[i+1])

def firstfun():
    x=requests.get('https://kur.doviz.com/')
    soup=BeautifulSoup(x.text,"html.parser")
    global listem
    listem=[]
    x=False
    left=soup.find_all("td")
    pattern=re.compile(r'\D')
    patter=re.compile(r'\w')
    listem.append("Türk Lirası - TRY")
    for l in left:
    		if l.get_text()!="":
    			if "USD" in l.get_text() or x:
    				if pattern.match(l.get_text().lower()) or "yen" in l.get_text().lower():
    					if patter.match(l.get_text().lower()):
    						listem.append(l.get_text())
    						x=True
    return list(listem)