from ttkbootstrap import Style
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk

# FONKSİYONLAR ;

def birim1_arti():
    global birim1
    try:
        sayi = float(birim1.get())
        sayi += 1
        birim1.delete(0,len(birim1.get()))
        birim1.insert(0,str(sayi))
    except ValueError:
        messagebox.showerror("Tip Hatası","Lütfen sayısal bir değer giriniz.")
def birim1_eksi():
    global birim1
    try:
        if float(birim1.get()) > 0:
            sayi = float(birim1.get())
            sayi -= 1
            birim1.delete(0,len(birim1.get()))
            birim1.insert(0,str(sayi))
    except ValueError:
        messagebox.showerror("Tip Hatası","Lütfen sayısal bir değer giriniz.")
def kontrol():
    global birim,x,y,tip_indis
    indis1 = 0
    indis2 = 0
    birim = ""
    birim1 = ""
    birim2 = ""
    while indis1 < len(tipler):
        try:
            if tipler[indis1].index(birim1_tip.get()):
                birim1 = tipler[indis1][0]
                tip_indis = indis1
                x = (len(tipler[indis1]) - 1) - tipler[indis1].index(birim1_tip.get())
                break
        except ValueError:
            indis1 += 1
            continue
    while indis2 < len(tipler):
        try:
            if tipler[indis2].index(birim2_tip.get()):
                birim2 = tipler[indis2][0]
                y = (len(tipler[indis2]) - 1) - tipler[indis2].index(birim2_tip.get())
                break
        except ValueError:
            indis2 += 1
            continue
    if birim1 == birim2 and not "":
        birim = birim1
        return True
    else:
        return False
def donustur():
    if kontrol():
        kat = 1
        try:
            if birim == "uzunluk":
                carpanlar = [10,100,1000]
                if x > y:
                    for i in carpanlar[y:x]:
                        kat *= i
                    sonuc = float(birim1.get()) * kat
                    messagebox.showinfo("Sonuç","{} {} eşittir: {} {}".format(birim1.get(),birim1_tip.get(),sonuc,birim2_tip.get()))
                if x < y:
                    for i in carpanlar[x:y]:
                        kat *= i
                    sonuc = float(birim1.get()) / kat
                    messagebox.showinfo("Sonuç","{} {} eşittir: {} {}".format(birim1.get(),birim1_tip.get(),sonuc,birim2_tip.get()))
            if birim == "hacim":
                if x > y:
                    sonuc = (10 ** (x-y)) * float(birim1.get())
                    messagebox.showinfo("Sonuç","{} {} eşittir: {} {}".format(birim1.get(),birim1_tip.get(),sonuc,birim2_tip.get()))
                if x < y:
                    sonuc = float(birim1.get()) / (10 ** abs(x-y))
                    messagebox.showinfo("Sonuç","{} {} eşittir: {} {}".format(birim1.get(),birim1_tip.get(),sonuc,birim2_tip.get()))
            if birim == "ağırlık":
                if x > y:
                    sonuc = (1000 ** (x-y)) * float(birim1.get())
                    messagebox.showinfo("Sonuç","{} {} eşittir: {} {}".format(birim1.get(),birim1_tip.get(),sonuc,birim2_tip.get()))
                if x < y:
                    sonuc = float(birim1.get()) / (1000 ** abs(x-y))
                    messagebox.showinfo("Sonuç","{} {} eşittir: {} {}".format(birim1.get(),birim1_tip.get(),sonuc,birim2_tip.get()))
            if birim == "zaman":
                if x > y:
                    sonuc = (60 ** (x-y)) * float(birim1.get())
                    messagebox.showinfo("Sonuç","{} {} eşittir: {} {}".format(birim1.get(),birim1_tip.get(),sonuc,birim2_tip.get()))
                if x < y:
                    sonuc = float(birim1.get()) / (60 ** abs(x-y))
                    messagebox.showinfo("Sonuç","{} {} eşittir: {} {}".format(birim1.get(),birim1_tip.get(),sonuc,birim2_tip.get()))
        except ValueError:
            messagebox.showerror("Tip Hatası","Lütfen sayısal bir değer giriniz.")
    else:
        messagebox.showerror("Tip Hatası","{} birimi {} birimine dönüştürülebilir değildir.".format(birim1_tip.get(),birim2_tip.get()))

# ARABİRİM ;

pencere = tk.Tk()
tipler = [["ağırlık","ton","kg","gr","mg"],["uzunluk","km","m","cm","mm"],["hacim","hl","dal","l","dl","ml"],["zaman","saat","dakika","saniye"]]
tip = ""
tip_indis = 0
x,y = 0,0
kategoriler = [tipler[0][0].title(), tipler[1][0].title(), tipler[2][0].title(), tipler[3][0].title()]
pencere.title("Birim Dönüştürücü")
pencere.geometry("400x210")
pencere.resizable(0,0)

# STİL
style = Style(theme='minty')
pencere = style.master

arti_resim = ImageTk.PhotoImage(Image.open("res/arti.png"))
eksi_resim = ImageTk.PhotoImage(Image.open("res/eksi.png"))
cevir_resim = ImageTk.PhotoImage(Image.open("res/cevir.png"))
ikon = ImageTk.PhotoImage(Image.open("res/ikon.png"))
pencere.wm_iconphoto(True,ikon)

birim1_etiket = tk.Label(text = "Değer :")
birim1_etiket.place(x=20, y=20)

birim1 = tk.Entry(width=22)
birim1.insert(0,"0")
birim1.place(x=120,y=20)

birim_kategori_etiket = tk.Label(text = "Kategori :")
birim_kategori_etiket.place(x=20, y=70)

birim_kategori = ttk.Combobox()
birim_kategori["values"] = kategoriler
birim_kategori.place(x=120,y=65)

birim1_tip_etiket = tk.Label(text = "Girdi Birimi :")
birim1_tip_etiket.place(x=20, y=120)

birim1_tip = ttk.Combobox(state='readonly')
birim1_tip["values"] = str([x[1:] for x in tipler]).replace("[","").replace("]","").replace("'","").replace(",","")
birim1_tip.place(x=120,y=115)

birim2_tip_etiket = tk.Label(text = "Çıktı Birimi :")
birim2_tip_etiket.place(x=20, y=170)

birim2_tip = ttk.Combobox(state='readonly')
birim2_tip["values"] = str([x[1:] for x in tipler]).replace("[","").replace("]","").replace("'","").replace(",","")
birim2_tip.place(x=120,y=165)

birim1_btn = tk.Button(command=birim1_arti,image=arti_resim)
birim1_btn.place(x=325,y=20)

birim1_btn2 = tk.Button(command=birim1_eksi,image=eksi_resim)
birim1_btn2.place(x=325,y=80)

donustur_btn = tk.Button(command=donustur,image=cevir_resim)
donustur_btn.place(x=325,y=140)
pencere.mainloop()
