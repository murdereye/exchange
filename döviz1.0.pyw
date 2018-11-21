import requests
from bs4 import BeautifulSoup
from tkinter import *		
from tkinter import ttk
import re

window=Tk(className=" Döviz Uygulaması")
window.config(background="green")
window.geometry('500x140')
window.resizable(False, False)

def detail():
    frame=Tk(className=" Tüm Paralar")
    frame.geometry('290x532')
    fonklist=listem
    lb=Text(frame,height=33,width=38,bg="green",fg="white",font="Helvetica 10 bold")
    lb.grid(row=1,column=0)
    sb=Scrollbar(frame)
    sb.grid(row=1,column=1,sticky='ns')
    lb.configure(yscrollcommand=sb)
    sb.configure(command=lb.yview)
    frame.iconbitmap(r"money-bag-256.ico")
    
    fixedmoneys=[]
    themoney=1
    if "Türk" in fonklist[0]:
        fonklist.remove(fonklist[0])
    
    if "Türk" in c.get():
        for i in mlist:
            fixedmoneys.append(float(m.get().replace(',','.'))/float(i))
    else:
        listwithmoney=list(zip(fonklist,mlist))
        themoney=1
        for j in listwithmoney:
            if c.get()==j[0]:
                themoney=float(j[1])
        for i in listwithmoney:
            fixedmoneys.append(themoney*float(m.get())/float(i[1]))

        
    final=list(zip(fonklist,fixedmoneys))
    if "Türk" not in final:
        final.insert(0,["Türk Lirası - TRY" ,themoney*float(m.get())])
    for x in final:
        if x[0]!=c.get():
            lb.insert(END,"{}\t<==>\t{}\n\n".format(x[0],format(x[1],'.2f')))
    fonklist=listem
    frame.mainloop()

    
def swap():
    global temp,c,k
    temp=c
    c=k
    k=temp
    t2.config(textvariable=c)
    t3.config(textvariable=k)
def fun():
    global mlist
    mlist=[]
    if not c.get() or not k.get():
        return
    clock=Label(window,text="Saat",bg="green",fg="white")
    clock.grid(row=7,column=4) 
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
    select=c.get()
    money=float(m.get())
    to=k.get()
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
    			res.delete("1.0 ", END)
    			res.insert(END,format(result,'.2f'))
    			clc.config(text=liste[i+1])
    	if select in liste[i]:
    		if to in "Türk Lirası - TRY":
    			result=float(liste[i+2].replace(',','.'))*float(money)
    			res.delete("1.0 ", END)
    			res.insert(END,format(result,'.2f'))
    			clc.config(text=liste[i+1])
    				#print(f"{money} {liste[i]} = {format(result,'.2f')} Türk Lirası")
    		else:	
    			for j in range(len(liste)):
    					if to in liste[j]:
    						result=float(liste[i+2].replace(',','.'))*float(money)/float(liste[j+2].replace(',','.'))
    						res.delete("1.0 ", END)
    						res.insert(END,format(result,'.2f'))
    						clc.config(text=liste[i+1])
    							#print(f"{money} {liste[i]} = {format(result,'.2f')} {liste[j]}
    b3=Button(window,text="Tüm Paralar",command=detail,bg="gold")
    b3.grid(row=7,column=2)

window.iconbitmap(r"money-bag-256.ico")
e1=Label(window,text="Çevrilecek para birimi",bg="green",fg="white",font="Helvetica 10 bold")
e1.grid(row=0,column=2)
e2=Label(window,text="Çevrilecek para miktarı",bg="green",fg="white",font="Helvetica 10 bold")
e2.grid(row=0,column=0)
e2=Label(window,text="Neye çevrilecek",bg="green",fg="white",font="Helvetica 10 bold")
e2.grid(row=0,column=4)
global temp, c, k
temp=StringVar()
k=StringVar() 
m=StringVar()
c=StringVar()
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

b1=Button(window,text="Çevir",command=fun,bg="gold",font="Helvetica 13")
b1.grid(row=5,column=0)
b2=Button(window,text="<==>",command=swap,width=3,bg="green",fg="white",font="Helvetica 9 bold")
b2.grid(row=1,column=3)

t1=Entry(window,textvariable=m)  #para miktarı
t1.grid(row=1,column=0)
t1.insert("1","1")
 
t2=ttk.Combobox(window,textvariable=c) # para birimi
t2.grid(row=1,column=2)
t2.config(values=listem)
 
t3=ttk.Combobox(window,textvariable=k) # çevrilecek birim
t3.config(values=listem)
t3.grid(row=1,column=4)

res=Text(window,height=1,width=10)
res.grid(row=7,column=0)

clc=Label(window,text="",height=1,width=5,bg="green",fg="white")
clc.grid(row=8,column=4)
 
window.mainloop()