import sqlite3 as sql 
from time import sleep
from tkinter import *
from tkinter import messagebox
import tkinter
from PIL.ImageTk import PhotoImage
from tkinter import ttk
import pygame

db = sql.connect("sifreler.db")
sorgu = """CREATE TABLE IF NOT EXISTS sifreler(uygulama_adi,K_ad,sifre)"""
imlec = db.cursor()
imlec.execute(sorgu)
def db_input(x,y,z):
    global db,imlec
    veri= "INSERT INTO sifreler VALUES ('{}','{}','{}')"
    imlec.execute(veri.format(x,y,z))
    db.commit()
    
def delete(x):
    global db,imlec
    veri = "DELETE FROM sifreler WHERE uygulama_adi = '{}'"
    imlec.execute(veri.format(x))
    db.commit()
    

def liste():
    global imlec,db
    tablo=ttk.Treeview()
    tablo["column"]=("A","B","C")
    tablo.column("#0",width=50)
    tablo.column("A",width=80)
    tablo.column("B",width=140)
    tablo.column("C",width=420)
    
    
    tablo.heading("#0",text="ID")
    tablo.heading("A",text="Uygulam ADI")
    tablo.heading("B",text="kullanıcı Adı")
    tablo.heading("C",text="Şifre")
    #tablo.insert("","end",text=str(2),values=("1","1","12"))
    say=0
    imlec=db.cursor()
    imlec.execute("select * from sifreler")
    v=imlec.fetchall()
    for i in v:
        
        tablo.insert("","end",text=str(say),values=(i[0],i[1],i[2]))
        say+=1
    tablo.place(relx="0.001",rely="0.1")
    
    
def update(y,z):
    global db,imlec
     
    veri1 = "UPDATE sifreler SET uygulama_adi='{}' WHERE uygulama_adi='{}'"
    imlec.execute(veri1.format(y,z))
    db.commit()
    
    veri2 = "UPDATE sifreler SET K_ad='{}' WHERE K_ad='{}'"
    imlec.execute(veri2.format(y,z))
    db.commit()
    
    veri3 = "UPDATE sifreler SET sifre='{}' WHERE sifre='{}'"
    imlec.execute(veri3.format(y,z))
    db.commit()
    

def main(sec):
    global ad,k_ad,sifre 
    if sec=="1":
        app=ad.get()
        k=k_ad.get()
        s=sifre.get()
        db_input(app,k,s)
        liste()
    elif sec=="2": 
        app=ad.get()
        k=k_ad.get()
        s=sifre.get()
        update(sec,isim,yeni_ad)
        liste()
    elif sec=="3":
            liste()
    elif sec=="q" or sec=="Q":
        db.close()
        
    elif sec=="4":
        app=ad.get()
        delete(app)
        liste()
def close():
    global pencere
    if messagebox.askokcancel("DİKKAT", "Kapatılacak"):
        db.close()
        pencere.destroy()   
    
             
pencere = Tk()
pygame.init()
pygame.mixer.init()
img=PhotoImage(file="arka_plan.gif")
pencere.geometry("700x400")
pencere.resizable(width=TRUE, height=FALSE)   

pygame.init()
pygame.mixer.init()
img=PhotoImage(file="arka_plan.gif")
labelarka=Label(image=img).place(relx="0",rely="0")

ekle=Button(text="Şifre Ekle",command=lambda:main("1")).place(relx="0.0",rely="0.0")
guncelle=Button(text="database kapat",bg="red",command=lambda:close()).place(relx="0.310",rely="0.0")
sil=Button(text="Şifre Sil ",command=lambda:main("4")).place(relx="0.7",rely="0.0")
#listele=Button(text="Şifreleri Listele",command=lambda:main("3")).place(relx="0.700",rely="0.0")

label_1=Label(text="Uygulama Adı:",bg="white").place(relx="0.0",rely="0.700")
label_1=Label(text="Şifre:",bg="white").place(relx="0.0",rely="0.900")
label_1=Label(text="Kullanıcı Adı:",bg="white").place(relx="0.0",rely="0.800")
pencere.protocol("WM_DELETE_WINDOW", lambda:close())
ad=Entry()
ad.place(relx="0.3",rely="0.700")
k_ad=Entry()
k_ad.place(relx="0.3",rely="0.800")
sifre=Entry()
sifre.place(relx="0.3",rely="0.900")
liste()
pencere.mainloop()


        
    
    
    
    
    