from ttkbootstrap import Style
from tkinter import ttk
import tkinter as tk
import webbrowser
import pyperclip

# ARABİRİM
style = Style(theme='superhero')  # superhero, journal, minty, lumen, morph, darkly

window = style.master
window.geometry("400x250+500+300")
window.resizable(0, 0)
window.title("Birim Dönüştürücü")

# create a notebook
notebook = ttk.Notebook(window)
notebook.pack(pady=10, expand=True)

# create frames
frame1 = ttk.Frame(notebook, width=400, height=250)
frame2 = ttk.Frame(notebook, width=400, height=250)
frame3 = ttk.Frame(notebook, width=400, height=250)
frame4 = ttk.Frame(notebook, width=400, height=250)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
frame4.pack(fill='both', expand=True)

# add frames to notebook
notebook.add(frame1, text='Uzunluk')
notebook.add(frame2, text='Alan')
notebook.add(frame3, text='Hacim')
notebook.add(frame4, text='Hakkında')

# ölçü birimleri
tip_uzunluk = ("km","hm", "dkm","m","dm","cm","mm")
tip_agirlik = ("ton","kg","gr","mg")
tip_hacim = ("hl","dal","l","dl","ml")
tip_zaman = ("saat","dakika","saniye")

# UZUNLUK SEKMESİ WİDGET'LARI
etiket_girdi_deger_uzn = ttk.Label(frame1, text = "Değer :")
etiket_girdi_deger_uzn.place(x=20, y=20)

entry_girdi_uzn = ttk.Entry(frame1, width=22)
entry_girdi_uzn.insert(0,"0")
entry_girdi_uzn.place(x=120,y=20)

etiket_girdi_birim_uzn = ttk.Label(frame1, text = "Girdi Birimi :")
etiket_girdi_birim_uzn.place(x=20, y=60)

kombo_uzunluk_girdi_uzn = ttk.Combobox(frame1, state='readonly')
kombo_uzunluk_girdi_uzn["values"] = tip_uzunluk
kombo_uzunluk_girdi_uzn.place(x=120,y=60)

etiket_cikti_birim_uzn = ttk.Label(frame1, text = "Çıktı Birimi :")
etiket_cikti_birim_uzn.place(x=20, y=100)

kombo_uzunluk_cikti_uzn = ttk.Combobox(frame1, state='readonly')
kombo_uzunluk_cikti_uzn["values"] = tip_uzunluk
kombo_uzunluk_cikti_uzn.place(x=120,y=100)

etiket_sonuc_uzn = ttk.Label(frame1, text = "Sonuç :")
etiket_sonuc_uzn.place(x=20, y=140)

entry_sonuc_uzn = ttk.Entry(frame1, width=22, state="normal")
entry_sonuc_uzn.insert(0,"Sonuc")
entry_sonuc_uzn.place(x=120,y=140)

def hesapla_aktar_uzn():
	entry_sonuc_uzn.delete(0, "end")
	entry_sonuc_uzn.insert(0, hesapla_uzn())
	
def hesapla_uzn():
    deger = int(entry_girdi_uzn.get())
    girdi_brm = kombo_uzunluk_girdi_uzn.get()
    cikti_brm = kombo_uzunluk_cikti_uzn.get()
    
    girdi_indeks = tip_uzunluk.index(girdi_brm)+1
    cikti_indeks = tip_uzunluk.index(cikti_brm)+1
    
    return (deger * 10**(cikti_indeks- girdi_indeks))
    
def kopyala_uzn():
	pyperclip.copy(entry_sonuc_uzn.get())
	

buton_kopyala_uzn = ttk.Button(frame1, text = "Kopyala", command=kopyala_uzn)
buton_kopyala_uzn.place(x=300,y=50)

buton_donustur_uzn = ttk.Button(frame1, text = "Dönüştür", command=hesapla_aktar_uzn)
buton_donustur_uzn.place(x=300,y=100)


# HAKKINDA
etiket_uygulama = ttk.Label(frame4, text = "\nBirim Dönüştürücü\nVersiyon 0.2")
etiket_uygulama.pack(expand="YES")

def baglantiya_git(url):
    webbrowser.open_new(url)

etiket_baglanti = ttk.Button(frame4, text = "https://github.com/mhalil/birim-donusturme", style='Link.TButton')
etiket_baglanti.pack(expand="YES")
etiket_baglanti.bind("<Button-1>", lambda e: baglantiya_git("https://github.com/mhalil/birim-donusturme"))


window.mainloop()
